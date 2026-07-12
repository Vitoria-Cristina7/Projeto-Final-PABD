from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Usuario(Base):
    _tablename_ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]

    ordens: Mapped[list["OrdemServico"]] = relationship(back_populates="mecanico")


class Cliente(Base):
    _tablename_ = "clientes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    telefone: Mapped[str]
    cidade: Mapped[str]

    veiculos: Mapped[list["Veiculo"]] = relationship(back_populates="cliente")


class Veiculo(Base):
    _tablename_ = "veiculos"
    id: Mapped[int] = mapped_column(primary_key=True)
    placa: Mapped[str] = mapped_column(unique=True)
    modelo: Mapped[str]

    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"))
    cliente: Mapped["Cliente"] = relationship(back_populates="veiculos")

    ordens: Mapped[list["OrdemServico"]] = relationship(back_populates="veiculo")


class OrdemServico(Base):
    _tablename_ = "ordens_servico"
    id: Mapped[int] = mapped_column(primary_key=True)
    problema: Mapped[str]
    status: Mapped[str] = mapped_column(default="aberta")

    veiculo_id: Mapped[int] = mapped_column(ForeignKey("veiculos.id"))
    veiculo: Mapped["Veiculo"] = relationship(back_populates="ordens")

    mecanico_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    mecanico: Mapped["Usuario"] = relationship(back_populates="ordens")