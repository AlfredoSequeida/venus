import glob
import os
import sys
import tempfile
import time
from configparser import ConfigParser

import requests

import os_tools


def get_url(collection_id: str, resolution: str, search_term: str) -> str:
    """
    This method returns unsplash url based on user settings.
    If  a collection id is provided, it will return images within a given collection that fit the user monitor resolution.
    Otherwise, it will return random images from Unsplash that match any search criteria provided.

    :param collection_id: string containing unsplash collection id.
    :param resolution: string containg monitor resolution.
    :param search_term: string containing search parameters.
    :return: unsplash url in string format.
    """
    if not collection_id:
        return f"https://source.unsplash.com/{resolution}/?{search_term}"

    return f"https://source.unsplash.com/collection/{collection_id}/{resolution}"


def get_wall(base_url: str, output_path: str) -> str:
    """
    This method downloads a random  wallpaper to use from unsplash. The file is
    saved to a temporary file so it can be taken care of by the operating
    system.

    :param resolution: the resolution to use for retrieving the wallpaper the
                        default resolution is 1920x1080
    :return: the picture file retrieved
    """

    fd, picture_file = tempfile.mkstemp(suffix=".jpg", prefix="venus_", dir=output_path)

    # downloading the image to the system
    r = requests.get(base_url)
    with os.fdopen(fd, "wb") as f:
        f.write(r.content)

    return picture_file


def get_config() -> ConfigParser:
    """
    This method gets the configuration for venus

    :return - the config file
    """

    config = ConfigParser()
    config.read(os.path.join(os.path.expanduser("~"), ".config/venus/config"))
    return config


def get_sytem():
    if sys.platform == "linux":
        return os_tools.linux
    if sys.platform == "win32":
        return os_tools.windows
    if sys.platform == "darwin":
        return os_tools.darwin


def main():

    # checking platform for using system specific code
    system = get_sytem()

    # getting config
    config = get_config()

    # parse config
    screen_resolution_config = config.get(
        "SETTINGS", "SCREEN_RESOLUTION", fallback=None
    )
    output_path_config = config.get("SETTINGS", "OUTPUT_PATH", fallback=None)
    cache_items_config = config.get("SETTINGS", "CACHE_ITEMS", fallback=None)
    wait_time_config = config.get("SETTINGS", "WAIT_TIME", fallback=None)
    use_pywal_config = config.getboolean("SETTINGS", "USE_PYWAL", fallback=False)
    collection_id_config = config.get("SETTINGS", "COLLECTION_ID", fallback=None)

    search_terms_config = (
        config.get("SETTINGS", "SEARCH_TERMS", fallback=None)
        if len(sys.argv) == 1
        else sys.argv[1:]
    )

    # default path for empty OUTPUT_PATH setting
    if not output_path_config:
        output_path_config = None

    # default to system screen resolution for empty SCREEN_RESOLUTION setting
    if not screen_resolution_config:
        screen_resolution_config = system.get_screen_resolution()

    base_url_config = get_url(
        collection_id=collection_id_config,
        resolution=screen_resolution_config,
        search_terms=search_terms_config,
    )

    # loop control var
    run = True

    while run:

        system.set_wall(
            get_wall(
                base_url=base_url_config,
                output_path=output_path_config,
            ),
            use_pywal_config,
        )
        if cache_items_config and output_path_config:
            cacheFiles = glob.glob(output_path_config + "/*")
            cacheFiles.sort(key=os.path.getmtime, reverse=True)
            if len(cacheFiles) >= int(cache_items_config):
                for i, file in enumerate(cacheFiles):
                    if i >= int(cache_items_config):
                        os.remove(file)

        if not wait_time_config:
            run = False
        else:
            time.sleep(int(wait_time_config))


if __name__ == "__main__":
    # main()
    config = get_config()
    print(config)
