# YouTube MP3 Downloader

A simple CLI script to download YouTube videos as MP3 audio files.

## Prerequisites

- Python 3.6 or higher
- yt-dlp package

## Installation

1. Clone this repository or download the script files.

2. Install the required dependencies:

```bash
pip install yt-dlp
```

## Usage

### Download a single YouTube video as MP3

```bash
python youtube_mp3_downloader.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Download multiple YouTube videos from a file

Create a text file with one YouTube URL per line, then run:

```bash
python youtube_mp3_downloader.py -f youtube_urls.txt
```

### Specify a custom output directory

By default, MP3 files are saved to a directory named "mp3". You can specify a different directory:

```bash
python youtube_mp3_downloader.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o "my_music"
```

## Options

- `-u, --url`: Single YouTube URL to download
- `-f, --file`: File containing YouTube URLs (one per line)
- `-o, --output-dir`: Output directory for MP3 files (default: 'mp3')
- `-h, --help`: Show help message

## Example

1. Create a file named `youtube_urls.txt` with multiple YouTube URLs:

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=jNQXAC9IVRw
https://www.youtube.com/watch?v=9bZkp7q19f0
```

2. Run the script to download all videos as MP3:

```bash
python youtube_mp3_downloader.py -f youtube_urls.txt
```

3. The MP3 files will be saved in the "mp3" directory.
