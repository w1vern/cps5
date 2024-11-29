
import select
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import *


async def algorithm(session: AsyncSession, table_3_1, table_3_2, table_3_3, table_3_4, table_3_5, N, n_1, n_2, phi, cable_type, delta_small):
    m = 35 * (N/n_1)**(1/3)
    b = phi * m
    z_1 = await session.scalar(select(Table_3_3.z_1).where(Table_3_3.m == m,
                                                           Table_3_3.max_n_1 > n_1 - 250,
                                                           Table_3_3.min_n_1 < n_1 + 250
                                                           ).limit(1))
    if z_1 is None:
        print(f"Таблица 3.3 не содержит значения z_1 при m ={m}, n_1 = {n_1}")
        return
    u = n_1 / n_2
    z_2 = z_1 * u
    a_min = 0.5*(z_1+z_2) + 2*m
    a_max = 2 * m * (z_1 + z_2)
    print(f"a_min = {a_min}, a_max = {a_max}, Введите a:")
    a = float(input())
    t_p = await session.scalar(select(Table_3_1.t_p).where(Table_3_1.m == m).limit(1))
    if t_p is None:
        print("Таблица 3.1 не содержит значения t_p при m =", m)
        return
    z_p = 2*a/t_p + (z_1+z_2)/2 + (z_2-z_1)**2*t_p/(40*a)
    L_p = await session.scalar(select(Table_3_4.L_p).where(Table_3_4.m == m, Table_3_4.z_p == z_p).limit(1))
    if L_p is None:
        print(f"Таблица 3.4 не содержит значения L_p при m = {m}, z_p = {z_p}")
        return
    Lambda = L_p - t_p * (z_1 + z_2) / 2
    delta_big = m * (z_2-z_1) / 2
    a_real = (Lambda + (Lambda**2 - 8*delta_big**2)**0.5) / 4

