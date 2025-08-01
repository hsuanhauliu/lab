# Definitions of RPC request and response data.

from pydantic import BaseModel
from typing import List


# Inference Request format.
class InferenceRequest(BaseModel):
    base64_img: str  # base64 encoded image


# Inference Response format.
class InferenceResponse(BaseModel):
    """
    Inference response containing the results.

    The order of both lists align with each other.
    """
    bounding_boxes: List[dict[str, int]]
    classes: List[str]
