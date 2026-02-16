
# 1. Base Image
FROM python:3.10-slim
# Says: "Start with official Python 3.10 slim image"
# "slim" = smaller size, just essentials

# 2. Set Working Directory
WORKDIR /app
# Says: "All commands run from /app directory"
# Like doing: cd /app

# 3. Copy Requirements First
COPY requirements.txt .
# Says: "Copy requirements.txt to current dir (/app)"
# We do this FIRST for Docker caching

# 4. Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Says: "Run pip install"
# --no-cache-dir = don't save cache (smaller image)

# 5. Copy Everything Else
COPY . .
# Says: "Copy all files (respecting .dockerignore) to /app"

# 6. Set Environment Variable
ENV PYTHONPATH=/app
# Says: "Set PYTHONPATH so Python finds our modules"

# 7. Default Command
CMD ["pytest", "-v"]
# Says: "When container starts, run: pytest -v"
# This is the default, can be overridden