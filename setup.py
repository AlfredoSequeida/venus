from setuptools import setup, find_packages
import codecs
import re
import os

with open('README.md', 'r') as fh:
    long_description = fh.read()

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

dynamic_version = find_version('venus', '__init__.py')

setup(
    name='venuspy',
    version=dynamic_version,
    author="Alfredo Sequeida",
    description='A cross platform tool for setting a random wallpaper image from unsplash.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/AlfredoSequeida/venus',
    download_url='https://github.com/AlfredoSequeida/venus/archive/' + dynamic_version + '.tar.gz',
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
    scripts=[
        'venus/os_tools/linux.py',
        'venus/os_tools/darwin.py',
        'venus/os_tools/windows.py',
        ],
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    entry_points={'console_scripts': ['venus = venus.venus:main']},
)
