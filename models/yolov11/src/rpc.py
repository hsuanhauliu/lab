# Definitions of RPC request and response data.

from pydantic import BaseModel
from typing import List, Union


class Coordinate(BaseModel):
    """Bounding box coordinate"""
    left: int
    top: int
    right: int
    bottom: int


class ModelInfo(BaseModel):
    """Model information"""
    labels: List[str]
    layers: Union[int, None]
    parameters: Union[int, None]


# Inference Request format.
class InferenceRequest(BaseModel):
    base64_img: str  # base64 encoded image


# Inference Response format.
class InferenceResponse(BaseModel):
    """
    Inference response containing the results.

    The order of both lists align with each other.
    """

    bounding_boxes: List[Coordinate]
    classes: List[str]
    model_info: ModelInfo
