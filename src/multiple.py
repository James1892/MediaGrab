from src.defaultLocation import DefaultLocation
from src.clearScreen import ScreenCleaner
from rich import print
import subprocess
import os

def downloadMultiple(mainMenu):
    ScreenCleaner.clearScreen()
    print("""[cyan]

░░░░░░   ░░░░░  ░░░░░░░░  ░░░░░░ ░░   ░░     ░░░░░░   ░░░░░░  ░░     ░░ ░░░    ░░ ░░       ░░░░░░   ░░░░░  ░░░░░░  
▒▒   ▒▒ ▒▒   ▒▒    ▒▒    ▒▒      ▒▒   ▒▒     ▒▒   ▒▒ ▒▒    ▒▒ ▒▒     ▒▒ ▒▒▒▒   ▒▒ ▒▒      ▒▒    ▒▒ ▒▒   ▒▒ ▒▒   ▒▒ 
▒▒▒▒▒▒  ▒▒▒▒▒▒▒    ▒▒    ▒▒      ▒▒▒▒▒▒▒     ▒▒   ▒▒ ▒▒    ▒▒ ▒▒  ▒  ▒▒ ▒▒ ▒▒  ▒▒ ▒▒      ▒▒    ▒▒ ▒▒▒▒▒▒▒ ▒▒   ▒▒ 
▓▓   ▓▓ ▓▓   ▓▓    ▓▓    ▓▓      ▓▓   ▓▓     ▓▓   ▓▓ ▓▓    ▓▓ ▓▓ ▓▓▓ ▓▓ ▓▓  ▓▓ ▓▓ ▓▓      ▓▓    ▓▓ ▓▓   ▓▓ ▓▓   ▓▓ 
██████  ██   ██    ██     ██████ ██   ██     ██████   ██████   ███ ███  ██   ████ ███████  ██████  ██   ██ ██████  

[/cyan]""")

    urls = []
    while True:
        url = input("Enter YouTube URL (or type 'done' to finish):\n>> ").strip()
        if url.lower() == "done":
            break
        if url:
            urls.append(url)

    if not urls:
        print("[bold red]No URLs provided[/bold red]")
        input("Press Enter to continue...")
        mainMenu()
        return

    while True:
        print("\nChoose a format")
        print("1) Audio")
        print("2) Video")
        option = input(">> ").strip()
        if option == "1":
            downloadMultipleAudio(urls, mainMenu)
            break
        elif option == "2":
            downloadMultipleVideos(urls, mainMenu)
            break
        else:
            print("[bold red]Invalid option[/bold red]\n")


def downloadMultipleAudio(urls, mainMenu):
    location = input(f"Save to directory [Default: {DefaultLocation.getDefaultSaveLocation()}]\n>> ").strip()
    if not location:
        location = DefaultLocation.getDefaultSaveLocation()
    while not os.path.exists(location):
        print(f"[bold red]{location} does not exist[/bold red]\n")
        location = input("Enter a valid directory path:\n>> ").strip()

    yt_cmd = "yt-dlp.exe" if os.name == "nt" else "yt-dlp"

    for url in urls:
        print(f"[bold cyan]Processing:[/bold cyan] {url}")
        try:
            # Download audio and convert to MP3
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
            print(f"[bold green]Downloaded successfully[/bold green]\n")
        except subprocess.CalledProcessError:
            print(f"[bold red]Failed to download: {url}[/bold red]\n")
        except Exception as e:
            print(f"[bold red]Unexpected error: {e}[/bold red]\n")

    input("Press Enter to continue...")
    mainMenu()


def downloadMultipleVideos(urls, mainMenu):
    location = input(f"Save to directory [Default: {DefaultLocation.getDefaultSaveLocation()}]\n>> ").strip()
    if not location:
        location = DefaultLocation.getDefaultSaveLocation()
    while not os.path.exists(location):
        print(f"[bold red]{location} does not exist[/bold red]\n")
        location = input("Enter a valid directory path:\n>> ").strip()

    yt_cmd = "yt-dlp.exe" if os.name == "nt" else "yt-dlp"

    for url in urls:
        print(f"[bold cyan]Processing:[/bold cyan] {url}")
        try:
            # Download best video + audio
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
            print(f"[bold green]Downloaded successfully[/bold green]\n")
        except subprocess.CalledProcessError:
            print(f"[bold red]Failed to download: {url}[/bold red]\n")
        except Exception as e:
            print(f"[bold red]Unexpected error: {e}[/bold red]\n")

    input("Press Enter to continue...")
    mainMenu()
