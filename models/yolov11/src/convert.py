# Helper functions for type conversion.
import io
import base64

import cv2
import numpy as np


def base64ToNumpyArray(img: str) -> np.ndarray:
    """Convert base64 image to numpy array."""
    if "," in img:
        # Split the string by the comma and take the second part
        img = img.split(',')[1]

    img = base64.b64decode(img)
    img = np.fromstring(img, dtype=np.uint8)
    return cv2.imdecode(img, cv2.IMREAD_COLOR)


def numpyArrayToBase64(img: np.ndarray) -> str:
    return base64.b64encode(img)


def boxToCoordinates(box) -> dict[str, int]:
    "Convert a Ultralytics Box class to dictionary of coordinates."
    bounding_box = box.xyxy[0].numpy()
    return {
        "left": int(bounding_box[0]),
        "top": int(bounding_box[1]),
        "right": int(bounding_box[2]),
        "bottom": int(bounding_box[3]),
    }