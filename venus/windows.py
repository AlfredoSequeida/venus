import subprocess                                                           
import ctypes
import os
from ctypes import wintypes

def set_wall(picture_file):
    """
    This method sets a wallpaper
    :param picture_file - The file to use for setting the background
    """
    picture_file = os.path.basename(picture_file)
    print (picture_file)
    picture_file = "C:\\Users/PC/AppData/Local/Temp/" + picture_file 
    print (picture_file)
    picture_file= "C:\\Users/PC/AppData/Local/Temp/venus_tf20nufp.jpg"

    SPI_SETDESKWALLPAPER  = 0x0014
    SPIF_UPDATEINIFILE    = 0x0001
    SPIF_SENDWININICHANGE = 0x0002

    user32 = ctypes.WinDLL('user32')
    SystemParametersInfo = user32.SystemParametersInfoW
    SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint
    SystemParametersInfo.restype = wintypes.BOOL
    print(SystemParametersInfo(SPI_SETDESKWALLPAPER, 1, picture_file, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE))

def get_screen_resolution():
    """
    This method gets the screen resolution using xrandr
    """
    #wmic path Win32_VideoController get CurrentHorizontalResolution,CurrentVerticalResolution
    output = subprocess.Popen("wmic path Win32_VideoController get CurrentHorizontalResolution, CurrentVerticalResolution",shell=True     , stdout=subprocess.PIPE).communicate()[0]

    #cleaning up output 
    resolution = str(output).replace("CurrentHorizontalResolution", "").replace("CurrentVerticalResolution", "").replace("b'", "").replace("\\n" ," ").replace("\\r", " ").split() 

    #formationg resolution
    resolution = resolution[0] + "x" + resolution[1]

    return resolution
