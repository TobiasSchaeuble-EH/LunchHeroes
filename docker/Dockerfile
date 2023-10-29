# --- Backend Build Stage ---
FROM python:3.9-slim as backend

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the Poetry configuration and lock files
COPY backend/pyproject.toml backend/poetry.lock /app/

# Install dependencies without creating a virtual environment
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the backend source code into the image
COPY backend /app/

# --- Frontend Build Stage ---
FROM node:14 as frontend

WORKDIR /app

# Copy the frontend package configuration files
COPY frontend/package*.json /app/

# Install dependencies
RUN npm install

# Copy the frontend source code into the image
COPY frontend /app/

# Build the frontend
RUN npm run build

# --- Nginx Stage ---
FROM nginx:alpine

# Copy the built frontend files to the Nginx server
COPY --from=frontend /app/build /usr/share/nginx/html

# Copy the backend app to a directory served by Gunicorn
COPY --from=backend /app /app

# Set up Gunicorn to serve the backend app
COPY docker/gunicorn.conf /etc/gunicorn/gunicorn.conf

# Set up Nginx to proxy requests to Gunicorn
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

# Expose the necessary ports
EXPOSE 80

# Start Gunicorn and Nginx
CMD ["sh", "-c", "gunicorn -c /etc/gunicorn/gunicorn.conf app:app & nginx -g 'daemon off;'"]