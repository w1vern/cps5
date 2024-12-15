
import asyncio
import select
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import session_manager

from models import *


def create_default() -> tuple[Node, AssemblyUnit, Part, Part, Part]:
    with session_manager.session() as session:
        stmt = session.query(Node).order_by(Node.id.desc()).first()
        if stmt is None:
            n_id = 0
        else:
            n_id = stmt.id
        n = Node(id=n_id + 1)

        stmt = session.query(AssemblyUnit).order_by(
            AssemblyUnit.id.desc()).first()
        if stmt is None:
            a_id = 0
        else:
            a_id = stmt.id

        a = AssemblyUnit(id=a_id+1)
        a.node_id = n.id
        a.NSE = "передача"
        a.TSE = "ременная"
        a.VSE = "с зубчатым ремнем"

        p1 = Part()
        p1.assembly_unit_id = a.id
        p1.ND = "ремень"

        p2 = Part()
        p2.assembly_unit_id = a.id
        p2.ND = "шкив"
        p2.NaD = "ведущий"

        p3 = Part()
        p3.assembly_unit_id = a.id
        p3.ND = "шкив"
        p3.NaD = "ведомый"

        return n, a, p1, p2, p3


def algorithm(node: Node,
              assembly_unit: AssemblyUnit,
              belt: Part,
              shift_1: Part,
              shift_2: Part
              ) -> None:

    with session_manager.session() as session:
        belt.b = belt.phi_p * assembly_unit.m
        shift_1.z_1 = session.scalar(select(Table_3_3.z_1).where(Table_3_3.m == assembly_unit.m,  # type: ignore
                                                                 Table_3_3.max_n_1 > shift_1.n_1 - 250,
                                                                 Table_3_3.min_n_1 < shift_1.n_1 + 250
                                                                 ).limit(1))
        if shift_1.z_1 is None:
            print(f"Таблица 3.3 не содержит значения z_1 при m ={assembly_unit.m}" +
                  f", n_1 = {shift_1.n_1}")
            return
        assembly_unit.u = shift_1.n_1 / shift_2.n_2
        shift_2.z_2 = shift_1.z_1 * assembly_unit.u  # type: ignore
        assembly_unit.a_min = 0.5*(shift_1.z_1+shift_2.z_2) + 2*assembly_unit.m
        assembly_unit.a_max = 2 * assembly_unit.m * (shift_1.z_1 + shift_2.z_2)
        assembly_unit.a = (assembly_unit.a_min + assembly_unit.a_max)/2
        shift_1.t_p = session.scalar(  # type: ignore
            select(Table_3_1.t_p).where(Table_3_1.m == assembly_unit.m).limit(1))
        if shift_1.t_p is None:
            print("Таблица 3.1 не содержит значения t_p при m = ", assembly_unit.m)
            return
        shift_1.z_p = 2*assembly_unit.a/shift_1.t_p + (shift_1.z_1+shift_2.z_2)/2 + (
            # type: ignore
            shift_2.z_2-shift_1.z_1)**2*shift_1.t_p/(40*assembly_unit.a)
        z_ps = (session.scalars(
            select(Table_3_4.z_p).where(Table_3_4.m == assembly_unit.m))).all()
        shift_1.z_p = min(z_ps, key=lambda x: abs(x-shift_1.z_p))
        shift_1.L_p = session.scalar(select(Table_3_4.L_p).where(  # type: ignore
            Table_3_4.m == assembly_unit.m, Table_3_4.z_p == shift_1.z_p).limit(1))
        if shift_1.L_p is None:
            print(f"Таблица 3.4 не содержит значения L_p при m = {assembly_unit.m}" +
                  f", z_p = {shift_1.z_p}")
            return
        shift_1.Lambda = shift_1.L_p - shift_1.t_p * \
            (shift_1.z_1 + shift_2.z_2) / 2
        delta_big = assembly_unit.m * (shift_2.z_2-shift_1.z_1) / 2
        # a_real = (shift_1.Lambda + (shift_1.Lambda**2 - 8*delta_big**2)**0.5) / 4
        shift_1.F = 1.91 * 10**7 * belt.N / \
            (shift_1.z_1*shift_1.n_1*assembly_unit.m)
        shift_1.i = session.scalar(select(Table_3_5.i).where(  # type: ignore
            Table_3_5.m == assembly_unit.m, Table_3_5.cable_type == belt.cable_type).limit(1))
        if shift_1.i is None or shift_1.i == -1:
            print(f"Таблица 3.5 не содержит значения i при m = {assembly_unit.m}" +
                  f", cable_type = {belt.cable_type}")
            return
        shift_1.C_1 = 0.15 * shift_1.F * shift_1.i * shift_1.z_1 / belt.b
        shift_2.C_2 = 0.15 * shift_1.F * shift_1.i * shift_2.z_2 / belt.b
        shift_1.d_a1 = assembly_unit.m * shift_1.z_1 - \
            2 * assembly_unit.delta_small + shift_1.C_1
        shift_2.d_a2 = assembly_unit.m * shift_2.z_2 - \
            2 * assembly_unit.delta_small + shift_2.C_2


def save_results(node: Node, assembly_unit: AssemblyUnit, belt: Part, shift_1: Part, shift_2: Part) -> None:
    with session_manager.session() as session:
        session.add(node)
        session.add(assembly_unit)
        session.add(belt)
        session.add(shift_1)
        session.add(shift_2)
        session.flush()