import os
import base64
import requests
import uuid
from io import BytesIO
from flask import Flask, render_template, request, send_file, abort

app = Flask(__name__)

API_URL = os.getenv("BG_REMOVE_API_URL", "http://127.0.0.1:8000").rstrip("/")

# Simple in-memory cache for downloads (token -> png bytes)
DOWNLOAD_CACHE: dict[str, bytes] = {}
MAX_CACHE_ITEMS = 25  # avoid unbounded memory use


def _cache_put(token: str, data: bytes) -> None:
    DOWNLOAD_CACHE[token] = data
    # trim old items (FIFO-ish)
    while len(DOWNLOAD_CACHE) > MAX_CACHE_ITEMS:
        oldest_key = next(iter(DOWNLOAD_CACHE))
        DOWNLOAD_CACHE.pop(oldest_key, None)


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

    # Read uploaded bytes once (so we can preview it)
    uploaded_bytes = f.read()
    if not uploaded_bytes:
        return render_template("index.html", error="Uploaded file is empty.")

    uploaded_preview = (
        f"data:{f.mimetype or 'image/jpeg'};base64,"
        + base64.b64encode(uploaded_bytes).decode("utf-8")
    )

    endpoint = f"{API_URL}/upload-image"
    files = {"image": (f.filename, uploaded_bytes, f.mimetype or "application/octet-stream")}

    try:
        r = requests.post(endpoint, files=files, timeout=300)
        r.raise_for_status()

        content_type = (r.headers.get("Content-Type") or "").lower()
        if not content_type.startswith("image/"):
            # The API should return a PNG now; if it doesn't, show a helpful error
            return render_template(
                "index.html",
                error=f"API returned unexpected content-type: {content_type}. Body: {r.text[:300]}",
                uploaded_preview=uploaded_preview,
            )

        processed_bytes = r.content
        processed_preview = (
            "data:image/png;base64," + base64.b64encode(processed_bytes).decode("utf-8")
        )

        token = uuid.uuid4().hex
        _cache_put(token, processed_bytes)

        return render_template(
            "index.html",
            uploaded_preview=uploaded_preview,
            processed_preview=processed_preview,
            download_token=token,
        )

    except requests.RequestException as e:
        return render_template("index.html", error=f"API error: {e}", uploaded_preview=uploaded_preview)


@app.get("/download/<token>")
def download(token: str):
    data = DOWNLOAD_CACHE.get(token)
    if not data:
        abort(404)

    return send_file(
        BytesIO(data),
        mimetype="image/png",
        as_attachment=True,
        download_name="bg-removed.png",
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
