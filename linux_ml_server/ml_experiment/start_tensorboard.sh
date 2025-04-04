# Jupyter notebook container needs to be running first.
docker exec -d -it jupyter_env tensorboard --logdir logs --bind_all
