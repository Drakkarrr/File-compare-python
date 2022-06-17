import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file1", type=str)
parser.add_argument("file2", type=str)

args = parser.parse_args()

def getFileMD5(file_name):
    file = open(file_name, mode="rb")
    data = file.read()
    return hashlib.md5(data).hexdigest()

hash1 = getFileMD5(args.file1)
hash2 = getFileMD5(args.file2)

if hash1 == hash2:
    print("Both files match")
else:
    print("Files dont match")