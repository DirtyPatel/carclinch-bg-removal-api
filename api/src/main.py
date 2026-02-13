import os
import shutil
from pathlib import Path
from fastapi import FastAPI, File, HTTPException, UploadFile
import sys

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

    try:
        with input_path.open("wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    finally:
        image.file.close()

    output_img, _ = processor.process_image(str(input_path), model_name="isnet-general-use")
    output_img.save(output_path, format="PNG")

    return {
        "input_filename": input_path.name,
        "input_path": str(input_path),
        "output_filename": output_path.name,
        "output_path": str(output_path),
        "message": "Image uploaded and processed successfully",
    }
