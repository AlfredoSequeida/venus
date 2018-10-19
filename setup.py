from setuptools import setup, find_packages


setup(
    name='venus',
    version='0.0.1',
    author="Alfredo Sequeida",
    description="A cross platform tool for setting a random wallpaper image from unsplash.com",
    license="MIT",
    packages=['venus',],
    #packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={"console_scripts": ["venus = venus.venus:main"]},
)
