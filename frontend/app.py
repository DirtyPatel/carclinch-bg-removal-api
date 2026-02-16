import os
import base64
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_URL = os.getenv("BG_REMOVE_API_URL", "http://localhost:8000").rstrip("/")

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/remove")
def remove():
    if "image" not in request.files:
        return render_template("index.html", error="No file uploaded.")

    f = request.files["image"]
    if not f.filename:
        return render_template("index.html", error="Please choose a file.")

    # Change these to match your API if needed
    endpoint = f"{API_URL}/remove-bg"   # <-- likely needs adjustment
    files = {"image": (f.filename, f.stream, f.mimetype or "application/octet-stream")}

    try:
        r = requests.post(endpoint, files=files, timeout=120)
        r.raise_for_status()

        # If API returns image bytes (PNG), show it
        img_b64 = base64.b64encode(r.content).decode("utf-8")
        data_url = f"data:image/png;base64,{img_b64}"

        return render_template("index.html", result=data_url)

    except requests.RequestException as e:
        return render_template("index.html", error=f"API error: {e}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
