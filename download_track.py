import os
import sys  # Import sys module to access command line arguments
from pytube import YouTube, Playlist

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

def download_playlist(url, save_path='./'):
    """
    Downloads all tracks from a YouTube Music playlist as MP3 files.

    Args:
        url (str): The URL of the YouTube Music playlist to download.
        save_path (str): The directory to save the downloaded MP3 files.
    """
    try:
        # Create Playlist object with the URL
        playlist = Playlist(url)

        # Iterate over all video URLs in the playlist
        for video_url in playlist.video_urls:
            # Download each track using the existing function
            download_track(video_url, save_path)

        print(f"Downloaded all tracks from playlist successfully.")

    except Exception as e:
        print(f"Failed to download the playlist: {e}")

if __name__ == "__main__":
    # Check if a URL is passed as a command line argument
    if len(sys.argv) > 2:
        url = sys.argv[2]  # Use the URL passed as command line argument
        mode = sys.argv[1]  # Determine mode (track or playlist)

        if mode == "track":
            download_track(url)
        elif mode == "playlist":
            download_playlist(url)
        else:
            print("Invalid mode. Use 'track' or 'playlist'.")
    else:
        # Only prompt for input if no URL is provided as a command line argument
        mode = input("Enter mode (track/playlist): ")
        url = input("Enter the YouTube Music URL: ")
        if mode == "track":
            download_track(url)
        elif mode == "playlist":
            download_playlist(url)
        else:
            print("Invalid mode. Use 'track' or 'playlist'.")
