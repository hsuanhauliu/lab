# Jupyter notebook container needs to be running first.
# This will start a tensorboard that's not tied to any kernel.
# Default port is 6006
docker exec -d -it jupyter_env tensorboard --logdir logs --bind_all
