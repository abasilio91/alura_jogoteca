from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from databases.db import db

class Usuario(db.Model):
    __tablename__ = 'Usuarios'

    Id_usuario: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Nome: Mapped[str] = mapped_column(String(100))
    Nickname: Mapped[str] = mapped_column(String(100))
    Senha: Mapped[str] = mapped_column(String(100))
    Usuario_ativo: Mapped['str'] = mapped_column(String(1))