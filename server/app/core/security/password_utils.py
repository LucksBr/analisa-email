import bcrypt
import hashlib

def _normalize_password(password: str) -> bytes:
    normalized = hashlib.sha256(password.encode("utf-8")).digest()
    return normalized

def hash_password(password: str) -> str:
    normalized = _normalize_password(password)
    hashed = bcrypt.hashpw(normalized, bcrypt.gensalt())
    return hashed.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    normalized = _normalize_password(plain_password)
    return bcrypt.checkpw(
        normalized,
        hashed_password.encode("utf-8")
    )