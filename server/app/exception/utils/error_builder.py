from datetime import datetime
from fastapi import Request

def build_error(request: Request, status: int, error: str, message: str):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "status": status,
        "error": error,
        "message": message,
        "path": request.url.path
    }