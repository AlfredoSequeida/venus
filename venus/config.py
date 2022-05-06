import os
import sys
from configparser import ConfigParser
from dataclasses import dataclass

from system import System


@dataclass
class VenusConfig:
    """Venus Config Class with parsed attributes from the config file"""

    system: System

    def __post_init__(self):
        self._path = os.path.join(os.path.expanduser("~"), ".config/venus/config")
        self._config = ConfigParser()
        self._config.read(self._path)

    @property
    def screen_resolution(self) -> str:
        """wallpaper screen resolution

        :return: string with the desired screen resolution
        """
        screen_resolution = self._config.get(
            "SETTINGS", "SCREEN_RESOLUTION", fallback=None
        )
        return screen_resolution if screen_resolution else self.system.screen_resolution

    @property
    def output_path(self) -> str:
        """cache directory for storing downloaded images

        :return: string with the directory path
        """
        output_path = self._config.get("SETTINGS", "OUTPUT_PATH", fallback=None)
        return output_path if output_path else None

    @property
    def cache_items(self) -> int:
        """maximum number of allowed cached items

        :return: integer representing the maximum number of allowed cached items
        """
        cache_items = self._config.get("SETTINGS", "CACHE_ITEMS", fallback=0)
        return int(cache_items) if cache_items else 0

    @property
    def wait_time(self) -> int:
        """time in seconds before next wallpaper change

        :return: integer representing the number of seconds before next wallpaper change
        """
        wait_time = self._config.get("SETTINGS", "WAIT_TIME", fallback=0)
        return int(wait_time) if wait_time else 0

    @property
    def use_pywal(self) -> bool:
        """Flag determining the integration with pywal. Pywal must be installed in the system.

        :return: boolean on whether pywal should be called with each wallpaper change
        """
        return self._config.getboolean("SETTINGS", "USE_PYWAL", fallback=False)

    @property
    def collection_id(self) -> str:
        """Unsplash Collection Id to be searched

        :return: string representing an unsplash collection id
        """
        collection_id = self._config.get("SETTINGS", "COLLECTION_ID", fallback=None)
        return collection_id if collection_id else None

    @property
    def search_terms(self) -> str:
        """Terms to be used when seartching unsplash for Pictures. Overrided by colleciton_id.

        :return: string with the search terms
        """
        if len(sys.argv) == 1:
            search_terms = self._config.get("SETTINGS", "SEARCH_TERMS", fallback=None)
        else:
            search_terms = ",".join(sys.argv[1:])
        return search_terms if search_terms else None
