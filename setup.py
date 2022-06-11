from setuptools import setup
from os.path import exists
from hafez.about import __version__, __description__

if not exists("hafez/config.py"):
    print("\033[38;5;196m" + " ERROR:" + "\033[38;5;255m" +  " Please create your configs in hafez/config.py")

try:
    with open('README.md', 'r') as readme:
        longDescription = readme.read()
except:
    print("Can't read README.md")
    exit()

VERSION = __version__
DESCRIPTION = __description__

setup(
    name="Hafez",
    version=VERSION,
    description=__description__,
    long_description=longDescription,
    long_description_content_type="text/markdown",
    author="Seyed Hosein Mousavi Fard",
    author_mail="shmf1385@protonmail.com",
    url="https://github.com/hafez-notebook",
    keyword=["notebook", "note", "hafez", "fastapi",],
    packages = (
        "hafez",
        "hafez.apps",
        "hafez.models",
    ),
    install_requires = ["fastapi[all]"],
    include_package_data=True,
    license="GPL3.0",
    license_files=(
        "LICENSE"
    ),
    entry_points = {
        'console_scripts': [
            'hafez = hafez.__main__:run',
        ]
    },
    classfires = [
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: FastAPI',
        'Natural Language :: Persian',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ]
)
