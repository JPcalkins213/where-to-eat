from config import *
import sqlalchemy
from sqlalchemy import create_engine, text

def checking_postgres_existence(zc):
    engine_db = create_engine(f'postgresql://postgres:postgres@{dbendpoint}:5432/to-be-named')
    data = engine_db.execute(
        f"SELECT COUNT(*) FROM restaurants WHERE zip_code = '{zc}'"
    )
    url = f"postgresql://postgres:postgres@{dbendpoint}:5432/postgres"
    engine_db = create_engine(url)
    connection = engine_db.connect()
    query= """SELECT COUNT(*) FROM  restaurants WHERE CAST(zip_code AS int) = 76065 """
    data = engine_db.execute(text(query)).fetchall()
    print(data)
    if data[0][0] > 0:
        return True
    elif data[0][0] == 0:
        return False

def add_data_to_postgres(name, addy, category):
    #category
    
    
    #restaurant