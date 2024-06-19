import os
import sys  # Import sys module to access command line arguments
from pytube import YouTube, Playlist
from pydub import AudioSegment  # Import AudioSegment from pydub
from pydub.exceptions import CouldntDecodeError

def sanitize_filename(filename):
    """
    Sanitizes filenames by removing or replacing illegal characters.

    Args:
        filename (str): The filename to sanitize.

    Returns:
        str: The sanitized filename.
    """
    illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in illegal_chars:
        filename = filename.replace(char, '')
    return filename

def download_track(url, save_path='./'):
    """
    Downloads a track from YouTube Music as an MP4 file and converts it to MP3.

    Args:
        url (str): The URL of the YouTube Music track to download.
        save_path (str): The directory to save the downloaded MP3 file.

    Returns:
        str: The path of the downloaded MP3 file.
    """
    try:
        # Create YouTube object with the URL
        yt = YouTube(url)

        # Select the audio stream with the highest quality
        audio_stream = yt.streams.get_audio_only()

        # Sanitize the title to use as filename
        sanitized_title = sanitize_filename(yt.title)

        # Download the audio stream as MP4
        mp4_filename = sanitized_title + '.mp4'
        audio_stream.download(output_path=save_path, filename=mp4_filename)

        # Convert MP4 to MP3 using pydub
        mp3_filename = sanitized_title + '.mp3'
        mp3_path = os.path.join(save_path, mp3_filename)
        AudioSegment.from_file(os.path.join(save_path, mp4_filename)).export(mp3_path, format="mp3")

        # Delete the original MP4 file
        os.remove(os.path.join(save_path, mp4_filename))

        print(f"Downloaded and converted '{sanitized_title}' successfully. MP3 saved at: {mp3_path}")

        return os.path.abspath(mp3_path)

    except CouldntDecodeError:
        print("Failed to convert the track. Please ensure ffmpeg/ffprobe is installed and available in your PATH.")
    except Exception as e:
        print(f"Failed to download and convert the track: {e}")

def download_playlist(url, save_path='./'):
    """
    Downloads all tracks from a YouTube Music playlist as MP4 files and converts them to MP3.

    Args:
        url (str): The URL of the YouTube Music playlist to download.
        save_path (str): The directory to save the downloaded MP3 files.
    """
    try:
        # Create Playlist object with the URL
        playlist = Playlist(url)

        # Iterate over all video URLs in the playlist
        for video_url in playlist.video_urls:
            # Download and convert each track using the existing function
            download_track(video_url, save_path)

        print(f"Downloaded and converted all tracks from playlist successfully.")

    except CouldntDecodeError:
        print("Failed to convert one or more tracks in the playlist. Please ensure ffmpeg/ffprobe is installed and available in your PATH.")
    except Exception as e:
        print(f"Failed to download and convert the playlist: {e}")

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
