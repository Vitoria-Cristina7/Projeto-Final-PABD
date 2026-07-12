from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import Base, engine
import models
import schemas
import crud


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/usuarios")
async def criar_usuario(dados: schemas.UsuarioIn):
    return await crud.criar_usuario(dados)

@app.post("/usuarios/login")
async def login(dados: schemas.LoginIn):
    return await crud.login(dados)


@app.post("/clientes")
async def criar_cliente(dados: schemas.ClienteIn):
    return await crud.criar_cliente(dados)

@app.get("/clientes")
async def listar_clientes():
    return await crud.listar_clientes()

@app.get("/clientes/{id}")
async def buscar_cliente(id: int):
    return await crud.buscar_cliente(id)

@app.put("/clientes/{id}")
async def atualizar_cliente(id: int, dados: schemas.ClienteIn):
    return await crud.atualizar_cliente(id, dados)

@app.delete("/clientes/{id}")
async def deletar_cliente(id: int):
    return await crud.deletar_cliente(id)


@app.post("/veiculos")
async def criar_veiculo(dados: schemas.VeiculoIn):
    return await crud.criar_veiculo(dados)

@app.get("/veiculos")
async def listar_veiculos():
    return await crud.listar_veiculos()

@app.get("/veiculos/{id}")
async def buscar_veiculo(id: int):
    return await crud.buscar_veiculo(id)

@app.put("/veiculos/{id}")
async def atualizar_veiculo(id: int, dados: schemas.VeiculoIn):
    return await crud.atualizar_veiculo(id, dados)

@app.delete("/veiculos/{id}")
async def deletar_veiculo(id: int):
    return await crud.deletar_veiculo(id)


@app.post("/ordens")
async def criar_ordem(dados: schemas.OrdemIn):
    return await crud.criar_ordem(dados)

@app.get("/ordens")
async def listar_ordens():
    return await crud.listar_ordens()

@app.get("/ordens/{id}")
async def buscar_ordem(id: int):
    return await crud.buscar_ordem(id)

@app.put("/ordens/{id}")
async def atualizar_ordem(id: int, dados: schemas.OrdemUpdateIn):
    return await crud.atualizar_ordem(id, dados)

@app.delete("/ordens/{id}")
async def deletar_ordem(id: int):
    return await crud.deletar_ordem(id)