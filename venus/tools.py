import glob
import os
import tempfile

import requests
from PIL import Image

from config import VenusConfig


def get_url(config: VenusConfig) -> str:
    """
    This method returns unsplash url based on user settings.
    If  a collection id is provided, it will return images within a given collection that fit the user monitor resolution.
    Otherwise, it will return random images from Unsplash that match any search criteria provided.

    :param config: VenusConfig class containing parameters from the config file.
    :return: unsplash url in string format.
    """
    if not config.collection_id:
        return f"https://source.unsplash.com/{config.resolution}/?{config.search_term}"

    return f"https://source.unsplash.com/collection/{config.collection_id}/{config.screen_resolution}"


def get_wall(base_url: str, output_path: str) -> str:
    """
    This method downloads a random  wallpaper to use from unsplash. The file is
    saved to a temporary file so it can be taken care of by the operating
    system.

    :param resolution: resolution to use for retrieving wallpapers. The default resolution the screen resolution.
    :return: the picture file retrieved
    """

    fd, picture_file = tempfile.mkstemp(suffix=".jpg", prefix="venus_", dir=output_path)

    # downloading the image to the system
    r = requests.get(base_url)
    with os.fdopen(fd, "wb") as f:
        f.write(r.content)

    return picture_file


def is_jpg(filename: str) -> bool:
    try:
        i = Image.open(filename)
        return i.format == "JPEG"
    except IOError:
        return False


def update_cached_items(max_cached_items: int, cache_dir: str) -> None:
    """removes older wallpapers, keeping only the newest items up to the maximum number of cached items set by config file.

    :param max_cached_items: maximum number of allowed wallpapers in the cached directory
    :param cache_dir: cache directory path
    """

    cached_files = glob.glob(cache_dir + "/*")
    cached_files.sort(key=os.path.getmtime, reverse=True)

    if len(cached_files) <= int(max_cached_items):
        return

    [os.remove(file) for file in cached_files[max_cached_items:]]
