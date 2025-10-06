# See the Docker file here:
# https://github.com/iot-salzburg/gpu-jupyter/blob/master/.build/Dockerfile
#
# All available images:
# https://hub.docker.com/r/cschranz/gpu-jupyter/tags
FROM cschranz/gpu-jupyter:v1.9_cuda-12.6_ubuntu-24.04

# Install custom packages:
# 1. computer vision/image processing packages
# 2. audio processing packages
# 3. useful hugging-face packages
# 4. onnx runtime package
RUN pip install --no-cache-dir \
	opencv-python opencv-contrib-python invisible-watermark \
	soundfile librosa \
	diffusers transformers huggingface_hub \
	onnxruntime-gpu

# Download Jupyter notebook extensions
# https://jupyterlab-contrib.github.io/migrate_from_classical.html
RUN pip install --no-cache-dir isort black jupyterlab-code-formatter
