from pydantic import BaseModel

class LoginRespondeDTO(BaseModel):
    access_token: str
    token_type: str = "Bearer"