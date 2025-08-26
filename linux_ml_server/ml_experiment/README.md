# ML Notebook

Docker services for ML & CV experiment. Jupyter notebook + Tensorboard.

```bash
./create_dirs.sh
docker compose up -d
# set a token via env var
# JUPYTER_TOKEN='yourpassword' docker compose up -d
./get_urls.sh           # get URL of the notebook with token
./start_tensorboard.sh  # optional: run if you need tensorboard
docker compose down
```

Ports:

- 8888: Notebook port.
- 8889: Tensorboard port.

Directories inside the Jupyter notebook environment:

- `notebooks`: directories for all notebooks.
- `notebooks/data`: dataset directory.
- `notebooks/test`: test data.
- `notebooks/output`: generated files.
- `logs`: Tensorboard log folder for model training.

Files:

- `jupyter_notebook/Dockerfile`: added some additional packages on top of the gpu-jupyter Dockerfile.
- `start_env.sh`: start the original jupyter notebook container.
- `stop_env.sh`: stop the original jupyter notebook container.
