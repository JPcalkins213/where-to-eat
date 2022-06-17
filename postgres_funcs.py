from config import *
import sqlalchemy
from sqlalchemy import create_engine, null, text
import pandas as pd

def checking_postgres_existence(zip_code):
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
    url = f"postgresql://postgres:postgres@{dbendpoint}:5432/postgres"
    engine_db = create_engine(url)
    connection = engine_db.connect()
    #category
    query = """INSERT INTO Category CAST(category AS varchar)"""
    engine_db.execute(query)
    #restaurant
    df = pd.DataFrame()
    df['name'] = name
    df['address'] = addy
    df['categoryID'] = null
    df.to_sql('Category', con=connection, if_exists='replace', index=False)
    