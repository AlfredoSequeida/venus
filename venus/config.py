import os
import sys
from configparser import ConfigParser
from dataclasses import dataclass

from system import System


@dataclass
class VenusConfig:

    system: System

    def __post_init__(self):
        self._path = os.path.join(os.path.expanduser("~"), ".config/venus/config")
        self._config = ConfigParser()
        self._config.read(self._path)

    @property
    def screen_resolution(self) -> str:
        screen_resolution = self._config.get(
            "SETTINGS", "SCREEN_RESOLUTION", fallback=None
        )
        return (
            screen_resolution
            if screen_resolution
            else self.system.get_screen_resolution()
        )

    @property
    def output_path(self) -> str:
        output_path = self._config.get("SETTINGS", "OUTPUT_PATH", fallback=None)
        return output_path if output_path else None

    @property
    def cache_items(self) -> int:
        cache_items = int(self._config.get("SETTINGS", "CACHE_ITEMS", fallback=0))
        return cache_items if cache_items else 0

    @property
    def wait_time(self) -> int:
        wait_time = self._config.get("SETTINGS", "WAIT_TIME", fallback=0)
        return wait_time if wait_time else 0

    @property
    def use_pywal(self) -> bool:
        return self._config.getboolean("SETTINGS", "USE_PYWAL", fallback=False)

    @property
    def collection_id(self) -> str:
        collection_id = self._config.get("SETTINGS", "COLLECTION_ID", fallback=None)
        return collection_id if collection_id else None

    @property
    def search_terms(self) -> str:
        if len(sys.argv) == 1:
            search_terms = self._config.get("SETTINGS", "SEARCH_TERMS", fallback=None)
        else:
            search_terms = ",".join(sys.argv[1:])
        return search_terms if search_terms else None
