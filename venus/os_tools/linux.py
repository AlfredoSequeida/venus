import subprocess                                                           
import dbus

def set_wall(picture_file):
    """
    This method sets a wallpaper
    :param picture_file - The file to use for setting the background
    """
    #implementation for desktop envirorments and window mannagers using feh      for 
    #wallpaper management for example: 
    #i3 
    #openbox
    try:
        feh = subprocess.call(["feh", "--bg-fill", picture_file])
    except:
        pass

    #gsettings set org.gnome.desktop.background picture-uri 'file:///home/Jo     hnDoe/Pictures/cool_wallpaper.jpg'
    #implementation for gnome desktops such as:
    #ubuntu
    #gnome
    try:
        command = subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "file://" + picture_file])
    except:
        pass

    #kde
    try:
        plugin = 'org.kde.image'

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
        plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
        plasma.evaluateScript(jscript % (plugin, plugin, picture_file))

    except:
        pass


def get_screen_resolution():
    """
    This method gets the screen resolution using xrandr
    """
    # note, we are using xrandr to get the screen resolution instead of usin     g   
    # something like tkinter or wxpython, which provides a cross platform
    # solution to avoid the need for dependecies.

    #xrandr | grep \* | cut -d' ' -f4

    output = subprocess.Popen("xrandr  | grep \* | cut -d' ' -f4",shell=True     , stdout=subprocess.PIPE).communicate()[0]
    resolution = str(output.split()[0]).replace("b'", '').replace("'", '')
    return resolution
