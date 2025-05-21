from fastapi import FastAPI,HTTPException
from models import *
from typing import List

carros_db: List[Carro] = []
clientes_db: List[Cliente] = []
reservas_db: List[Reserva] = []

app = FastAPI()

@app.get("/carros", response_model=List[Carro])
def listar_carros():
    return carros_db

@app.post("/carros", response_model=Carro)
def adicionar_carro(carro: Carro):
    carros_db.append(carro)
    return carro

@app.put("/carros/{id}", response_model=Carro)
def atualizar_carro(id: int, carro_atualizado: Carro):
    for i, carro in enumerate(carros_db):
        if carro.id == id:
            carros_db[i] = carro_atualizado
            return carro_atualizado
    raise HTTPException(status_code=404, detail="Carro não encontrado")

@app.delete("/carros/{id}")
def remover_carro(id: int):
    for i, carro in enumerate(carros_db):
        if carro.id == id:
            del carros_db[i]
            return {"mensagem": "Carro removido com sucesso"}
    raise HTTPException(status_code=404, detail="Carro não encontrado")

@app.get("/carros/disponiveis", response_model=List[Carro])
def listar_carros_disponiveis():
    return [carro for carro in carros_db if carro.disponivel]


@app.get("/clientes", response_model=List[Cliente])
def listar_clientes():
    return clientes_db

@app.post("/clientes", response_model=Cliente)
def adicionar_cliente(cliente: Cliente):
    clientes_db.append(cliente)
    return cliente

@app.get("/clientes/{id}", response_model=Cliente)
def buscar_cliente_por_id(id: int):
    for cliente in clientes_db:
        if cliente.id == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")


@app.post("/reservas", response_model=Reserva)
def criar_reserva(reserva: Reserva):
    for i, carro in enumerate(carros_db):
        if carro.id == reserva.carro.id:
            if not carro.disponivel:
                raise HTTPException(status_code=400, detail="Carro indisponível")
            carros_db[i].disponivel = False
            reservas_db.append(reserva)
            return reserva
    raise HTTPException(status_code=404, detail="Carro não encontrado")

@app.get("/reservas", response_model=List[Reserva])
def listar_reservas():
    return reservas_db

@app.delete("/reservas/{id}")
def cancelar_reserva(id: int):
    for i, reserva in enumerate(reservas_db):
        if reserva.id == id:
            for carro in carros_db:
                if carro.id == reserva.carro.id:
                    carro.disponivel = True
                    break
            del reservas_db[i]
            return {"mensagem": "Reserva cancelada com sucesso"}
    raise HTTPException(status_code=404, detail="Reserva não encontrada")