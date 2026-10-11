import pytest
from ddas.hashing import sha256_file
from ddas.store import FileStore
from ddas.scanner import scan_directory
from ddas.metadata_crypto import encrypt_metadata,decrypt_metadata

def test_hash_and_duplicate_scan(tmp_path):
 root=tmp_path/'files'; root.mkdir(); (root/'a').write_bytes(b'same'); (root/'b').write_bytes(b'same'); (root/'partial.part').write_bytes(b'same')
 store=FileStore(tmp_path/'idx.db'); result=scan_directory(root,store)
 assert len(result['scanned'])==2 and len(result['duplicates'])==1
 assert sha256_file(root/'a')['sha256']==sha256_file(root/'b')['sha256']
def test_metadata_encryption():
 key=b'k'*32; value={'files':['a','b']}; assert decrypt_metadata(encrypt_metadata(value,key),key)==value
 with pytest.raises(Exception): decrypt_metadata(encrypt_metadata(value,key),b'x'*32)
