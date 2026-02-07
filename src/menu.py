from src.multiple import downloadMultiple
from src.playlist import downloadPlaylist 
from src.defaultLocation import DefaultLocation
from src.clearScreen import ScreenCleaner
from src.audio import audioDownload
from src.video import videoDownload
from rich import print
import sys

CONFIG_FILE = "config.txt"  # Path to the configuration file

def mainMenu():
    ScreenCleaner.clearScreen()
    while True:
        print("""[red]
██╗   ██╗████████╗███╗   ███╗███████╗██████╗ ██╗ █████╗  ██████╗ ██████╗  █████╗ ██████╗ 
╚██╗ ██╔╝╚══██╔══╝████╗ ████║██╔════╝██╔══██╗██║██╔══██╗██╔════╝ ██╔══██╗██╔══██╗██╔══██╗
 ╚████╔╝    ██║   ██╔████╔██║█████╗  ██║  ██║██║███████║██║  ███╗██████╔╝███████║██████╔╝
  ╚██╔╝     ██║   ██║╚██╔╝██║██╔══╝  ██║  ██║██║██╔══██║██║   ██║██╔══██╗██╔══██║██╔══██╗
   ██║      ██║   ██║ ╚═╝ ██║███████╗██████╔╝██║██║  ██║╚██████╔╝██║  ██║██║  ██║██████╔╝
   ╚═╝      ╚═╝   ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
       
   [/red][white]v1.5""")

        print("""======================================================================
        options:
                    1) Audio
                    2) Video
                    3) Download Multiple URLs
                    4) Download A playlist
                    5) Set Default Save Location
                    99) Exit
======================================================================""")

        option = input(">> ")
        if option == "1":
            audioDownload(mainMenu)
        elif option == "2":
            videoDownload(mainMenu)
        elif option == "3":
            downloadMultiple(mainMenu)
        elif option == "4":
            downloadPlaylist(mainMenu)
        elif option == "5":
            DefaultLocation.setDefaultSaveLocation()
        elif option == "99":
            sys.exit()

