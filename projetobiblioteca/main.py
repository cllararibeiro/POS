from fastapi import FastAPI, HTTPException
from models import Usuario, Livro, Biblioteca,Emprestimo
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

usuarios: List[Usuario] = []
livros: List[Livro] = []
bibliotecas: List[Biblioteca] = []
emprestimos: List[Emprestimo] = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Aceita requisições de qualquer origem (pode restringir depois)
    allow_credentials=True,
    allow_methods=["*"],  # Aceita todos os métodos HTTP (GET, POST, DELETE)
    allow_headers=["*"],  # Aceita todos os cabeçalhos
)

@app.post("/usuarios/", response_model=Usuario)
def cad_usu(usuario: Usuario):
    usuario.data_criacao = datetime.utcnow()
    usuarios.append(usuario)
    return usuario

@app.get("/usuarios/", response_model=List[Usuario])
def listar_usuarios():
    return usuarios

@app.delete("/usuarios/{username}", response_model=Usuario)
def excluir_usu(username: str):
    for index, usuario in enumerate(usuarios):
        if usuario.username == username:
            return usuarios.pop(index)
    raise HTTPException(status_code=404, detail="Usuario não encontrado")

@app.post("/livros/", response_model=Livro)
def cad_livro(livro: Livro):
    livros.append(livro)
    return livro

@app.get("/livros/", response_model=List[Livro])
def listar_livros():
    return livros

@app.delete("/livros/{titulo}", response_model=Livro)
def excluir_livro(titulo: str):
    for index, livro in enumerate(livros):
        if livro.titulo == titulo:
            return livros.pop(index)
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.post("/emprestimos/", response_model=Emprestimo)
def cad_emprestimo(emprestimo: Emprestimo):
    emprestimos.append(emprestimo)
    return emprestimo

@app.get("/emprestimos/", response_model=List[Emprestimo])
def listar_emprestimos():
    return emprestimos

@app.delete("/emprestimos/{username}/{titulo}", response_model=Usuario)
def excluir_usu(username: str, titulo: str):
    for index, emprestimo in enumerate(emprestimos):
        if emprestimo.usuario.username == username and emprestimo.livro.titulo == titulo:
            return emprestimos.pop(index)  
    raise HTTPException(status_code=404, detail="Empréstimo não encontrado")

@app.post("/bibliotecas/", response_model=Biblioteca)
def cad_bib(biblioteca: Biblioteca):
    bibliotecas.append(biblioteca)
    return biblioteca

@app.get("/bibliotecas/{nome}", response_model=Biblioteca)
def obter_biblioteca(nome: str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome:
            return biblioteca
    raise HTTPException(status_code=404, detail="Biblioteca não encontrada")

@app.delete("/bibliotecas/{nome}", response_model=Biblioteca)
def excluir_biblioteca(nome: str):
    for index, biblioteca in enumerate(bibliotecas):
        if biblioteca.nome == nome:
            return bibliotecas.pop(index) 
    raise HTTPException(status_code=404, detail="Biblioteca não encontrada")
