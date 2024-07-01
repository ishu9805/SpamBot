#RiZoeLXSpam By @TheRiZoeL

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from utils import load_plugins
import logging
from telethon import events
from __init__ import Riz

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "RiZoeLXSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("RiZoeL Bot Spam Successfully deployed -!")
print("Enjoy! Do visit @RiZoeLX")

if __name__ == "__main__":
    Riz.run_until_disconnected()
    
