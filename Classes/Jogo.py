from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from databases.db import db

class Jogo(db.Model):
    __tablename__ = 'Jogos'

    Id_jogos: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Nome: Mapped[str] = mapped_column(String(100))
    Categoria: Mapped[str] = mapped_column(String(100))
    Console: Mapped[str] = mapped_column(String(100))
    Jogo_ativo: Mapped[str] = mapped_column(String(1))