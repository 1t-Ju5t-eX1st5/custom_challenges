import hashlib

def read_file_contents(file_path) -> str:
    with open(file_path, "r") as file:
        return file.read() 

def generate_id(file_path) -> str:
    to_hash = file_path + read_file_contents(file_path)
    hashed_id = hashlib.sha256(to_hash.encode()).hexdigest()
    return hashed_id[:16]

file_path = r"custom_challenges\intermediate\coding\caesar_cipher_decrypt.py"
print(generate_id(file_path))