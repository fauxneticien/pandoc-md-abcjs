FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    pandoc \
    entr \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Taskfile (go-task)
RUN curl -sSL https://taskfile.dev/install.sh | sh -s -- -d -b /usr/local/bin

# Install Python dependencies
RUN pip install --no-cache-dir livereload

WORKDIR /app

EXPOSE 8000 35729

CMD ["task", "serve"]
