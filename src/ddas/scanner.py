from pathlib import Path
from .hashing import sha256_file

def scan_directory(root,store,partial_suffixes=('.part','.crdownload','.tmp')):
    scanned=[]
    for p in Path(root).rglob('*'):
        if not p.is_file() or p.name.endswith(partial_suffixes): continue
        try: info=sha256_file(p)
        except (OSError,RuntimeError): continue
        st=p.stat(); store.upsert(p,info['sha256'],info['size'],st.st_mtime_ns); scanned.append({'path':str(p),'sha256':info['sha256'],'size':info['size']})
    return {'scanned':scanned,'duplicates':store.duplicates()}
