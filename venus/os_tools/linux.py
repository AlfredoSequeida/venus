import subprocess
import dbus
import json


def set_wall(picture_file, use_pywal):
    """
    This method sets a wallpaper
    :param picture_file - The file to use for setting the background
    """
    silent = dict(stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if use_pywal:
        try:
            wal = subprocess.call(["wal", "-i", picture_file, "-q"], **silent)
        except:
            pass

    # implementation for desktop envirorments and window mannagers using feh      for
    # wallpaper management for example:
    # i3
    # openbox
    try:
        feh = subprocess.call(["feh", "--bg-fill", picture_file], **silent)
    except:
        pass

    # gsettings set org.gnome.desktop.background picture-uri 'file:///home/Jo     hnDoe/Pictures/cool_wallpaper.jpg'
    # implementation for gnome desktops such as:
    # ubuntu
    # gnome
    try:
        command = subprocess.call(
            ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "file://" + picture_file], **silent)
    except:
        pass

    # kde
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
        plasma = dbus.Interface(bus.get_object(
            'org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
        plasma.evaluateScript(jscript % (plugin, plugin, picture_file))

    except:
        pass

    # sway
    try:
        swaymsg = subprocess.call(["swaymsg", "output * bg \"{f}\" fill".format(f=picture_file)], **silent)
    except:
        pass


def get_screen_resolution():
    """
    This method gets the screen resolution using xrandr
    """
    # note, we are using xrandr to get the screen resolution instead of usin     g
    # something like tkinter or wxpython, which provides a cross platform
    # solution to avoid the need for dependecies.

    # xrandr | grep \* | cut -d' ' -f4
    try:
        output = subprocess.Popen("xrandr  | grep \* | cut -d' ' -f4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).communicate()[0]
        resolution = str(output.split()[0]).replace("b'", '').replace("'", '')
        return resolution
    except:
        pass

    output = subprocess.Popen("swaymsg -t get_outputs", shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).communicate()[0]
    tmp = json.loads(output)[0]['current_mode']

    resolution = "{w}x{h}".format(w=tmp['width'], h=tmp['height'])

    return resolution
