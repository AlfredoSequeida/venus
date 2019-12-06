Venus: For those that get bored of looking at their wallpaper 
===============================================================

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Downloads](https://pepy.tech/badge/venuspy)](https://pepy.tech/project/venuspy)


<p align="center">
    <img src="https://imgur.com/W1E85ZK.png" alt="venus">
    </br>
    </br>
    <img src="https://imgur.com/ZdNOhIo.gif" alt="">
</p>

Venus aims to be a cross-platform tool to automatically change your desktop wallpaper using images from [Unsplash](https://unsplash.com/). By default, all images are stored in the system's temporary directory, this way their disposal is handled by the operating system. 


Venus also handles using images that work with your resolution.

---

Note for the adventurous -> set venus as a startup program. This way you can see what awaits you with each reboot :)

# Installation
1) Install using pip3 

Linux/OSX

```
pip3 install venuspy 
```

Windows 

```
py -m pip install venuspy 
```


# Usage
1) Just type venus!
 
Linux/OSX

```
venus 
```

Windows 

```
py -m venus 
```

# Config
Venus can be configured for specific search terms to get a category of images.

Edit the config file located in:

```
~.config/venus/config
```

By default, the search terms are empty, which means the image selection will be random. To choose what kind of images you want, enter search terms separated by commas.

Here is an example:

```
SEARCH_TERMS = landscape,nature,car
```

By default all images are stored as temporary files in the temp directory of the operating system. To change the location where the images are stored, edit the OUTPUT_PATH option.


Here is an example:

```
OUTPUT_PATH = /home/user/Pictures
```

Venus has the option of using a timer to change your wallpaper given an interval in seconds.

Here is an example that changes the wallpaper every 60 seconds (1 minute):

```
WAIT_TIME = 60
```

By default a image is requested with the resoluton of your screen. If you need to change that for any reason (if your screen resolution is not available by Unsplash and you are getting a 404 image as your wallpaper), edit the SCREEN_RESOLUTION option. Here is an example:

```
SCREEN_RESOLUTION = 1920x1080
```

Venus supports using [pywal](https://github.com/dylanaraps/pywal) as an addon.
To use pywal first [install it](https://github.com/dylanaraps/pywal/wiki/Installation), 
then enable it in the config file:

```
USE_PYWAL = True 
```


 Current Verion 1.0.1 - verified working on
 -----------------
 - [x] Feh 2.28
 - [x] Gnome 3.28
 - [x] KDE Plasma 5.15.4
 - [x] Sway 1.2 
 - [x] macOS High Sierra
 - [x] Windows 10

 
 
 How to Contribute
-----------------

1.  Check for open issues or open a fresh issue to start a discussion
    around a feature idea or a bug [here](https://github.com/AlfredoSequeida/venus/issues)
    tag for issues that should be ideal for people who are not very familiar with the codebase yet.
2.  Fork [the repository](https://github.com/alfredosequeida/venus) on
    GitHub to start making your changes to the **master** branch (or branch off of it).
3.  Write a test which shows that the bug was fixed or that the feature
    works as expected.
4.  Send a pull request and bug the maintainer until it gets merged and
    published. :) Make sure to add yourself to
    [AUTHORS](https://github.com/AlfredoSequeida/venus/blob/master/AUTHORS).

