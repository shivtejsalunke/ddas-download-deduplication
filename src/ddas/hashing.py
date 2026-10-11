from pathlib import Path
import hashlib

def sha256_file(path, chunk_size=1024*1024):
    p=Path(path); before=p.stat(); h=hashlib.sha256()
    with p.open('rb') as f:
        while True:
            chunk=f.read(chunk_size)
            if not chunk: break
            h.update(chunk)
    after=p.stat()
    if (before.st_size,before.st_mtime_ns)!=(after.st_size,after.st_mtime_ns): raise RuntimeError('file changed during hashing')
    return {'sha256':h.hexdigest(),'size':after.st_size}
