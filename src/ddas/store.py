import sqlite3
from pathlib import Path

class FileStore:
    def __init__(self,db_path):
        self.db_path=str(db_path)
        with self.connect() as c:
            c.execute('CREATE TABLE IF NOT EXISTS files(path TEXT PRIMARY KEY, sha256 TEXT NOT NULL, size INTEGER NOT NULL, mtime_ns INTEGER NOT NULL)')
    def connect(self): return sqlite3.connect(self.db_path)
    def upsert(self,path,sha256,size,mtime_ns):
        with self.connect() as c:
            c.execute('INSERT INTO files VALUES(?,?,?,?) ON CONFLICT(path) DO UPDATE SET sha256=excluded.sha256,size=excluded.size,mtime_ns=excluded.mtime_ns',(str(Path(path).resolve()),sha256,size,mtime_ns))
    def duplicates(self):
        with self.connect() as c:
            rows=c.execute('SELECT sha256,GROUP_CONCAT(path),COUNT(*) FROM files GROUP BY sha256 HAVING COUNT(*)>1').fetchall()
        return [{'sha256':h,'paths':paths.split(','),'count':n} for h,paths,n in rows]
