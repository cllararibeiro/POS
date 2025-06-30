from pydantic import BaseModel

class Carro(BaseModel):
    placa: int
    modelo: str
    marca: str
    placa: str 
    nome: str


