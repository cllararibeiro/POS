from fastapi import FastAPI, HTTPException
from models import Carro
from typing import List

app = FastAPI()

carros_db: List[Carro] = []

@app.get("/carros", response_model=List[Carro])
def listar_carros():
    return carros_db

@app.get("/carros/{placa}", response_model=Carro)
def buscar_carro(placa: str):
    for carro in carros_db:
        if carro.placa == placa:
            return carro
    raise HTTPException(status_code=404, detail="Carro não encontrado")

@app.post("/carros", response_model=Carro)
def adicionar_carro(carro: Carro):
    for c in carros_db:
        if c.placa == carro.placa:
            raise HTTPException(status_code=400, detail="Carro com essa placa já existe")
    carros_db.append(carro)
    return carro

@app.put("/carros/{placa}", response_model=Carro)
def atualizar_carro(placa: str, carro_atualizado: Carro):
    for i, carro in enumerate(carros_db):
        if carro.placa == placa:
            carros_db[i] = carro_atualizado
            return carro_atualizado
    raise HTTPException(status_code=404, detail="Carro não encontrado")

@app.delete("/carros/{placa}")
def remover_carro(placa: str):
    for i, carro in enumerate(carros_db):
        if carro.placa == placa:
            del carros_db[i]
            return {"mensagem": "Carro removido com sucesso"}
    raise HTTPException(status_code=404, detail="Carro não encontrado")
