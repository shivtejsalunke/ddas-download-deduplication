import json, os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_metadata(metadata, key):
    if len(key)!=32: raise ValueError('key must be 32 bytes')
    nonce=os.urandom(12); return nonce+AESGCM(key).encrypt(nonce,json.dumps(metadata,sort_keys=True).encode(),None)
def decrypt_metadata(blob, key):
    if len(key)!=32 or len(blob)<28: raise ValueError('invalid key or metadata envelope')
    return json.loads(AESGCM(key).decrypt(blob[:12],blob[12:],None).decode())
