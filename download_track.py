import os
import sys  # Import sys module to access command line arguments
from pytube import YouTube

def download_track(url, save_path='./'):
    """
    Downloads a track from YouTube Music as an MP3 file.

    Args:
        url (str): The URL of the YouTube Music track to download.
        save_path (str): The directory to save the downloaded MP3 file.
    """
    try:
        # Create YouTube object with the URL
        yt = YouTube(url)

        # Select the audio stream with the highest quality
        audio_stream = yt.streams.get_audio_only()

        # Download the audio stream
        audio_stream.download(output_path=save_path, filename=yt.title + '.mp3')

        print(f"Downloaded '{yt.title}' successfully.")

    except Exception as e:
        print(f"Failed to download the track: {e}")

if __name__ == "__main__":
    # Check if a URL is passed as a command line argument
    if len(sys.argv) > 1:
        url = sys.argv[1]  # Use the URL passed as command line argument
    else:
        # Only prompt for input if no URL is provided as a command line argument
        url = input("Enter the YouTube Music track URL: ")
    download_track(url)
