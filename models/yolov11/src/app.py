# Run this script from the parent directory
# python ./src/inference_img.py


from rpc import InferenceRequest, InferenceResponse, Coordinate
import convert

from typing import List, Tuple, Union

from fast_serve import create_app
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import numpy as np
from ultralytics import YOLO

# Load model
model_path = "./data/yolo_model.pt"
model = YOLO(model_path)
model_labels = [name for _, name in model.names.items()]

# Add this middleware
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "null",  # Allow requests from file:// protocol
]


###### Helper Functions ######
# Convert the model inference results to a list of bounding boxes and a list of corresponding class names.
def to_lists(
    model_results, class_names
) -> Tuple[List[List[Coordinate]], List[List[str]]]:
    all_bb, all_classes = [], []
    for result in model_results:
        bb, classes = [], []
        for box in result.boxes:
            # get box coordinates in (left, top, right, bottom)
            bb.append(convert.boxToCoordinates(box))
            classes.append(class_names[int(box.cls)])
        all_bb.append(bb)
        all_classes.append(classes)
    return all_bb, all_classes


# Inference entry point
def inference(data: InferenceRequest) -> dict[str, Union[int, str]]:
    imgs = convert.base64ListToNumpyArrayList(data.base64_imgs)
    results = model(imgs)
    bb, classes = to_lists(results, model.names)

    model_info = model.info(detailed=False, verbose=True)
    model_layers = model_info[0] if model_info and len(model_info) > 1 else None
    model_parameters = model_info[1] if model_info and len(model_info) > 1 else None

    return {
        "bounding_boxes": bb,
        "classes": classes,
        "model_info": {
            "labels": model_labels,
            "layers": model_layers,
            "parameters": model_parameters,
        },
    }


app = create_app(inference, response_model=InferenceResponse)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods, including OPTIONS
    allow_headers=["*"],  # Allow all headers
)
