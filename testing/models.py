from rembg import remove, new_session
from PIL import Image
import numpy as np
from functools import lru_cache


@lru_cache(maxsize=1)  # keep only one model in memory at a time
def get_session(model_name: str):
    return new_session(model_name)


def run_model(image: Image.Image, model_name: str) -> np.ndarray:
    session = get_session(model_name)
    output = remove(image, session=session)
    alpha = np.array(output)[:, :, 3]
    return alpha > 0


def clear_model_sessions():
    """Explicitly clear the LRU cache to free VRAM/RAM."""
    get_session.cache_clear()

