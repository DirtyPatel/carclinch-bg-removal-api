import os
import shutil
from typing import Union

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# Ensure the images directory exists
IMAGES_DIR = "images"
os.makedirs(IMAGES_DIR, exist_ok=True)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload-image")
def upload_image(image: UploadFile = File(...)):
    file_path = os.path.join(IMAGES_DIR, image.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {
        "filename": image.filename,
        "message": "Image uploaded successfully"
    }