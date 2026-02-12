from fastapi import FastAPI, UploadFile, Response
from PIL import Image
from pathlib import Path
import io
import sys

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from core import processor

app = FastAPI()


@app.post("/remove-bg")
async def remove_bg(file: UploadFile, model: str = "u2net"):
    # 1. load the upload
    input_bytes = await file.read()
    input_img = Image.open(io.BytesIO(input_bytes))

    # 2. process using the shared library
    output_img, _ = processor.process_image(input_img, model_name=model)

    # 3. return the PNG
    img_byte_arr = io.BytesIO()
    output_img.save(img_byte_arr, format="PNG")
    return Response(content=img_byte_arr.getvalue(), media_type="image/png")
