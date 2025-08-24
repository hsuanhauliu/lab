# Jupyter notebook container needs to be running first.
docker exec -d -it jupyter_env tensorboard --logdir notebooks/logs --bind_all
