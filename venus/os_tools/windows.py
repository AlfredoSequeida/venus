import ctypes
import subprocess


def set_wall(picture_file, use_pywal):
    """This method sets a wallpaper.

    :param picture_file: The file to use for setting the background
    :param use_pywal: boolean determining whether pywal should be used
    :return: None
    """

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
    """returns the current system's screen resolution

    :return: string containing the screen resolution
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
