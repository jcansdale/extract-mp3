# extract-mp3

This repository now includes a Python script named `download_track.py` that allows users to download tracks from Youtube Music as MP3 files.

## Requirements

To run the `download_track.py` script, you will need:
- Python 3.6 or newer
- `pytube` library installed (you can install it using `pip install pytube`)

## Usage

To download a track from Youtube Music, simply run the script with the track's URL as an argument:

```
python download_track.py <YouTube Music track URL>
```

For example:

```
python download_track.py https://www.youtube.com/watch?v=EXAMPLE
```

This will download the specified track as an MP3 file to the current directory.
