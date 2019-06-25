import sys                                                                  
import requests
import tempfile
import os
import configparser

def get_wall(resolution="1920x1080", search_term=""):
    """
    This method downloads a random  wallpaper to use from unsplash. The file is 
    saved to a temporary file so it can be taken care of by the operating 
    system.

    :param resolution - the resolution to use for retrieving the wallpaper the  
                        default resolution is 1920x1080
    :return - the picture file retrieved
    """
    
    base_url = 'https://source.unsplash.com/' + resolution +'/?' + search_term

    r = requests.get(base_url)

    fd, picture_file = tempfile.mkstemp(suffix=".jpg", prefix="venus_")

    with os.fdopen(fd, 'wb') as f:

        #downloading the image to the system
        f.write(r.content)

    return picture_file

def get_config():
    """
    This method gets the configuration for venus

    :return - the config file
    """

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.expanduser('~'), '.config/venus/config'))

    return config

def main():
    #checking platform for applying the wallpaper
    platform = sys.platform

    #getting config
    config = get_config()
    
    search_term_config = config['SETTINGS']['SEARCH_TERMS']

    if 'linux' in platform:
        from venus.os_tools import linux
        linux.set_wall(get_wall(resolution=linux.get_screen_resolution(), 
            search_term=search_term_config))

    elif 'win32' in platform:
        from venus.os_tools import windows 
        windows.set_wall(get_wall(resolution=windows.get_screen_resolution(),
            search_term = search_term_config))

    elif 'darwin' in platform:
        from venus.os_tools import darwin 
        darwin.set_wall(get_wall(resolution=darwin.get_screen_resolution(),
            search_term = search_term_config))

if __name__ == "__main__":
    main()

