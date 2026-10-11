import argparse,json
from .store import FileStore
from .scanner import scan_directory

def main():
 p=argparse.ArgumentParser(prog='ddas'); s=p.add_subparsers(dest='cmd',required=True)
 i=s.add_parser('init'); i.add_argument('--db',required=True)
 q=s.add_parser('scan'); q.add_argument('--db',required=True); q.add_argument('--directory',required=True)
 d=s.add_parser('duplicates'); d.add_argument('--db',required=True)
 a=p.parse_args(); store=FileStore(a.db)
 if a.cmd=='scan': print(json.dumps(scan_directory(a.directory,store),indent=2))
 elif a.cmd=='duplicates': print(json.dumps(store.duplicates(),indent=2))
 else: print('database initialized:',a.db)
if __name__=='__main__': main()
