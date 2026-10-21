import asyncio
from pathlib import Path

import aiohttp
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


async def download_artwork(session, artwork_url: str) -> bytes:
    async with session.get(artwork_url) as response:
        response.raise_for_status()
        return await response.read()


def save_metadata(
    file: Path,
    title: str,
    artist: str,
    album: str,
    artwork: bytes,
):
    music_file = music_tag.load_file(file)

    music_file["tracktitle"] = title
    music_file["artist"] = artist
    music_file["album"] = album
    music_file["artwork"] = artwork

    music_file.save()


async def main():
    audio_files = get_audio_files(MUSIC_FOLDER)

    shazam = Shazam(segment_duration_seconds=10)

    not_recognized = []

    print(f"Found {len(audio_files)} audio files.")

    async with aiohttp.ClientSession() as session:

        for index, file in enumerate(audio_files, start=1):
            print(f"[{index}/{len(audio_files)}] {file.name}")

            try:
                result = await shazam.recognize(file)

                if "track" not in result:
                    print("    Shazam could not recognize this file.")
                    not_recognized.append(file.name)
                    continue

                track = result["track"]

                track_title = track["title"]
                track_artist = track["subtitle"]
                track_album = get_album(track)
                artwork_url = track["images"]["coverart"]

                artwork = await download_artwork(
                    session,
                    artwork_url,
                )

                save_metadata(
                    file,
                    track_title,
                    track_artist,
                    track_album,
                    artwork,
                )

                print(f"    Album: {track_album}")
                print(f"    Artist: {track_artist}")
                print(f"    Title: {track_title}")
                print("    Artwork: Updated")
                print("    Metadata: Saved")

            except Exception as e:
                print(f"    Error: {e}")
                not_recognized.append(file.name)

    print()
    print("==============================")
    print("Finished")
    print("==============================")

    print(f"Total files: {len(audio_files)}")
    print(f"Could not recognize: {len(not_recognized)}")

    if not_recognized:
        print()
        print("Files Shazam could not recognize:")

        for file_name in not_recognized:
            print(f"    {file_name}")


asyncio.run(main())
