import asyncio
from pathlib import Path

import music_tag
from shazamio import Shazam

MUSIC_FOLDER = Path("/home/kiarash/Music/Telegram")

AUDIO_EXTENSIONS = {
    ".mp3",
    ".flac",
    ".wav",
    ".m4a",
    ".ogg",
    ".opus",
    ".aac",
    ".wma",
}


def get_audio_files(folder: Path) -> list[Path]:
    audio_files = []

    for file in folder.glob("*"):
        if file.is_file() and file.suffix.lower() in AUDIO_EXTENSIONS:
            audio_files.append(file)

    return audio_files


def get_album(track: dict) -> str:
    for section in track["sections"]:
        if section["type"] == "SONG":
            for item in section["metadata"]:
                if item["title"] == "Album":
                    return item["text"]
    return "Single Release"


def save_metadata(file: Path, title: str, artist: str, album: str):
    music_file = music_tag.load_file(file)

    music_file["tracktitle"] = title
    music_file["artist"] = artist
    music_file["album"] = album

    music_file.save()


async def main():
    audio_files = get_audio_files(MUSIC_FOLDER)
    shazam = Shazam(segment_duration_seconds=10)
    print(f"Found {len(audio_files)} audio files.")

    for index, file in enumerate(audio_files, start=1):
        print(f"[{index}/{len(audio_files)}] {file.name}")

        try:
            result = await shazam.recognize(file)
            track = result["track"]

            track_title = track["title"]
            track_artist = track["subtitle"]
            track_album = get_album(track)

            save_metadata(file, track_title, track_artist, track_album)

            print(f"    Album: {track_album}")
            print(f"    Artist: {track_artist}")
            print(f"    Title: {track_title}")
            print(f"    Metadata Saved.")

        except Exception as e:
            print(f"    Error: {e}")


asyncio.run(main())
