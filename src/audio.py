from src.defaultLocation import DefaultLocation
from src.clearScreen import ScreenCleaner
from rich import print
import subprocess
import os


def audioDownload(mainMenu):
    ScreenCleaner.clearScreen()
    print("""[dark_magenta]
 █████╗ ██╗   ██╗██████╗ ██╗ ██████╗ 
██╔══██╗██║   ██║██╔══██╗██║██╔═══██╗
███████║██║   ██║██║  ██║██║██║   ██║
██╔══██║██║   ██║██║  ██║██║██║   ██║
██║  ██║╚██████╔╝██████╔╝██║╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝
[/dark_magenta]""")

    while True:
        url = input("Enter YouTube video URL\n>> ").strip()

        location = input(
            f"Save to directory [Default: {DefaultLocation.getDefaultSaveLocation()}]\n>> "
        ).strip()

        if location == "":
            location = DefaultLocation.getDefaultSaveLocation()

        if not os.path.exists(location):
            print(f"[bold red]{location} does not exist[/bold red]\n")
            continue

        output_template = os.path.join(location, "%(title)s.%(ext)s")

        command = [
            "yt-dlp",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "--restrict-filenames",  # avoids illegal characters in filenames
            "--quiet",               # suppress most yt-dlp messages
            "--no-warnings",         # suppress warnings
            "-o", output_template,
            url
        ]

        try:
            subprocess.run(command, check=True)
            print("[bold green]Audio downloaded successfully[/bold green]\n")
        except subprocess.CalledProcessError:
            print("[bold red]Download failed — invalid URL or network issue[/bold red]\n")

        input("Press Enter to continue...")
        mainMenu()
