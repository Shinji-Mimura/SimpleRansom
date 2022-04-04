import random
import string


class AESGenerator():
    def __init__(self) -> None:
        self.key32 = ""

    def aes_key_generator(self) -> str:
        for _ in range(32):
            self.key32 += random.choice(string.ascii_letters[0:52])

        return self.key32
