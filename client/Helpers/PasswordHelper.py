from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64

def encode(password: str) -> str:
    key = password.encode()
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256, length=16, salt=b'\xa0\x11\xdd\x91e\x1d\x8e\xe8\xd4vq%9\xb2\xf2\x94', iterations=10000)
    key = base64.urlsafe_b64encode(kdf.derive(key))
    return str(key)