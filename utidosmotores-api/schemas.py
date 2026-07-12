from pydantic import BaseModel


class UsuarioIn(BaseModel):
    username: str
    email: str
    password: str

class LoginIn(BaseModel):
    username: str
    password: str

class ClienteIn(BaseModel):
    nome: str
    telefone: str
    cidade: str

class VeiculoIn(BaseModel):
    placa: str
    modelo: str
    cliente_id: int

class OrdemIn(BaseModel):
    problema: str
    veiculo_id: int
    mecanico_id: int

class OrdemUpdateIn(BaseModel):
    problema: str
    status: str