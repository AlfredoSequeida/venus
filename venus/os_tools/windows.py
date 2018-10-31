import subprocess                                                           
import ctypes
import os

def set_wall(picture_file):
    """
    This method sets a wallpaper
    :param picture_file - The file to use for setting the background
    """

    SPI = 20
    SPIF = 2

    #path = "C:\\Users\\PC\\AppData\\Local\\Temp\\" + "venus__4787_tj.jpg" 
    #print ('-> ' + path)
    path = "C:\\Users\\PC\\AppData\\Local\\Temp\\" + os.path.basename(picture_file) 
    print ('-> ' + path)
    ctypes.windll.user32.SystemParametersInfoW(SPI, 0, path, SPIF)


    #The bellow statement works
    #ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users/PC/AppData/Local/Temp/venus_cv531apn.jpg", 0)


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
