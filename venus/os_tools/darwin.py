import subprocess


def set_wall(picture_file: str, use_pywal: bool) -> None:
    """This method sets a wallpaper.

    :param picture_file: The file to use for setting the background
    :param use_pywal: boolean determining whether pywal should be used
    :return: None
    """

    silent = dict(stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if use_pywal:
        try:
            wal = subprocess.call(["wal", "-i", picture_file, "-q"], **silent)
        except:
            pass

    SCRIPT = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "%s"
    end tell"""

    subprocess.Popen(SCRIPT % picture_file, shell=True)


def get_screen_resolution() -> str:
    """returns the current system's screen resolution

    :return: string containing the screen resolution
    """

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
