from src.defaultLocation import DefaultLocation
from src.clearScreen import ScreenCleaner
from rich import print
import subprocess
import os

def videoDownload(mainMenu):
    ScreenCleaner.clearScreen()
    print("""[green_yellow]
 __     __ __       __                   
|  \   |  \  \     |  \                  
| ▓▓   | ▓▓\▓▓ ____| ▓▓ ______   ______  
| ▓▓   | ▓▓  \/      ▓▓/      \ /      \ 
 \▓▓\ /  ▓▓ ▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ 
  \▓▓\  ▓▓| ▓▓ ▓▓  | ▓▓ ▓▓    ▓▓ ▓▓  | ▓▓
   \▓▓ ▓▓ | ▓▓ ▓▓__| ▓▓ ▓▓▓▓▓▓▓▓ ▓▓__/ ▓▓
    \▓▓▓  | ▓▓\▓▓    ▓▓\▓▓    \ \▓▓    ▓▓
     \▓    \▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓  \▓▓▓▓▓▓ 
[/green_yellow]""")

    yt_cmd = "yt-dlp.exe" if os.name == "nt" else "yt-dlp"

    while True:
        url = input("Enter URL for the video you want to download \n>> ").strip()
        if not url:
            continue

        # Get video title first to handle filenames safely
        try:
            # Get video info without downloading
            command_info = [yt_cmd, "--get-title", url, "--quiet"]
            result = subprocess.run(command_info, capture_output=True, text=True, check=True)
            video_title = result.stdout.strip()
            print(f"[italic orange3]{video_title}[/italic orange3]")
        except subprocess.CalledProcessError:
            print(f"[bold red]Invalid URL or video not available: {url}[/bold red]\n")
            continue
        except Exception as e:
            print(f"[bold red]Unexpected error: {e}[/bold red]\n")
            continue

        # Choose save directory
        while True:
            location = input(f"Save to directory [Default: {DefaultLocation.getDefaultSaveLocation()}]\n>> ").strip()
            if not location:
                location = DefaultLocation.getDefaultSaveLocation()
            if not os.path.exists(location):
                print(f"[bold red]{location} does not exist[/bold red]\n")
                continue
            break

        # Handle filename conflicts
        file_path = os.path.join(location, video_title + ".mp4")
        if os.path.exists(file_path):
            print("[bold yellow]A file with the same name already exists. What do you want to do?[/bold yellow]")
            print("1) Replace the existing file")
            print("2) Rename the file")
            choice = input(">> ").strip()
            if choice == "1":
                os.remove(file_path)
                print(f"[bold green]{video_title} replaced successfully[/bold green]\n")
            elif choice == "2":
                while True:
                    new_file_name = input("Enter a new name for the file: ").strip()
                    new_file_path = os.path.join(location, new_file_name + ".mp4")
                    if not os.path.exists(new_file_path):
                        file_path = new_file_path
                        print(f"[bold green]{video_title} renamed successfully to {new_file_name}[/bold green]\n")
                        break
                    else:
                        print("[bold red]File already exists, choose another name[/bold red]")
            else:
                print("[bold red]Invalid choice[/bold red]\n")
                continue

        # Download the video
        print(f"[bold cyan]Downloading {video_title}...[/bold cyan]")
        command_download = [
            yt_cmd,
            "-f", "bestvideo+bestaudio/best",
            "--merge-output-format", "mp4",
            "--restrict-filenames",
            "--quiet",
            "--no-warnings",
            "-o", file_path,
            url
        ]
        try:
            subprocess.run(command_download, check=True)
            print(f"[bold green]{video_title} downloaded successfully[/bold green]\n")
        except subprocess.CalledProcessError:
            print(f"[bold red]Failed to download: {video_title}[/bold red]\n")
        except Exception as e:
            print(f"[bold red]Unexpected error: {e}[/bold red]\n")

        input("Press Enter to continue...")
        mainMenu()
