import sys
from dataclasses import dataclass


@dataclass
class System:
    set_wall: callable
    get_screen_resolution: callable


def get_system() -> System:
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
