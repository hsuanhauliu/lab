# Logic for RPC request and response data.

import io
import base64

import cv2
from pydantic import BaseModel, field_validator
from typing import List, Union
import numpy as np


# Inference Request format.
class InferenceRequest(BaseModel):
    image: np.ndarray

    class Config:
        arbitrary_types_allowed = True

    @field_validator("image", mode="before")
    @classmethod
    def parse_coordinates(cls, v: str) -> np.ndarray:
        """
        Custom validator to parse base64 encoded image to Numpy array.
        """
        im_bytes = io.BytesIO(base64.b64decode(v))
        return cv2.imread(im_bytes)


# Inference Response format.
class InferenceResponse(BaseModel):
    bounding_boxes: List[np.ndarray]
    classes: List[str]

    class Config:
        arbitrary_types_allowed = True

