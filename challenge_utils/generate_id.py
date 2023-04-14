import hashlib, datetime

def generate_id(file_name):
    to_hash = file_name + (__file__)
    hashed_id = hashlib.sha256(to_hash.encode()).hexdigest()
    return hashed_id[:16]