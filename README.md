# LUDA

The Levelling Up Data API.

LUDA provides a structured view to all metrics under the 12 Levelling Up missions in the form

```bash
category > variable > metric
```

## Installation

### Local

Get started by creating a virtual environment using `poetry` and install the dependencies with

```bash
poetry install
```

Start the development server with

```bash
poetry run uvicorn app.main:app --reload --host localhost --port 8000
```

### Docker

Build the image with

```bash
docker build -t luda .
```

You can stop the build at specific stages with the `--target` option:

```bash
docker build -t poetry-project --target [development | lint | test | production] .
```

Access `poetry`'s shell within the container with

```bash
docker run -it luda bash
```

Start the production server with

```bash
docker run -it -p 8000:8000 luda
```

### Docker Compose

Build and start the development server with

```bash
docker-compose up --build -d
```
