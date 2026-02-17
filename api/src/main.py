import io
from fastapi.responses import Response
from PIL import Image
import os
import shutil
from pathlib import Path
from fastapi import FastAPI, File, HTTPException, UploadFile
import sys
from fastapi.responses import FileResponse

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_dir))

from core import processor

app = FastAPI()

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def get_dirs() -> tuple[Path, Path, Path]:
    """
    Default behavior: saves under ./images.
    Tests can override with IMAGE_BASE_DIR.
    """
    base_dir = Path(os.getenv("IMAGE_BASE_DIR", "images"))
    input_dir = base_dir / "input"
    output_dir = base_dir / "output"
    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    return base_dir, input_dir, output_dir


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.on_event("startup")
def warmup():
    # force model download/init at startup (so first user request is stable)
    try:
        import numpy as np
        from PIL import Image
        # tiny dummy image
        tmp = Path("images/input")
        tmp.mkdir(parents=True, exist_ok=True)
        p = tmp / "warmup.jpg"
        Image.new("RGB", (64, 64), (255, 255, 255)).save(p)
        processor.process_image(str(p), model_name="u2net")
    except Exception as e:
        print("Warmup failed:", e)


@app.post("/upload-image")
def upload_image(image: UploadFile = File(...)):
    if not (image.content_type and image.content_type.startswith("image/")):
        raise HTTPException(status_code=400, detail="File is not an image.")

    original_name = Path(image.filename or "upload")
    ext = original_name.suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file extension.")

    # Read upload into memory
    data = image.file.read()
    image.file.close()

    # Open with PIL, downscale hard
    try:
        with Image.open(io.BytesIO(data)) as img:
            img = img.convert("RGB")
            img.thumbnail((384, 384))
            buf_in = io.BytesIO()
            img.save(buf_in, format="JPEG", quality=85)
    except Exception:
        raise HTTPException(status_code=400, detail="Could not read image.")

    # Process using a temp file OR bytes depending on your processor
    # If processor needs a path, we must write a temp file safely:
    _, input_dir, _ = get_dirs()
    tmp_path = input_dir / "upload_tmp.jpg"
    tmp_path.write_bytes(buf_in.getvalue())

    # Background removal
    output_img, _ = processor.process_image(str(tmp_path), model_name="u2net")

    # Return PNG bytes directly
    out_buf = io.BytesIO()
    output_img.save(out_buf, format="PNG")
    out_buf.seek(0)

    return Response(
        content=out_buf.getvalue(),
        media_type="image/png",
        headers={"Content-Disposition": 'attachment; filename="bg-removed.png"'},
    )
    
# @app.get("/download")
# def download(path: str):
#     # Basic safety: allow only files under images/output
#     safe_root = os.path.abspath("images/output")
#     requested = os.path.abspath(path)

#     if not requested.startswith(safe_root):
#         raise HTTPException(status_code=400, detail="Invalid path")

#     if not os.path.exists(requested):
#         raise HTTPException(status_code=404, detail="File not found")

#     return FileResponse(
#         requested,
#         media_type="image/png",
#         filename=os.path.basename(requested),
#     )
    
@app.head("/")
def head_root():
    return


