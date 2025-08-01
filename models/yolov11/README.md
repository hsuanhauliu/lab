# YOLOv11

Inference service serving Ultralytics' [YOLOv11](https://docs.ultralytics.com/models/yolo11/) model built with Docker.

## Build

```bash
docker build -t yolov11 .
```

## Run

Use the provided script to download YOLOv11. Modify the URL in the script if you want to use different yolo models.

```bash
./get_model.sh
```

Command to run the image:

```bash
docker run -v ./data:/app/data yolov11
```

## Dev

Create local environment.

```bash
python3.13 -m venv venv2
source venv2/bin/activate
pip install opencv-python-headless ultralytics
```
