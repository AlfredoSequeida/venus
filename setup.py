from setuptools import setup, find_packages
import os
import sys

platform = sys.platform

platform_file = ''

if 'linux' in platform:
    platform_file = 'venus/os_tools/linux.py' 
elif 'win32' in platform:
    platform_file = 'venus/os_tools/windows.py' 
elif 'darwin' in platform:
    platform_file = 'venus/os_tools/darwin.py' 


setup(
    name='venuspy',
    version='0.1.1',
    author="Alfredo Sequeida",
    description='A cross platform tool for setting a random wallpaper image from unsplash.com',
    url='https://github.com/AlfredoSequeida/venus',
    download_url='https://github.com/AlfredoSequeida/venus/archive/0.1.1.tar.gz',
    license='MIT',
    packages=['venus'],
    scripts=[platform_file],
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    entry_points={'console_scripts': ['venus = venus.venus:main']},
)
