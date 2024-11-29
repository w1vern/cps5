

import asyncio
from re import L
from database import session_manager
from database import create_db_and_tables
from models import *


async def main():
    await create_db_and_tables()
    table_3_1 = [Table_3_1(m=2, t_p=6.283),
                 Table_3_1(m=3, t_p=9.425),
                 Table_3_1(m=4, t_p=12.566),
                 Table_3_1(m=5, t_p=15.708),
                 Table_3_1(m=6, t_p=21.991),
                 Table_3_1(m=7, t_p=31.416)]
    table_3_2 = []

    table_3_2.append(Table_3_2(m=2, b=8, possible=True))
    table_3_2.append(Table_3_2(m=2, b=10, possible=True))
    table_3_2.append(Table_3_2(m=2, b=12.5, possible=True))
    table_3_2.append(Table_3_2(m=2, b=16, possible=True))
    table_3_2.append(Table_3_2(m=2, b=20, possible=False))
    table_3_2.append(Table_3_2(m=2, b=25, possible=False))
    table_3_2.append(Table_3_2(m=2, b=32, possible=False))
    table_3_2.append(Table_3_2(m=2, b=40, possible=False))
    table_3_2.append(Table_3_2(m=2, b=50, possible=False))
    table_3_2.append(Table_3_2(m=2, b=63, possible=False))
    table_3_2.append(Table_3_2(m=2, b=80, possible=False))

    table_3_2.append(Table_3_2(m=3, b=8, possible=False))
    table_3_2.append(Table_3_2(m=3, b=10, possible=False))
    table_3_2.append(Table_3_2(m=3, b=12.5, possible=True))
    table_3_2.append(Table_3_2(m=3, b=16, possible=True))
    table_3_2.append(Table_3_2(m=3, b=20, possible=True))
    table_3_2.append(Table_3_2(m=3, b=25, possible=True))
    table_3_2.append(Table_3_2(m=3, b=32, possible=False))
    table_3_2.append(Table_3_2(m=3, b=40, possible=False))
    table_3_2.append(Table_3_2(m=3, b=50, possible=False))
    table_3_2.append(Table_3_2(m=3, b=63, possible=False))
    table_3_2.append(Table_3_2(m=3, b=80, possible=False))

    table_3_2.append(Table_3_2(m=4, b=8, possible=False))
    table_3_2.append(Table_3_2(m=4, b=10, possible=False))
    table_3_2.append(Table_3_2(m=4, b=12.5, possible=False))
    table_3_2.append(Table_3_2(m=4, b=16, possible=False))
    table_3_2.append(Table_3_2(m=4, b=20, possible=True))
    table_3_2.append(Table_3_2(m=4, b=25, possible=True))
    table_3_2.append(Table_3_2(m=4, b=32, possible=True))
    table_3_2.append(Table_3_2(m=4, b=40, possible=True))
    table_3_2.append(Table_3_2(m=4, b=50, possible=False))
    table_3_2.append(Table_3_2(m=4, b=63, possible=False))
    table_3_2.append(Table_3_2(m=4, b=80, possible=False))

    table_3_2.append(Table_3_2(m=5, b=8, possible=False))
    table_3_2.append(Table_3_2(m=5, b=10, possible=False))
    table_3_2.append(Table_3_2(m=5, b=12.5, possible=False))
    table_3_2.append(Table_3_2(m=5, b=16, possible=False))
    table_3_2.append(Table_3_2(m=5, b=20, possible=False))
    table_3_2.append(Table_3_2(m=5, b=25, possible=True))
    table_3_2.append(Table_3_2(m=5, b=32, possible=True))
    table_3_2.append(Table_3_2(m=5, b=40, possible=True))
    table_3_2.append(Table_3_2(m=5, b=50, possible=True))
    table_3_2.append(Table_3_2(m=5, b=63, possible=False))
    table_3_2.append(Table_3_2(m=5, b=80, possible=False))

    table_3_2.append(Table_3_2(m=7, b=8, possible=False))
    table_3_2.append(Table_3_2(m=7, b=10, possible=False))
    table_3_2.append(Table_3_2(m=7, b=12.5, possible=False))
    table_3_2.append(Table_3_2(m=7, b=16, possible=False))
    table_3_2.append(Table_3_2(m=7, b=20, possible=False))
    table_3_2.append(Table_3_2(m=7, b=25, possible=False))
    table_3_2.append(Table_3_2(m=7, b=32, possible=False))
    table_3_2.append(Table_3_2(m=7, b=40, possible=False))
    table_3_2.append(Table_3_2(m=7, b=50, possible=True))
    table_3_2.append(Table_3_2(m=7, b=63, possible=True))
    table_3_2.append(Table_3_2(m=7, b=80, possible=True))

    table_3_2.append(Table_3_2(m=10, b=8, possible=False))
    table_3_2.append(Table_3_2(m=10, b=10, possible=False))
    table_3_2.append(Table_3_2(m=10, b=12.5, possible=False))
    table_3_2.append(Table_3_2(m=10, b=16, possible=False))
    table_3_2.append(Table_3_2(m=10, b=20, possible=False))
    table_3_2.append(Table_3_2(m=10, b=25, possible=False))
    table_3_2.append(Table_3_2(m=10, b=32, possible=False))
    table_3_2.append(Table_3_2(m=10, b=40, possible=False))
    table_3_2.append(Table_3_2(m=10, b=50, possible=True))
    table_3_2.append(Table_3_2(m=10, b=63, possible=True))
    table_3_2.append(Table_3_2(m=10, b=80, possible=True))

    table_3_3 = []
    table_3_3.append(Table_3_3(m=2, min_n_1=500, max_n_1=3000, z_1=12))
    table_3_3.append(Table_3_3(m=2, min_n_1=3500, max_n_1=4500, z_1=14))
    table_3_3.append(Table_3_3(m=2, min_n_1=5000, max_n_1=6800, z_1=16))
    table_3_3.append(Table_3_3(m=2, min_n_1=7000, max_n_1=7500, z_1=18))

    table_3_3.append(Table_3_3(m=3, min_n_1=500, max_n_1=1000, z_1=12))
    table_3_3.append(Table_3_3(m=3, min_n_1=1500, max_n_1=2000, z_1=14))
    table_3_3.append(Table_3_3(m=3, min_n_1=2500, max_n_1=3500, z_1=16))
    table_3_3.append(Table_3_3(m=3, min_n_1=4000, max_n_1=5000, z_1=18))

    table_3_3.append(Table_3_3(m=4, min_n_1=500, max_n_1=500, z_1=12))
    table_3_3.append(Table_3_3(m=4, min_n_1=1000, max_n_1=1000, z_1=14))
    table_3_3.append(Table_3_3(m=4, min_n_1=1500, max_n_1=2000, z_1=16))
    table_3_3.append(Table_3_3(m=4, min_n_1=2500, max_n_1=3500, z_1=18))

    table_3_3.append(Table_3_3(m=5, min_n_1=500, max_n_1=500, z_1=16))
    table_3_3.append(Table_3_3(m=5, min_n_1=1000, max_n_1=1500, z_1=18))
    table_3_3.append(Table_3_3(m=5, min_n_1=2000, max_n_1=3000, z_1=20))
    table_3_3.append(Table_3_3(m=5, min_n_1=3500, max_n_1=4000, z_1=22))

    table_3_3.append(Table_3_3(m=7, min_n_1=500, max_n_1=500, z_1=20))
    table_3_3.append(Table_3_3(m=7, min_n_1=1000, max_n_1=1000, z_1=22))
    table_3_3.append(Table_3_3(m=7, min_n_1=1500, max_n_1=1500, z_1=24))
    table_3_3.append(Table_3_3(m=7, min_n_1=2000, max_n_1=2000, z_1=26))

    table_3_3.append(Table_3_3(m=10, min_n_1=500, max_n_1=500, z_1=20))
    table_3_3.append(Table_3_3(m=10, min_n_1=1000, max_n_1=1000, z_1=22))
    table_3_3.append(Table_3_3(m=10, min_n_1=1500, max_n_1=1500, z_1=24))
    table_3_3.append(Table_3_3(m=10, min_n_1=2000, max_n_1=2000, z_1=26))

    table_3_4 = []

    table_3_4.append(Table_3_4(z_p=32, m=2, L_p=201))
    table_3_4.append(Table_3_4(z_p=32, m=3, L_p=-1))
    table_3_4.append(Table_3_4(z_p=32, m=4, L_p=-1))
    table_3_4.append(Table_3_4(z_p=32, m=5, L_p=-1))
    table_3_4.append(Table_3_4(z_p=32, m=7, L_p=-1))
    table_3_4.append(Table_3_4(z_p=32, m=10, L_p=-1))

    table_3_4.append(Table_3_4(z_p=36, m=2, L_p=226.1))
    table_3_4.append(Table_3_4(z_p=36, m=3, L_p=339.1))
    table_3_4.append(Table_3_4(z_p=36, m=4, L_p=-1))
    table_3_4.append(Table_3_4(z_p=36, m=5, L_p=-1))
    table_3_4.append(Table_3_4(z_p=36, m=7, L_p=-1))
    table_3_4.append(Table_3_4(z_p=36, m=10, L_p=-1))

    table_3_4.append(Table_3_4(z_p=40, m=2, L_p=251.2))
    table_3_4.append(Table_3_4(z_p=40, m=3, L_p=376.8))
    table_3_4.append(Table_3_4(z_p=40, m=4, L_p=502.4))
    table_3_4.append(Table_3_4(z_p=40, m=5, L_p=-1))
    table_3_4.append(Table_3_4(z_p=40, m=7, L_p=-1))
    table_3_4.append(Table_3_4(z_p=40, m=10, L_p=-1))

    table_3_4.append(Table_3_4(z_p=45, m=2, L_p=282.6))
    table_3_4.append(Table_3_4(z_p=45, m=3, L_p=423.9))
    table_3_4.append(Table_3_4(z_p=45, m=4, L_p=565.2))
    table_3_4.append(Table_3_4(z_p=45, m=5, L_p=706.5))
    table_3_4.append(Table_3_4(z_p=45, m=7, L_p=-1))
    table_3_4.append(Table_3_4(z_p=45, m=10, L_p=-1))

    table_3_4.append(Table_3_4(z_p=50, m=2, L_p=314))
    table_3_4.append(Table_3_4(z_p=50, m=3, L_p=471))
    table_3_4.append(Table_3_4(z_p=50, m=4, L_p=628))
    table_3_4.append(Table_3_4(z_p=50, m=5, L_p=785))
    table_3_4.append(Table_3_4(z_p=50, m=7, L_p=989.1))
    table_3_4.append(Table_3_4(z_p=50, m=10, L_p=-1))

    table_3_4.append(Table_3_4(z_p=56, m=2, L_p=351.7))
    table_3_4.append(Table_3_4(z_p=56, m=3, L_p=527.5))
    table_3_4.append(Table_3_4(z_p=56, m=4, L_p=703.4))
    table_3_4.append(Table_3_4(z_p=56, m=5, L_p=879.2))
    table_3_4.append(Table_3_4(z_p=56, m=7, L_p=1099))
    table_3_4.append(Table_3_4(z_p=56, m=10, L_p=1570))

    table_3_4.append(Table_3_4(z_p=63, m=2, L_p=395.6))
    table_3_4.append(Table_3_4(z_p=63, m=3, L_p=593.5))
    table_3_4.append(Table_3_4(z_p=63, m=4, L_p=791.3))
    table_3_4.append(Table_3_4(z_p=63, m=5, L_p=989.1))
    table_3_4.append(Table_3_4(z_p=63, m=7, L_p=1230.9))
    table_3_4.append(Table_3_4(z_p=63, m=10, L_p=1758.4))

    table_3_4.append(Table_3_4(z_p=71, m=2, L_p=445.9))
    table_3_4.append(Table_3_4(z_p=71, m=3, L_p=668.8))
    table_3_4.append(Table_3_4(z_p=71, m=4, L_p=891.8))
    table_3_4.append(Table_3_4(z_p=71, m=5, L_p=1114.7))
    table_3_4.append(Table_3_4(z_p=71, m=7, L_p=1384.7))
    table_3_4.append(Table_3_4(z_p=71, m=10, L_p=1978.2))

    table_3_4.append(Table_3_4(z_p=80, m=2, L_p=502.4))
    table_3_4.append(Table_3_4(z_p=80, m=3, L_p=753.6))
    table_3_4.append(Table_3_4(z_p=80, m=4, L_p=1004.8))
    table_3_4.append(Table_3_4(z_p=80, m=5, L_p=1256))
    table_3_4.append(Table_3_4(z_p=80, m=7, L_p=1560.6))
    table_3_4.append(Table_3_4(z_p=80, m=10, L_p=2229.4))

    table_3_4.append(Table_3_4(z_p=90, m=2, L_p=565.2))
    table_3_4.append(Table_3_4(z_p=90, m=3, L_p=847.8))
    table_3_4.append(Table_3_4(z_p=90, m=4, L_p=1130.4))
    table_3_4.append(Table_3_4(z_p=90, m=5, L_p=1413))
    table_3_4.append(Table_3_4(z_p=90, m=7, L_p=1758.4))
    table_3_4.append(Table_3_4(z_p=90, m=10, L_p=2512))

    table_3_4.append(Table_3_4(z_p=100, m=2, L_p=628))
    table_3_4.append(Table_3_4(z_p=100, m=3, L_p=942))
    table_3_4.append(Table_3_4(z_p=100, m=4, L_p=1256))
    table_3_4.append(Table_3_4(z_p=100, m=5, L_p=1570))
    table_3_4.append(Table_3_4(z_p=100, m=7, L_p=1978.2))
    table_3_4.append(Table_3_4(z_p=100, m=10, L_p=2826))

    table_3_4.append(Table_3_4(z_p=112, m=2, L_p=703.4))
    table_3_4.append(Table_3_4(z_p=112, m=3, L_p=1055))
    table_3_4.append(Table_3_4(z_p=112, m=4, L_p=1406.7))
    table_3_4.append(Table_3_4(z_p=112, m=5, L_p=1758.4))
    table_3_4.append(Table_3_4(z_p=112, m=7, L_p=2198))
    table_3_4.append(Table_3_4(z_p=112, m=10, L_p=3140))

    table_3_4.append(Table_3_4(z_p=125, m=2, L_p=785))
    table_3_4.append(Table_3_4(z_p=125, m=3, L_p=1177.5))
    table_3_4.append(Table_3_4(z_p=125, m=4, L_p=1570))
    table_3_4.append(Table_3_4(z_p=125, m=5, L_p=1962.5))
    table_3_4.append(Table_3_4(z_p=125, m=7, L_p=2461.8))
    table_3_4.append(Table_3_4(z_p=125, m=10, L_p=-1))

    table_3_4.append(Table_3_4(z_p=140, m=2, L_p=-1))
    table_3_4.append(Table_3_4(z_p=140, m=3, L_p=1318.8))
    table_3_4.append(Table_3_4(z_p=140, m=4, L_p=1758.4))
    table_3_4.append(Table_3_4(z_p=140, m=5, L_p=2198))
    table_3_4.append(Table_3_4(z_p=140, m=7, L_p=2747.5))
    table_3_4.append(Table_3_4(z_p=140, m=10, L_p=-1))

    table_3_4.append(Table_3_4(z_p=160, m=2, L_p=-1))
    table_3_4.append(Table_3_4(z_p=160, m=3, L_p=1507.2))
    table_3_4.append(Table_3_4(z_p=160, m=4, L_p=2009.6))
    table_3_4.append(Table_3_4(z_p=160, m=5, L_p=-1))
    table_3_4.append(Table_3_4(z_p=160, m=7, L_p=-1))
    table_3_4.append(Table_3_4(z_p=160, m=10, L_p=-1))

    table_3_5 = []

    table_3_5.append(Table_3_5(m=2, cable_type="1x7", i=0.0018))
    table_3_5.append(Table_3_5(m=3, cable_type="1x7", i=0.0025))
    table_3_5.append(Table_3_5(m=4, cable_type="1x7", i=0.003))
    table_3_5.append(Table_3_5(m=5, cable_type="1x7", i=-1))
    table_3_5.append(Table_3_5(m=7, cable_type="1x7", i=-1))
    table_3_5.append(Table_3_5(m=10, cable_type="1x7", i=-1))

    table_3_5.append(Table_3_5(m=2, cable_type="1x21", i=-1))
    table_3_5.append(Table_3_5(m=3, cable_type="1x21", i=-1))
    table_3_5.append(Table_3_5(m=4, cable_type="1x21", i=0.0011))
    table_3_5.append(Table_3_5(m=5, cable_type="1x21", i=0.0013))
    table_3_5.append(Table_3_5(m=7, cable_type="1x21", i=0.0019))
    table_3_5.append(Table_3_5(m=10, cable_type="1x21", i=0.0025))

    async with session_manager.session() as session:
        session.add_all(table_3_1)
        session.add_all(table_3_2)
        session.add_all(table_3_3)
        session.add_all(table_3_4)
        session.add_all(table_3_5)
        await session.flush()


if __name__ == "__main__":
    asyncio.run(main())
