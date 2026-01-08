# Start with Python 3.11 Slim
FROM python:3.12-slim

# Set working directory to /app
WORKDIR /app

# Install System Dependencies
# - build-essential/gcc: for compiling some python libs
# - portaudio19-dev: for PyAudio
# - libgl1/libglib2.0: for OpenCV (cv2)
# - wget/gnupg: utilities
RUN apt-get update && apt-get install -y \
    build-essential \
    portaudio19-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Copy Requirements
COPY requirements.txt .

# Install Python Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright Browsers (for Web Agent)
RUN pip install playwright
RUN playwright install chromium --with-deps

# Copy Backend Code
COPY backend/ ./backend/
# Copy optional project files
COPY settings.json .

# Expose the API Port
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the server
CMD ["python", "backend/server.py"]
