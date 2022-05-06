import time

from config import VenusConfig
from system import get_system
from tools import get_url, get_wall, is_jpg, update_cached_items


def main():

    # check user platform for using system specific code
    user_system = get_system()

    # getting config
    config = VenusConfig(user_system)

    # get unsplash url from config
    unsplash_url = get_url(config)

    # main loop
    while True:

        # get wallpaper
        wallpaper = get_wall(unsplash_url, config.output_path)

        # verify image integrity
        if not is_jpg(wallpaper):
            continue

        # set wallpaper
        user_system.set_wall(wallpaper, config.use_pywal)

        # update cached wallpapers
        if config.cache_items and config.output_path:
            update_cached_items(config.cache_items, config.output_path)

        # wait for next change
        if not config.wait_time:
            break

        time.sleep(config.wait_time)


if __name__ == "__main__":
    main()
