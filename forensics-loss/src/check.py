import os
import sys
import zlib

def is_zlib_compressed(file_path):
    try:
        with open(file_path, 'rb') as f:
            # Read the first few bytes to check for the zlib header
            header = f.read(2)
            # Check if the header matches the zlib signature
            return header == b'\x78\x9c' or header == b'\x78\x01' or header == b'\x78\xda'
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

def find_zlib_files(directory):
    zlib_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_zlib_compressed(file_path):
                print(file_path)
                print(zlib.decompress(open(file_path, 'rb').read()))
    return zlib_files

directory_to_search = sys.argv[1]
find_zlib_files(directory_to_search)
