from setuptools import setup, find_packages

setup(
    name="MediaGrab",                     # Project name
    version="1.5.0",
    description="Cross-platform audio/video downloader from multiple sites, including YouTube playlists",
    packages=find_packages(where="src"),  # Look for modules in src/
    package_dir={"": "src"},             # src/ is the root of your packages
    install_requires=[
        "yt-dlp",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "mediagrab=src.main:main"   # Run program with `mediagrab` command
        ]
    },
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Internet :: WWW/HTTP"
    ]
)
