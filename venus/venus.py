import sys                                                                  
import requests
import tempfile

def get_wall(resolution="1920x1080"):
    """
    This method downloads a random  wallpaper to use from unsplash. The file is 
    saved to a temporary file so it can be taken care of by the operating 
    system.

    :param resolution - the resolution to use for retrieving the wallpaper the  
                        default resolution is 1920x1080
    :return - the picture file retrieved
    """

    base_url = 'https://source.unsplash.com/random/' + resolution
    r = requests.get(base_url)

    _, picture_file = tempfile.mkstemp(suffix=".jpg", prefix="venus_")

    with open(picture_file, 'wb') as f:
        #downloading the image to the system
        f.write(r.content)

    return picture_file

def main():
    #checking platform for applying the wallpaper
    platform = sys.platform

    if 'linux' in platform:
        from venus.os_tools import linux
        linux.set_wall(get_wall(resolution=linux.get_screen_resolution()))

    elif 'win32' in platform:
        #from venus.os_tools import windows 
        #temporary fix for development until a windows package is made
        from os_tools import windows 
        windows.set_wall(get_wall(resolution=windows.get_screen_resolution()))

    elif 'darwin' in platform:
        from venus.os_tools import darwin 
        darwin.set_wall(get_wall(resolution=darwin.get_screen_resolution()))

if __name__ == "__main__":
    main()

