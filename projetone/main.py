from fastapi import FastAPI, HTTPException
from models import Tarefa
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Aceita requisições de qualquer origem (pode restringir depois)
    allow_credentials=True,
    allow_methods=["*"],  # Aceita todos os métodos HTTP (GET, POST, DELETE)
    allow_headers=["*"],  # Aceita todos os cabeçalhos
)


tarefas: List[Tarefa] = []

@app.get("/tarefas/", response_model=List[Tarefa])
def listar_tarefas():
    return tarefas


@app.post("/tarefas/", response_model=Tarefa)
def criar_tarefa(tarefa: Tarefa):
    tarefa.id = len(tarefas) + 1 
    tarefas.append(tarefa)
    return tarefa


@app.delete("/tarefas/{tarefa_id}", response_model=Tarefa)
def excluir_tarefa(tarefa_id: int):
    for index, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            return tarefas.pop(index)
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
