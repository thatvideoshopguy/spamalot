"""Compute the MD5 hash of a file. """
import hashlib


def compute_file_hash(file_path: str) -> str:
    """Return the MD5 hash of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The MD5 hash of the file.
    """
    hasher = hashlib.md5()
    with open(file_path, "rb") as open_file:
        buf = open_file.read()
        hasher.update(buf)
    return hasher.hexdigest()
