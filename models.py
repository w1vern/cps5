

import uuid

from sqlalchemy import ForeignKey
from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


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
    __tablename__ = "nodes"

    id: Mapped[int] = mapped_column(primary_key=True)


class AssemblyUnit(Base):
    __tablename__ = "assembly_units"

    id: Mapped[int] = mapped_column(primary_key=True)
    node_id: Mapped[int] = mapped_column(ForeignKey("nodes.id"))

    NSE: Mapped[str] = mapped_column()
    TSE: Mapped[str] = mapped_column()
    VSE: Mapped[str] = mapped_column()
    i: Mapped[int] = mapped_column(nullable=True)
    m: Mapped[int] = mapped_column(nullable=True)
    u: Mapped[float] = mapped_column(nullable=True)
    a_min: Mapped[float] = mapped_column(nullable=True)
    a_max: Mapped[float] = mapped_column(nullable=True)
    a: Mapped[float] = mapped_column(nullable=True)
    delta_small: Mapped[float] = mapped_column(nullable=True)
    delta_big: Mapped[float] = mapped_column(nullable=True)

    node: Mapped[Node] = relationship(foreign_keys=[node_id])


class Part(Base):
    __tablename__ = "parts"

    part_name: Mapped[str] = mapped_column(primary_key=True)
    assembly_unit_id: Mapped[int] = mapped_column(
        ForeignKey("assembly_units.id"), primary_key=True)

    ND: Mapped[str] = mapped_column()
    NaD: Mapped[str] = mapped_column(nullable=True)
    b: Mapped[float] = mapped_column(nullable=True)
    z_1: Mapped[int] = mapped_column(nullable=True)
    z_2: Mapped[int] = mapped_column(nullable=True)
    N: Mapped[float] = mapped_column(nullable=True)
    n_1: Mapped[float] = mapped_column(nullable=True)
    n_2: Mapped[float] = mapped_column(nullable=True)
    phi_p: Mapped[float] = mapped_column(nullable=True)
    cable_type: Mapped[str] = mapped_column(nullable=True)
    z_p: Mapped[int] = mapped_column(nullable=True)
    t_p: Mapped[float] = mapped_column(nullable=True)
    L_p: Mapped[float] = mapped_column(nullable=True)
    T_1: Mapped[float] = mapped_column(nullable=True)
    F: Mapped[float] = mapped_column(nullable=True)
    i: Mapped[float] = mapped_column(nullable=True)
    d_a1: Mapped[float] = mapped_column(nullable=True)
    d_a2: Mapped[float] = mapped_column(nullable=True)
    Lambda: Mapped[float] = mapped_column(nullable=True)
    C_1: Mapped[float] = mapped_column(nullable=True)
    C_2: Mapped[float] = mapped_column(nullable=True)

    assembly_unit: Mapped[AssemblyUnit] = relationship(
        foreign_keys=[assembly_unit_id])
