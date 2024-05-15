# Use Python 3.8 as the base image
FROM python:3.8

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Copy the application code into the Docker image
COPY . /app

# Set the working directory to /downloads
WORKDIR /downloads

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Set the entry point to run the download_track.py script
ENTRYPOINT ["python", "/app/download_track.py"]
