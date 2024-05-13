# extract-mp3

This repository now includes a Python script named `download_track.py` that allows users to download tracks from Youtube Music as MP4 files and then converts them to MP3 files using `pydub`.

## Requirements

To run the `download_track.py` script, you will need:
- Python 3.6 or newer
- Install the required libraries using `pip install -r requirements.txt`. This will install:
  - `pytube` library version 10.0.0 or newer for playlist functionality
  - `pydub` library
- `ffmpeg` installed for handling audio conversions. `ffmpeg` is not a Python package and needs to be installed separately. You can install it using your system's package manager or download it from [FFmpeg's official website](https://ffmpeg.org/download.html)

## Usage

To download a track from Youtube Music, you can either run the script with the track's URL as an argument or enter the URL after the script starts:

```
python download_track.py track <YouTube Music track URL>
```

Or, if you do not provide the URL as an argument, the script will prompt you to enter it:

```
python download_track.py
```

For example, to download a specific track by providing the URL as an argument:

```
python download_track.py track https://www.youtube.com/watch?v=EXAMPLE
```

And if you run the script without an argument, it will ask:

```
Enter the YouTube Music track URL:
```

This will download the specified track as an MP4 file and then convert it to an MP3 file using `pydub`, saving it to the current directory.

## Downloading a Playlist

To download an entire playlist from Youtube Music, use the `playlist` mode followed by the playlist's URL:

```
python download_track.py playlist <YouTube Music playlist URL>
```

For example, to download a whole playlist:

```
python download_track.py playlist https://www.youtube.com/playlist?list=EXAMPLE
```

This will download all tracks in the specified playlist as MP4 files and then convert them to MP3 files using `pydub`, saving them to the current directory.

## Troubleshooting

If you encounter an error stating "Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work", it indicates that `ffmpeg` is not properly installed or configured. Ensure that `ffmpeg` is installed on your system and that its binaries are in your system's PATH. For detailed installation instructions, refer to the [FFmpeg's official website](https://ffmpeg.org/download.html).
