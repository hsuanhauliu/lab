# ML Server Setup

This setup requires Nvidia GPU, so the driver and CUDA need to be installed already.

Everything can be brought up by ```docker compose up -d```, and turn down by ```docker compose down```.


1. Use `create_dirs.sh` to create all volumes the containers will be using.
2. ```docker compose up -d``` to bring up all containers.