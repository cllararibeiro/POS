from pydantic import BaseModel
from datetime import datetime

class Usuario(BaseModel):
    username:str
    password:str
    data_criacao:datetime


class Livro(BaseModel):
    titulo:str
    ano:int
    edicao:int

class Biblioteca(BaseModel):
    nome:str
    acervo: list
    usuario: list

class Emprestimo(BaseModel):
    usuario:Usuario
    livro:Livro
    data_emprestimo:datetime
    data_devolucao:datetime