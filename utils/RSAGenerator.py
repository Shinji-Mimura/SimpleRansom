import rsa


class RSAGen():
    def __init__(self) -> None:
        self.keys = []

    def createfiles() -> None:

        (pubkey, privkey) = rsa.newkeys(2048)

        publickey = open("./keys/public.pem", "wb")
        publickey.write(pubkey.save_pkcs1("PEM"))
        publickey.close()

        privatekey = open("./keys/private.pem", "wb")
        privatekey.write(privkey.save_pkcs1("PEM"))
        privatekey.close()
