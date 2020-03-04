import os
import hashlib

print(os.path.getsize('upload.txt'))
with open("upload.txt", "rb") as f:
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)
print(file_hash.digest())
print(file_hash.hexdigest())