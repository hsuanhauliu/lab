# Jupyter Notebook

Docker service for my ML experiments. Jupyter notebook + Tensorboard.

```bash
# start containers
# add --build to force build the Docker images
JUPYTER_TOKEN='yourpassword' docker compose up -d

# tear down the containers
docker compose down
```

Ports:

- 8888: Notebook port.
- 6006: Tensorboard port.

Files:

- `jupyter_notebook/Dockerfile`: added some additional packages on top of the gpu-jupyter Dockerfile.
- `start_env.sh`: start the original jupyter notebook container.
- `stop_env.sh`: stop the original jupyter notebook container.
- `get_urls.sh`: get URL and the token of the notebook.
- `start_tensorboard.sh`: run if you want to start a global tensorboard instance.

## Notes

### Tensorboard

When starting tensorboard in the Docker environment, make sure to bind to 0.0.0.0 and expose port.

```python
%load_ext tensorboard
%tensorboard --logdir logs --port 6006 --bind_all
```
