import sys
from dataclasses import dataclass


@dataclass
class System:
    """System Class.

    :param set_wall: system-specific function to set a new wallpaper.
    :param get_screen_resolution: system-specific function to get the screen resolution.
    """

    set_wall: callable
    get_screen_resolution: callable

    @property
    def screen_resolution(self) -> str:
        return self.get_screen_resolution()


def get_system() -> System:
    """Returns a system class with system-specific tools for setting wallpapers and fetching the screen resolution.

    :return: System class
    """
    if sys.platform == "darwin":
        from os_tools import darwin

        set_wall_func = darwin.set_wall
        get_screen_res_func = darwin.get_screen_resolution

    if sys.platform == "linux":
        from os_tools import linux

        set_wall_func = linux.set_wall
        get_screen_res_func = linux.get_screen_resolution

    if sys.platform == "win32":
        from os_tools import windows

        set_wall_func = windows.set_wall
        get_screen_res_func = windows.get_screen_resolution

    return System(set_wall_func, get_screen_res_func)
