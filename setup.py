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

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='venuspy',
    version='0.1.5',
    author="Alfredo Sequeida",
    description='A cross platform tool for setting a random wallpaper image from unsplash.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/AlfredoSequeida/venus',
    download_url='https://github.com/AlfredoSequeida/venus/archive/0.1.5.tar.gz',
    keywords ='wallpaper unsplash randomwallpaper',
    platforms ='any',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Topic :: Desktop Environment',
        ],
    license='MIT',
    packages=['venus'],
    scripts=[platform_file],
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    entry_points={'console_scripts': ['venus = venus.venus:main']},
)
