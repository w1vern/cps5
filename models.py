

import uuid
from database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Table_3_1(Base):
    __tablename__ = "table_3_1"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    m: Mapped[int] = mapped_column()
    t_p: Mapped[float] = mapped_column()


class Table_3_2(Base):
    __tablename__ = "table_3_2"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    m: Mapped[int] = mapped_column()
    b: Mapped[int] = mapped_column()
    possible: Mapped[bool] = mapped_column()


class Table_3_3(Base):
    __tablename__ = "table_3_3"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    m: Mapped[int] = mapped_column()
    min_n_1: Mapped[int] = mapped_column()
    max_n_1: Mapped[int] = mapped_column()
    z_1: Mapped[int] = mapped_column()


class Table_3_4(Base):
    __tablename__ = "table_3_4"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    z_p: Mapped[int] = mapped_column()
    L_p: Mapped[float] = mapped_column()
    m: Mapped[int] = mapped_column()


class Table_3_5(Base):
    __tablename__ = "table_3_5"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    m: Mapped[int] = mapped_column()
    cable_type: Mapped[str] = mapped_column()
    i: Mapped[float] = mapped_column()


class Params(Base):
    __tablename__ = "params"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    N: Mapped[float] = mapped_column()
    n_1: Mapped[float] = mapped_column()
    n_2: Mapped[float] = mapped_column()
    phi_p: Mapped[float] = mapped_column()
    cable_type: Mapped[str] = mapped_column()
    delta_small: Mapped[float] = mapped_column()
    T_1: Mapped[float] = mapped_column()

    m: Mapped[int] = mapped_column()
    b: Mapped[float] = mapped_column()
    z_1: Mapped[int] = mapped_column()
    z_2: Mapped[int] = mapped_column()
    u: Mapped[float] = mapped_column()
    min_a: Mapped[float] = mapped_column()
    max_a: Mapped[float] = mapped_column()
    a: Mapped[float] = mapped_column()
    z_p: Mapped[int] = mapped_column()
    t_p: Mapped[float] = mapped_column()
    L_p: Mapped[float] = mapped_column()
    a_real: Mapped[float] = mapped_column()
    Lambda: Mapped[float] = mapped_column()
    delta_big: Mapped[float] = mapped_column()
    d_a: Mapped[float] = mapped_column()
    C: Mapped[float] = mapped_column()
    F: Mapped[float] = mapped_column()
    i: Mapped[float] = mapped_column()
