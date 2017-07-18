
from distutils.core import setup

setup(
    name ='watcherpy',
    version ='0.1.0',
    description ='Simple CLI tool to watch and eload html files on change.',
    author ='John Morrison',
    author_email ='john@johmorrison.io',
    packages = ["watcherpy"],
    entry_points = {"console_scripts" : ["watcher = watcherpy.__main__:main"]}
)
