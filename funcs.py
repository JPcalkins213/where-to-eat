import config
import string
import requests
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine
from config import gkey
from pprint import pprint

def get_restaurants(zc):
    rest_names = []
    rest_addys = []
    #here i am getting the latitude and the longitude for the #zipcode the user enters
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={zc}&sensor=true&key={gkey}"
    response = requests.get(url).json()
    lat = response['results'][0]['geometry']['location']['lat']
    lng = response['results'][0]['geometry']['location']['lng']
    #with that info we can go ahead and grab the restaurants from #that zipcode within a 10 mile radius set to 16100 wich is a #little over 10 miles
    search_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=10500&keyword=food&key={gkey}"
    search = requests.get(search_url).json()
    for x in range(len(search['results'])-1):
        rest_names.append(search['results'][x]['name'])
        rest_addys.append(search['results'][x]['vicinity'])
    return rest_names, rest_addys

def get_zipcode():
    zip_code = input("whats your zip code? ")
    #here im just making sure the zip code is only 5 numbers long
    if len(zip_code) > 5 or len(zip_code) < 5:
        print("zipcode must 5 numbers")
        zip_code=input("whats your zip code? ")
    if zip_code == string:
        print("zip_code must be numbers only")
        zip_code=input('whats your zipcode? ')
    return zip_code


def to_df(name, addy, zip_code):

    zip_array = []
    for x in range(len(name)):
        zip_array.append(zip_code)
    df = pd.DataFrame()
    df['zip_code'] = zip_array
    df['name'] = name
    df['address'] = addy 
    return df

def to_pgadmin(df):
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/app_data')
    df.to_sql('restaurants', engine, if_exists='append')

#any engines i create once i get aws rds set up all engine links will need to change
def existence(zc):
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/app_data')
    data = engine.execute(
        f"SELECT COUNT(*) FROM restaurants WHERE zip_code = '{zc}'"
    )
    zip_count = data.fetchone()[0]
    print(zip_count)
    if zip_count > 0:
        return True
    elif zip_count == 0:
        return False