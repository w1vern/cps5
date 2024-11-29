
import asyncio
import select
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import session_manager

from models import *


async def algorithm():
    print("Начинаем расчет")
    N = float(input("Введите значение для мощности, передаваемой ремнем, кВт; N: "))
    n_1 = float(
        input("Введите значение для частоты вращения меньшего шкива, мин^(-1); n_1: "))
    n_2 = float(
        input("Введите значение для частоты вращения большего шкива, мин^(-1); n_2: "))
    delta_small = float(input(
        "Введите значение для расстояния от впадины зуба ремня до оси металлического троса, мм; delta_small: "))
    T_1 = float(
        input("Введите значение наибольшего кружного момента, Н*м; T_1: "))
    cable_type = input("Тип троса: ")
    phi_p = float(input("phi_p: "))  # TODO: ???

    async with session_manager.session() as session:

        m = (int)(35 * (N/n_1)**(1/3))
        b = phi_p * m
        z_1 = await session.scalar(select(Table_3_3.z_1).where(Table_3_3.m == m,
                                                               Table_3_3.max_n_1 > n_1 - 250,
                                                               Table_3_3.min_n_1 < n_1 + 250
                                                               ).limit(1))
        if z_1 is None:
            print(f"Таблица 3.3 не содержит значения z_1 при m ={m}" +
                  f", n_1 = {n_1}")
            return
        u = n_1 / n_2
        z_2 = z_1 * u
        a_min = 0.5*(z_1+z_2) + 2*m
        a_max = 2 * m * (z_1 + z_2)
        a = float(input(f"a_min = {a_min:.2f}, a_max = " +
                        f"{a_max:.2f}, Введите a: "))
        t_p = await session.scalar(select(Table_3_1.t_p).where(Table_3_1.m == m).limit(1))
        if t_p is None:
            print("Таблица 3.1 не содержит значения t_p при m = ", m)
            return
        z_p = 2*a/t_p + (z_1+z_2)/2 + (z_2-z_1)**2*t_p/(40*a)
        z_ps = (await session.scalars(select(Table_3_4.z_p).where(Table_3_4.m == m))).all()
        z_p = min(z_ps, key=lambda x: abs(x-z_p))
        L_p = await session.scalar(select(Table_3_4.L_p).where(Table_3_4.m == m, Table_3_4.z_p == z_p).limit(1))
        if L_p is None:
            print(f"Таблица 3.4 не содержит значения L_p при m = {m}" +
                  f", z_p = {z_p}")
            return
        Lambda = L_p - t_p * (z_1 + z_2) / 2
        delta_big = m * (z_2-z_1) / 2
        a_real = (Lambda + (Lambda**2 - 8*delta_big**2)**0.5) / 4
        F_1 = 2 * 10**3 * T_1/(m*z_1)
        F_2 = 1.91 * 10**7 * N/(z_1*n_1*m)
        F = (F_1 + F_2) / 2  # TODO: ???
        i = await session.scalar(select(Table_3_5.i).where(Table_3_5.m == m, Table_3_5.cable_type == cable_type).limit(1))
        if i is None or i == -1:
            print(f"Таблица 3.5 не содержит значения i при m = {m}" +
                  f", cable_type = {cable_type}")
            return
        C_1 = 0.15 * F * i * z_1 / b
        C_2 = 0.15 * F * i * z_2 / b
        d_a_1 = m * z_1 - 2 * delta_small + C_1
        d_a_2 = m * z_1 - 2 * delta_small + C_1
        print(f"m = {m:.2f}, b = {b:.2f}, z_1 = {z_1:.2f}, z_2 = {z_2:.2f}, u = {u:.2f}, a_min = {a_min:.2f}, a_max = {a_max:.2f}, a = {a:.2f}, t_p = {t_p:.2f}, z_p = {z_p:.2f}, L_p = {L_p:.2f},\n" +
              f"lambda = {Lambda:.2f}, Delta= {delta_big:.2f}, a_real = {a_real:.2f}, i = {i:.4f}, F_1 = {F_1:2f}, F_2 = {F_2:.2f}, F = {F:.2f}, C_1 = {C_1:.2f}, C_2 = {C_2:.2f}, d_a_1 = {d_a_1:.2f}, d_a_2 = {d_a_2:.2f}")
        choice = input(
            f"Расчет прошел успешно. Добавить результаты в базу данных? (y/n): ")
        while True:
            if choice == 'y':
                params = Params(N=N, n_1=n_1, n_2=n_2, phi_p=phi_p, cable_type=cable_type,
                                delta_small=delta_small, T_1=T_1, m=m, b=b, z_1=z_1, z_2=z_2, u=u,
                                min_a=a_min, max_a=a_max, a=a, z_p=z_p, t_p=t_p, L_p=L_p, a_real=a_real,
                                Lambda=Lambda, delta_big=delta_big, d_a=d_a_1, C=C_1, F=F, i=i)
                session.add(params)
                await session.flush()
                return
            if choice == 'n':
                return
            choice = input(
                f"Некорректный ввод. Добавить результаты в базу данных? (y/n): ")


if __name__ == "__main__":
    asyncio.run(algorithm())
