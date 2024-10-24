import hashlib

def calculate_chekcsum(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def calculate_checksum():
    return None