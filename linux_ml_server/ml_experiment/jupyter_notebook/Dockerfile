# See the Docker file here:
# https://github.com/iot-salzburg/gpu-jupyter/blob/master/.build/Dockerfile
#
# All available images:
# https://hub.docker.com/r/cschranz/gpu-jupyter/tags
FROM cschranz/gpu-jupyter:v1.9_cuda-12.6_ubuntu-24.04

# Install custom packages
RUN pip install opencv-python opencv-contrib-python \
	transformers huggingface_hub \
	onnxruntime-gpu \
	soundfile librosa 

# Download Jupyter notebook extensions
# https://jupyterlab-contrib.github.io/migrate_from_classical.html
RUN pip install isort black jupyterlab-code-formatter \
	jupyterlab-notifications
