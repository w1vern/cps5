

import uuid

from sqlalchemy import ForeignKey
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

class Node(Base):
    __tablename__ = "node"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)

class AssemblyUnit(Base):
    __tablename__ = "assembly_unit"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    node_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id"))

    delta_small: Mapped[float] = mapped_column()
    m: Mapped[int] = mapped_column()
    u: Mapped[float] = mapped_column()
    min_a: Mapped[float] = mapped_column()
    max_a: Mapped[float] = mapped_column()
    a: Mapped[float] = mapped_column()
    a_real: Mapped[float] = mapped_column()
    C_1: Mapped[float] = mapped_column()
    C_2: Mapped[float] = mapped_column()
    delta_big: Mapped[float] = mapped_column()

    node: Mapped[Node] = mapped_column(foreign_keys=[node_id])


class Part(Base):
    __tablename__ = "part"

    part_name: Mapped[str] = mapped_column(primary_key=True)
    assembly_unit_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("assembly_unit.id"), primary_key=True)

    b: Mapped[float] = mapped_column()
    z_1: Mapped[int] = mapped_column()
    z_2: Mapped[int] = mapped_column()
    N: Mapped[float] = mapped_column()
    n_1: Mapped[float] = mapped_column()
    n_2: Mapped[float] = mapped_column()
    phi_p: Mapped[float] = mapped_column()
    cable_type: Mapped[str] = mapped_column()
    z_p: Mapped[int] = mapped_column()
    t_p: Mapped[float] = mapped_column()
    L_p: Mapped[float] = mapped_column()
    T_1: Mapped[float] = mapped_column()
    F: Mapped[float] = mapped_column()
    i: Mapped[float] = mapped_column()
    d_a_1: Mapped[float] = mapped_column()
    d_a_2: Mapped[float] = mapped_column()
    Lambda: Mapped[float] = mapped_column()

    assembly_unit: Mapped[AssemblyUnit] = mapped_column(foreign_keys=[assembly_unit_id])
