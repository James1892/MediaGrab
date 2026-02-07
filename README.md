# MediaGrab - Video and MP3 Grabber

MediaGrab is a cross-platform Python application for downloading audio and video content from multiple websites, including YouTube, Twitch, and more. It supports single videos, multiple downloads, and full playlists.

## Screenshots

### Main Screen



### Audio Download



### Video Download



### Batch Download



### PlayList Download



### Configuration



## Installation

To use MediaGrab, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/James1892/MediaGrab.git
```
2. Navigate to the project directory:
```bash
cd MediaGrab
```
3. Install dependencies:

```bash
pip install -r requirements.txt
```

This installs the required Python packages: yt-dlp and rich.

4. Install FFmpeg (required for audio/video conversion):

- Windows: Download from ffmpeg.org and add to PATH

- macOS:
```bash
brew install ffmpeg
```
- Linux (Debian/Ubuntu):
```bash
sudo apt install ffmpeg
```

## Usage

1. Run the application:
```bash
python main.py
```

## Requirements
- Python 3.9+
- FFmpeg installed and accessible in PATH
- Python packages:
    - `yt-dlp`
    - `rich`
