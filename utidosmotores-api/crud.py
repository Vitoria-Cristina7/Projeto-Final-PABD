from sqlalchemy import select
from passlib.context import CryptContext
from database import get_db_connection
import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"])


async def criar_usuario(dados: schemas.UsuarioIn):
    db = await get_db_connection()
    try:
        hash_senha = pwd_context.hash(dados.password)
        usuario = models.Usuario(username=dados.username, email=dados.email, password_hash=hash_senha)
        db.add(usuario)
        await db.commit()
        await db.refresh(usuario)
        return {"message": "Usuário cadastrado!", "id": usuario.id}
    finally:
        await db.close()

async def login(dados: schemas.LoginIn):
    db = await get_db_connection()
    try:
        result = await db.execute(select(models.Usuario).where(models.Usuario.username == dados.username))
        usuario = result.scalar_one_or_none()
        if not usuario or not pwd_context.verify(dados.password, usuario.password_hash):
            return {"message": "Username ou senha inválidos."}
        return {"message": f"Login bem-sucedido, {usuario.username}!"}
    finally:
        await db.close()


async def criar_cliente(dados: schemas.ClienteIn):
    db = await get_db_connection()
    try:
        cliente = models.Cliente(**dados.model_dump())
        db.add(cliente)
        await db.commit()
        await db.refresh(cliente)
        return {"message": "Cliente criado!", "id": cliente.id}
    finally:
        await db.close()

async def listar_clientes():
    db = await get_db_connection()
    try:
        result = await db.execute(select(models.Cliente))
        return result.scalars().all()
    finally:
        await db.close()

async def buscar_cliente(id: int):
    db = await get_db_connection()
    try:
        cliente = await db.get(models.Cliente, id)
        if not cliente:
            return {"message": "Cliente não encontrado."}
        return cliente
    finally:
        await db.close()

async def atualizar_cliente(id: int, dados: schemas.ClienteIn):
    db = await get_db_connection()
    try:
        cliente = await db.get(models.Cliente, id)
        if not cliente:
            return {"message": "Cliente não encontrado."}
        cliente.nome = dados.nome
        cliente.telefone = dados.telefone
        cliente.cidade = dados.cidade
        await db.commit()
        return {"message": "Cliente atualizado!"}
    finally:
        await db.close()

async def deletar_cliente(id: int):
    db = await get_db_connection()
    try:
        cliente = await db.get(models.Cliente, id)
        if not cliente:
            return {"message": "Cliente não encontrado."}
        await db.delete(cliente)
        await db.commit()
        return {"message": "Cliente removido!"}
    finally:
        await db.close()


async def criar_veiculo(dados: schemas.VeiculoIn):
    db = await get_db_connection()
    try:
        cliente = await db.get(models.Cliente, dados.cliente_id)
        if not cliente:
            return {"message": "Cliente não encontrado."}
        veiculo = models.Veiculo(placa=dados.placa, modelo=dados.modelo, cliente_id=dados.cliente_id)
        db.add(veiculo)
        await db.commit()
        await db.refresh(veiculo)
        return {"message": "Veículo criado!", "id": veiculo.id}
    finally:
        await db.close()

async def listar_veiculos():
    db = await get_db_connection()
    try:
        result = await db.execute(select(models.Veiculo))
        return result.scalars().all()
    finally:
        await db.close()

async def buscar_veiculo(id: int):
    db = await get_db_connection()
    try:
        veiculo = await db.get(models.Veiculo, id)
        if not veiculo:
            return {"message": "Veículo não encontrado."}
        return veiculo
    finally:
        await db.close()

async def atualizar_veiculo(id: int, dados: schemas.VeiculoIn):
    db = await get_db_connection()
    try:
        veiculo = await db.get(models.Veiculo, id)
        if not veiculo:
            return {"message": "Veículo não encontrado."}
        veiculo.placa = dados.placa
        veiculo.modelo = dados.modelo
        veiculo.cliente_id = dados.cliente_id
        await db.commit()
        return {"message": "Veículo atualizado!"}
    finally:
        await db.close()

async def deletar_veiculo(id: int):
    db = await get_db_connection()
    try:
        veiculo = await db.get(models.Veiculo, id)
        if not veiculo:
            return {"message": "Veículo não encontrado."}
        await db.delete(veiculo)
        await db.commit()
        return {"message": "Veículo removido!"}
    finally:
        await db.close()


async def criar_ordem(dados: schemas.OrdemIn):
    db = await get_db_connection()
    try:
        veiculo = await db.get(models.Veiculo, dados.veiculo_id)
        mecanico = await db.get(models.Usuario, dados.mecanico_id)
        if not veiculo or not mecanico:
            return {"message": "Veículo ou usuário não encontrado."}
        ordem = models.OrdemServico(problema=dados.problema, veiculo_id=dados.veiculo_id, mecanico_id=dados.mecanico_id)
        db.add(ordem)
        await db.commit()
        await db.refresh(ordem)
        return {"message": "Ordem criada!", "id": ordem.id}
    finally:
        await db.close()

async def listar_ordens():
    db = await get_db_connection()
    try:
        result = await db.execute(select(models.OrdemServico))
        return result.scalars().all()
    finally:
        await db.close()

async def buscar_ordem(id: int):
    db = await get_db_connection()
    try:
        ordem = await db.get(models.OrdemServico, id)
        if not ordem:
            return {"message": "Ordem não encontrada."}
        return ordem
    finally:
        await db.close()

async def atualizar_ordem(id: int, dados: schemas.OrdemUpdateIn):
    db = await get_db_connection()
    try:
        ordem = await db.get(models.OrdemServico, id)
        if not ordem:
            return {"message": "Ordem não encontrada."}
        ordem.problema = dados.problema
        ordem.status = dados.status
        await db.commit()
        return {"message": "Ordem atualizada!"}
    finally:
        await db.close()

async def deletar_ordem(id: int):
    db = await get_db_connection()
    try:
        ordem = await db.get(models.OrdemServico, id)
        if not ordem:
            return {"message": "Ordem não encontrada."}
        await db.delete(ordem)
        await db.commit()
        return {"message": "Ordem removida!"}
    finally:
        await db.close()