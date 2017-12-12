import hashlib

def hash_image(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        img = f.read()
        hasher.update(img)
    return hasher.hexdigest()
