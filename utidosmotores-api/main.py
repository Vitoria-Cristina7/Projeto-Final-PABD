from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base, engine, get_db_connection
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
async def criar_usuario(dados: schemas.UsuarioIn, db: AsyncSession = Depends(get_db_connection)):
    return await crud.criar_usuario(db, dados)

@app.post("/usuarios/login")
async def login(dados: schemas.LoginIn, db: AsyncSession = Depends(get_db_connection)):
    return await crud.login(db, dados)


@app.post("/clientes")
async def criar_cliente(dados: schemas.ClienteIn, db: AsyncSession = Depends(get_db_connection)):
    return await crud.criar_cliente(db, dados)

@app.get("/clientes")
async def listar_clientes(db: AsyncSession = Depends(get_db_connection)):
    return await crud.listar_clientes(db)

@app.get("/clientes/{id}")
async def buscar_cliente(id: int, db: AsyncSession = Depends(get_db_connection)):
    return await crud.buscar_cliente(db, id)

@app.put("/clientes/{id}")
async def atualizar_cliente(id: int, dados: schemas.ClienteIn, db: AsyncSession = Depends(get_db_connection)):
    return await crud.atualizar_cliente(db, id, dados)

@app.delete("/clientes/{id}")
async def deletar_cliente(id: int, db: AsyncSession = Depends(get_db_connection)):
    return await crud.deletar_cliente(db, id)


@app.post("/veiculos")
async def criar_veiculo(dados: schemas.VeiculoIn, db: AsyncSession = Depends(get_db_connection)):
    return await crud.criar_veiculo(db, dados)

@app.get("/veiculos")
async def listar_veiculos(db: AsyncSession = Depends(get_db_connection)):
    return await crud.listar_veiculos(db)

@app.get("/veiculos/{id}")
async def buscar_veiculo(id: int, db: AsyncSession = Depends(get_db_connection)):
    return await crud.buscar_veiculo(db, id)

@app.put("/veiculos/{id}")
async def atualizar_veiculo(id: int, dados: schemas.VeiculoIn, db: AsyncSession = Depends(get_db_connection)):
    return await crud.atualizar_veiculo(db, id, dados)

@app.delete("/veiculos/{id}")
async def deletar_veiculo(id: int, db: AsyncSession = Depends(get_db_connection)):
    return await crud.deletar_veiculo(db, id)


@app.post("/ordens")
async def criar_ordem(dados: schemas.OrdemIn, db: AsyncSession = Depends(get_db_connection)):
    return await crud.criar_ordem(db, dados)

@app.get("/ordens")
async def listar_ordens(db: AsyncSession = Depends(get_db_connection)):
    return await crud.listar_ordens(db)

@app.get("/ordens/{id}")
async def buscar_ordem(id: int, db: AsyncSession = Depends(get_db_connection)):
    return await crud.buscar_ordem(db, id)

@app.put("/ordens/{id}")
async def atualizar_ordem(id: int, dados: schemas.OrdemUpdateIn, db: AsyncSession = Depends(get_db_connection)):
    return await crud.atualizar_ordem(db, id, dados)

@app.delete("/ordens/{id}")
async def deletar_ordem(id: int, db: AsyncSession = Depends(get_db_connection)):
    return await crud.deletar_ordem(db, id)