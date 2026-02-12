import os
import shutil
from typing import Union

from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI()

# Ensure the images directory exists
IMAGES_DIR = "images"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
os.makedirs(IMAGES_DIR, exist_ok=True)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload-image")
def upload_image(image: UploadFile = File(...)):
    
    #Check if the uploaded file has a valid image extension
    extension = image.filename.split(".")[-1].lower()
    if extension not in IMAGE_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file extension.")
    
    #Check if the uploaded file is an image based on its content type
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File is not an image.")
    
    file_path = os.path.join(IMAGES_DIR, image.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {
        "filename": image.filename,
        "message": "Image uploaded successfully"
    }