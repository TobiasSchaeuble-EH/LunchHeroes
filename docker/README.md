# LunchHeroes Docker Configuration

This Docker setup is designed to build the Docker image for the LunchHeroes application, which can then be pushed to a Docker registry and deployed on a server.


## Preliminary Steps

1. **Building the Docker Image**
    To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:
    ```bash
    docker push lucca93/lunchheroes:latest
    ```

2. **Pushing Docker Image:**
   - After building the Docker image, push it to your Docker registry using the following command:
     ```bash
     docker push lucca93/lunchheroes:latest
     ```


**Server Hosting:**
   - The server is hosted on [Flow Swiss](https://my.flow.swiss/).

## File Descriptions

### Dockerfile

The Dockerfile orchestrates the build process for both the frontend and backend of the LunchHeroes application. Here's a brief overview of each stage in the Dockerfile:

- **Backend Build Stage:**
  - Uses the `python:3.9-slim` base image.
  - Installs Poetry for dependency management.
  - Copies and installs the backend dependencies using Poetry.
  - Installs Gunicorn as the WSGI HTTP server to serve the backend application.
  - Copies the backend source code into the image.

- **Frontend Build Stage:**
  - Uses the `node:14` base image.
  - Copies and installs the frontend dependencies using npm.
  - Copies the frontend source code into the image.
  - Builds the frontend assets.

- **Nginx Stage:**
  - Uses the `nginx:alpine` base image.
  - Copies the built frontend files to the Nginx server.
  - Copies the backend app to a directory served by Gunicorn.
  - Sets up Gunicorn to serve the backend app.
  - Sets up Nginx to proxy requests to Gunicorn for the `/api` endpoint.
  - Exposes port 80.
  - Starts Gunicorn and Nginx.

### gunicorn.conf

This file contains the Gunicorn configuration. Gunicorn is set up to bind to `0.0.0.0:8000` and uses 3 worker processes.

### nginx.conf

This file contains the Nginx configuration. Nginx is set up to serve the static frontend files and to proxy requests to the `/api` endpoint to Gunicorn.


