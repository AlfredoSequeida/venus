import ctypes
import json
import subprocess
import sys
from typing import Protocol

import dbus


class System(Protocol):
    def set_wall(picture_file: str, use_pywal: bool) -> None:
        """This method sets a wallpaper.

        :param picture_file: The file to use for setting the background
        :param use_pywal: boolean determing whether pywal should be used. Requires pywal installed. Only available for Linux
        """
        ...

    @property
    def get_screen_resolution() -> str:
        """This method gets the screen resolution using system specific tools

        :return: screen resolution in string format
        """
        ...


class Darwin:
    def set_wall(picture_file, use_pywal):

        SCRIPT = """/usr/bin/osascript<<END
        tell application "Finder"
        set desktop picture to POSIX file "%s"
        end tell"""

        subprocess.Popen(SCRIPT % picture_file, shell=True)

    def get_screen_resolution():

        output = subprocess.Popen(
            "system_profiler SPDisplaysDataType |grep Resolution",
            shell=True,
            stdout=subprocess.PIPE,
        ).communicate()[0]

        resolution = (
            str(output)
            .replace("Resolution", " ")
            .replace("\\n'", "")
            .replace(":", "")
            .replace("b'", "")
            .split()
        )
        return resolution[0] + resolution[1] + resolution[2]


class Linux:
    def set_wall(picture_file, use_pywal):
        silent = dict(stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if use_pywal:
            try:
                wal = subprocess.call(["wal", "-i", picture_file, "-q"], **silent)
            except:
                pass

        # implementation for desktop environments and window mannagers using feh for
        # wallpaper management for example: i3 or openbox
        try:
            feh = subprocess.call(["feh", "--bg-fill", picture_file], **silent)
        except:
            pass

        # gsettings set org.gnome.desktop.background picture-uri 'file:///home/JohnDoe/Pictures/cool_wallpaper.jpg'
        # implementation for gnome desktops such as: ubuntu or gnome
        try:
            command = subprocess.call(
                [
                    "gsettings",
                    "set",
                    "org.gnome.desktop.background",
                    "picture-uri",
                    "file://" + picture_file,
                ],
                **silent
            )
        except:
            pass

        # kde
        try:
            plugin = "org.kde.image"

            jscript = """
            var allDesktops = desktops();
            print (allDesktops);
            for (i=0;i<allDesktops.length;i++) {
                d = allDesktops[i];
                d.wallpaperPlugin = "%s";
                d.currentConfigGroup = Array("Wallpaper", "%s", "General");
                d.writeConfig("Image", "file://%s")
            }
            """
            bus = dbus.SessionBus()
            plasma = dbus.Interface(
                bus.get_object("org.kde.plasmashell", "/PlasmaShell"),
                dbus_interface="org.kde.PlasmaShell",
            )
            plasma.evaluateScript(jscript % (plugin, plugin, picture_file))

        except:
            pass

        # sway
        try:
            swaymsg = subprocess.call(
                ["swaymsg", 'output * bg "{f}" fill'.format(f=picture_file)], **silent
            )
        except:
            pass

    def get_screen_resolution():
        # note, we are using xrandr to get the screen resolution instead of using
        # something like tkinter or wxpython, which provides a cross platform
        # solution to avoid the need for dependencies.

        # xrandr | grep \* | cut -d' ' -f4
        try:
            output = subprocess.Popen(
                "xrandr  | grep \* | cut -d' ' -f4",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
            ).communicate()[0]
            resolution = str(output.split()[0]).replace("b'", "").replace("'", "")
            return resolution
        except:
            pass

        output = subprocess.Popen(
            "swaymsg -t get_outputs",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        ).communicate()[0]
        tmp = json.loads(output)[0]["current_mode"]

        resolution = "{w}x{h}".format(w=tmp["width"], h=tmp["height"])

        return resolution


class Windows:
    def set_wall(picture_file, use_pywal):
        if use_pywal:
            try:
                wal = subprocess.call(["wal", "-i", picture_file, "-q"])
            except:
                pass

        # variables for system parameter info for setting the wallaper.

        SPI = 20
        SPIF = 2

        ctypes.windll.user32.SystemParametersInfoW(SPI, 0, picture_file, SPIF)

    def get_screen_resolution():
        """
        This method gets the screen resolution using the win32 video controller
        """
        output = subprocess.Popen(
            "wmic path Win32_VideoController get CurrentHorizontalResolution, CurrentVerticalResolution",
            shell=True,
            stdout=subprocess.PIPE,
        ).communicate()[0]

        # cleaning up output
        resolution = (
            str(output)
            .replace("CurrentHorizontalResolution", "")
            .replace("CurrentVerticalResolution", "")
            .replace("b'", "")
            .replace("\\n", " ")
            .replace("\\r", " ")
            .split()
        )

        # formationg resolution
        resolution = resolution[0] + "x" + resolution[1]

        return resolution


def get_system() -> System:
    if sys.platform == "darwin":
        return Darwin()
    if sys.platform == "linux":
        return Linux()
    if sys.platform == "win32":
        return Windows()
