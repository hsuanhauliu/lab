# See the Docker file here:
# https://github.com/iot-salzburg/gpu-jupyter/blob/master/.build/Dockerfile
#
# All available images:
# https://hub.docker.com/r/cschranz/gpu-jupyter/tags
FROM cschranz/gpu-jupyter:v1.9_cuda-12.6_ubuntu-24.04

# Update Jupyter notebook version and install extensions & their dependencies
#   - https://jupyterlab-contrib.github.io/migrate_from_classical.html
RUN pip install --no-cache-dir jupyter==1.1.1 jupyterlab==4.4.9 \
	jupyterlab-code-formatter==3.0.2 isort==6.1.0 black==25.9.0 

# Install custom packages:
# 1. computer vision/image processing packages
# 2. audio processing packages
# 3. useful hugging-face packages
RUN pip install --no-cache-dir \
	opencv-python==4.12.0.88 opencv-contrib-python==4.12.0.88 invisible-watermark==0.2.0 \
	soundfile==0.13.1 librosa==0.11.0 \
	diffusers==0.35.1 accelerate==1.10.1 transformers==4.57.0 huggingface_hub==0.35.3

# Some other useful ML packages
RUN pip install --no-cache-dir torchview==0.2.7 \
	lightning==2.5.5 onnxruntime-gpu==1.23.0

# Jupyter lab user settings
# See https://jupyterlab.readthedocs.io/en/latest/user/directories.html#settings
COPY overrides.json /opt/conda/share/jupyter/lab/settings/overrides.json

