from pathlib import Path
from typing import Union, Optional, Tuple, cast
import numpy as np
from PIL import Image
from rembg import remove, new_session
from functools import lru_cache


@lru_cache(maxsize=1)
def get_session(model_name: str):
    """
    Maintains a single model session in memory.
    Uses LRU cache with maxsize=1 to ensure that when a new model is loaded,
    the previous one is evicted to free up VRAM/RAM.
    """
    return new_session(model_name)


def process_image(
    input_data: Union[str, Path, Image.Image],
    model_name: str,
    max_size: Optional[Tuple[int, int]] = (1024, 1024),
) -> Tuple[Image.Image, np.ndarray]:
    """
    The primary entry point for background removal.

    This function handles:
    1. Input normalization (Path/String to PIL Image).
    2. Optional resizing for performance consistency.
    3. Background removal via the rembg session.
    4. Type-safe conversion of results into a visual Image and a boolean Mask.

    Returns:
        - A PIL Image (RGBA) with the background removed.
        - A boolean numpy array (Mask) where True indicates foreground.
    """
    # Load image if a path is provided
    if isinstance(input_data, (str, Path)):
        img = Image.open(input_data).convert("RGBA")
    else:
        img = input_data.convert("RGBA")

    # Resize for consistency if max_size is provided
    if max_size:
        if img.width > max_size[0] or img.height > max_size[1]:
            img.thumbnail(max_size, Image.Resampling.LANCZOS)

    session = get_session(model_name)

    # rembg.remove returns Union[bytes, Image, ndarray].
    # Since we provide an Image, it returns an Image.
    result = remove(img, session=session)

    # Type Guard for the checker
    if not isinstance(result, Image.Image):
        if isinstance(result, np.ndarray):
            result = Image.fromarray(result)
        else:  # it's bytes
            import io

            result = Image.open(io.BytesIO(result)).convert("RGBA")

    output_img = cast(Image.Image, result)

    # Generate boolean mask from the alpha channel
    alpha = np.array(output_img)[:, :, 3]
    mask = alpha > 0

    return output_img, mask


def clear_sessions():
    """Explicitly clears the model cache to free resources."""
    get_session.cache_clear()
