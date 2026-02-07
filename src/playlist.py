from src.defaultLocation import DefaultLocation
from src.clearScreen import ScreenCleaner
from rich import print
import subprocess
import os

def downloadPlaylist(mainMenu):
    ScreenCleaner.clearScreen()

    print("""
▀██▀▀█▄  ▀██                    ▀██   ██           ▄   
 ██   ██  ██   ▄▄▄▄    ▄▄▄▄ ▄▄▄  ██  ▄▄▄   ▄▄▄▄  ▄██▄  
 ██▄▄▄█▀  ██  ▀▀ ▄██    ▀█▄  █   ██   ██  ██▄ ▀   ██   
 ██       ██  ▄█▀ ██     ▀█▄█    ██   ██  ▄ ▀█▄▄  ██   
▄██▄     ▄██▄ ▀█▄▄▀█▀     ▀█    ▄██▄ ▄██▄ █▀▄▄█▀  ▀█▄▀ 
                       ▄▄ █                            
                        ▀▀                             
""")

    yt_cmd = "yt-dlp.exe" if os.name == "nt" else "yt-dlp"

    while True:
        playlist_url = input("Enter YouTube playlist URL\n>> ").strip()
        if not playlist_url:
            continue

        # Get all video URLs in the playlist
        command_list = [yt_cmd, "--flat-playlist", "-J", playlist_url]
        try:
            result = subprocess.run(command_list, capture_output=True, text=True, check=True)
            import json
            data = json.loads(result.stdout)
            video_urls = [f"https://www.youtube.com/watch?v={v['id']}" for v in data.get('entries', [])]

            if not video_urls:
                print("[bold red]The URL does not contain any videos. Try again.[/bold red]")
                continue

        except subprocess.CalledProcessError:
            print("[bold red]Invalid playlist URL or network error[/bold red]")
            continue
        except Exception as e:
            print(f"[bold red]Unexpected error: {e}[/bold red]")
            continue

        break

    while True:
        print("\nChoose a format")
        print("1) Audio (MP3)")
        print("2) Video (MP4)")
        option = input(">> ").strip()
        if option == "1":
            downloadPlaylistAudio(video_urls, yt_cmd, mainMenu)
            break
        elif option == "2":
            downloadPlaylistVideo(video_urls, yt_cmd, mainMenu)
            break
        else:
            print("[bold red]Invalid option[/bold red]\n")


def downloadPlaylistAudio(urls, yt_cmd, mainMenu):
    location = input(f"Save to directory [Default: {DefaultLocation.getDefaultSaveLocation()}]\n>> ").strip()
    if not location:
        location = DefaultLocation.getDefaultSaveLocation()
    while not os.path.exists(location):
        print(f"[bold red]{location} does not exist[/bold red]\n")
        location = input("Enter a valid directory path:\n>> ").strip()

    for url in urls:
        print(f"[bold cyan]Downloading audio:[/bold cyan] {url}")
        try:
            command = [
                yt_cmd,
                "-f", "bestaudio",
                "--extract-audio",
                "--audio-format", "mp3",
                "--audio-quality", "0",
                "--restrict-filenames",
                "--quiet",
                "--no-warnings",
                "--progress-template", "Downloading: {progress}% ETA: {eta}s",
                "-o", os.path.join(location, "%(title)s.%(ext)s"),
                url
            ]

            subprocess.run(command, check=True)
            print(f"[bold green]Audio downloaded successfully[/bold green]\n")
        except subprocess.CalledProcessError:
            print(f"[bold red]Failed to download: {url}[/bold red]\n")
        except Exception as e:
            print(f"[bold red]Unexpected error: {e}[/bold red]\n")

    input("Press Enter to continue...")
    mainMenu()


def downloadPlaylistVideo(urls, yt_cmd, mainMenu):
    location = input(f"Save to directory [Default: {DefaultLocation.getDefaultSaveLocation()}]\n>> ").strip()
    if not location:
        location = DefaultLocation.getDefaultSaveLocation()
    while not os.path.exists(location):
        print(f"[bold red]{location} does not exist[/bold red]\n")
        location = input("Enter a valid directory path:\n>> ").strip()

    for url in urls:
        print(f"[bold cyan]Downloading video:[/bold cyan] {url}")
        try:
            command = [
                yt_cmd,
                "-f", "bestvideo+bestaudio/best",
                "--merge-output-format", "mp4",
                "--restrict-filenames",
                "--quiet",
                "--no-warnings",
                "--progress-template", "Downloading: {progress}% ETA: {eta}s",
                "-o", os.path.join(location, "%(title)s.%(ext)s"),
                url
            ]
            subprocess.run(command, check=True)
            print(f"[bold green]Video downloaded successfully[/bold green]\n")
        except subprocess.CalledProcessError:
            print(f"[bold red]Failed to download: {url}[/bold red]\n")
        except Exception as e:
            print(f"[bold red]Unexpected error: {e}[/bold red]\n")

    input("Press Enter to continue...")
    mainMenu()
