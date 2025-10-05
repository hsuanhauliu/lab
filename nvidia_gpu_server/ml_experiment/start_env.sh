# Command to start the jupyter notebook environment
# - ./data dir is mapped to the base directory Jupyter is using
docker run --gpus all -d -it -p 8888:8888 -p 8889:6006 -v ~/data/gpu-jupyter:/home/jovyan -e GRANT_SUDO=yes -e JUPYTER_ENABLE_LAB=yes --user root --name jupyter_env cschranz/gpu-jupyter:v1.5_cuda-11.6_ubuntu-20.04
