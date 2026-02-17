from PIL import Image
import os
import shutil
from pathlib import Path
from fastapi import FastAPI, File, HTTPException, UploadFile
import sys
from fastapi.responses import FileResponse

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


@app.post("/upload-image")
def upload_image(image: UploadFile = File(...)):
    if not (image.content_type and image.content_type.startswith("image/")):
        raise HTTPException(status_code=400, detail="File is not an image.")

    original_name = Path(image.filename or "upload")
    ext = original_name.suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file extension.")

    _, input_dir, output_dir = get_dirs()

    input_path = input_dir / original_name.name
    output_name = f"{original_name.stem}_processed.png"
    output_path = output_dir / output_name

    # ✅ 1. Save uploaded file
    try:
        with input_path.open("wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    finally:
        image.file.close()

    # ✅ 2. Downscale BEFORE background removal (THIS IS NEW)
    with Image.open(input_path) as img:
        img = img.convert("RGB")
        img.thumbnail((1024, 1024))  # reduce memory usage
        img.save(input_path, format="JPEG", quality=90)

    # ✅ 3. Now run background removal
    output_img, _ = processor.process_image(
        str(input_path),
        model_name="isnet-general-use"
    )

    output_img.save(output_path, format="PNG")

    return FileResponse(
        str(output_path),
        media_type="image/png",
        filename=output_path.name,
    )

    
@app.get("/download")
def download(path: str):
    # Basic safety: allow only files under images/output
    safe_root = os.path.abspath("images/output")
    requested = os.path.abspath(path)

    if not requested.startswith(safe_root):
        raise HTTPException(status_code=400, detail="Invalid path")

    if not os.path.exists(requested):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        requested,
        media_type="image/png",
        filename=os.path.basename(requested),
    )
    
@app.head("/")
def head_root():
    return


