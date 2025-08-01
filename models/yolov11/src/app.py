# Run this script from the parent directory
# python ./src/inference_img.py


import numpy as np
from ultralytics import YOLO
from fast_serve import create_app
from typing import List, Tuple
from rpc import InferenceRequest, InferenceResponse

# Load model
model_path = "./data/yolo_model.pt"
model = YOLO(model_path)


###### Helper Functions ######
# Convert the model inference results to a list of bounding boxes and a list of corresponding class names.
def to_lists(yolo_results, class_names) -> Tuple[List[np.ndarray], List[str]]:
    bb, classes = [], []
    for box in yolo_results:
        bb.append(box.xyxy[0].numpy())
        classes.append(class_names[int(box.cls)])
    return bb, classes


# Entry point
def inference(data: InferenceRequest):
    results = model(data.image)
    bb, classes = to_lists(results, model.names)
    return {"bounding_boxes": bb, "classes": classes}


app = create_app(inference, response_model=InferenceResponse)
