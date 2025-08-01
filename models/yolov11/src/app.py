# Run this script from the parent directory
# python ./src/inference_img.py


import numpy as np
from ultralytics import YOLO
from fast_serve import create_app
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Tuple, Union
from rpc import InferenceRequest, InferenceResponse
import convert

# Load model
model_path = "./data/yolo_model.pt"
model = YOLO(model_path)


# Add this middleware
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "null",  # Allow requests from file:// protocol
]


###### Helper Functions ######
# Convert the model inference results to a list of bounding boxes and a list of corresponding class names.
def to_lists(model_results, class_names) -> Tuple[List[str], List[str]]:
    bb, classes = [], []
    for result in model_results:
        for box in result.boxes:
            # get box coordinates in (left, top, right, bottom)
            bb.append(convert.boxToCoordinates(box))
            classes.append(class_names[int(box.cls)])
    return bb, classes


# Entry point
def inference(data: InferenceRequest) -> dict[str, Union[int, str]]:
    img = convert.base64ToNumpyArray(data.base64_img)
    results = model(img)
    bb, classes = to_lists(results, model.names)
    return {"bounding_boxes": bb, "classes": classes}


app = create_app(inference, response_model=InferenceResponse)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods, including OPTIONS
    allow_headers=["*"],  # Allow all headers
)
