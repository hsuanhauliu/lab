# YOLOv11

Inference service serving Ultralytics' [YOLOv11](https://docs.ultralytics.com/models/yolo11/) model built with Docker.

## Run

Use the provided script to download YOLOv11. Modify the URL in the script if you want to use different yolo models.

```bash
./get_model.sh
```

Command to run the Docker image:

```bash
# Build the image. Needs to be in the current directory.
docker build -t yolov11 .

# Frontend client will be running on http://localhost:8080.
docker run --rm -v ./data:/app/data --name yolov11 -p 8080:5000 yolov11
```
