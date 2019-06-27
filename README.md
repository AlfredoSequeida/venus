Venus: For those that get bored of looking at their wallpaper 
===============================================================

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)


<p align="center">
    <img src="https://github.com/AlfredoSequeida/venus/raw/master/artwork/venus.png" alt="venus">
    </br>
    </br>
    <img src="https://github.com/AlfredoSequeida/venus/raw/master/artwork/venus_demo.gif" alt="">
</p>

Venus aims to be a cross-platform tool to automatically change your desktop wallpaper using images from [Unsplash](https://unsplash.com/). All images are stored in the system's temporary directory, this way their disposal is handled by the operating system. 


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
            

 
 Current Verion 0.1.4 - verified working on
 -----------------
 - [x] Arch Linux [Feh 2.28]
 - [x] Ubuntu 18.04.1 LTS [Gnome 3.28]
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

