from pydantic import BaseModel
from typing import Optional

class instituicao(BaseModel):
    chave: int
    nome: str

class lista_email(BaseModel):
    id: Optional(int) = None
    email: str
    situacao: int

    class config:
        orm_mode = True
        