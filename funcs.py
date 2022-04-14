import config
import string
import requests
import pandas as pd
import numpy as np
import boto3
import io
from io import StringIO
from sqlalchemy import create_engine, text
from config import gkey, db_endpoint, access_key_id, secret_access_key
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

#this will need to be changed to to_csv for aws s3 sake
def to_csv_s3(name, addy, zip_code):

    zip_array = []
    for x in range(len(name)):
        zip_array.append(zip_code)
    df = pd.DataFrame()
    df['zip_code'] = zip_array
    df['name'] = name
    df['address'] = addy 
    print(df)
    bucket = 'jcalkins-source'
    file_name = f'{zip_code}.csv'
    s3_client = boto3.client(
        "s3",
        aws_access_key_id = access_key_id,
        aws_secret_access_key = secret_access_key
    )
    with io.StringIO() as buffer:
        df.to_csv(buffer, index=False)
        response = s3_client.put_object(
            Bucket=bucket, Key=f'{zip_code}.csv', Body = buffer.getvalue()
        )
    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

    if status == 200:
        print(f"Successful S3 put_object response. Status - {status}")
    else:
        print(f"Unsuccessful S3 put_object response. Status - {status}")

#THIS FUNCTION NEEDS TO BE MODIFIED TO SEND A CSV TO S3 BUCKET 
# def to_s3(df, zc):
#     s3 = boto3.client('s3')
#     s3.upload_file(f"{zc}", "jcalkins-source", f"{df}")

def existence(zc):
    # engine = create_engine(f'postgresql://postgres:postgres@{db_endpoint}:5432/jcalkins-final-destination')
    # data = engine.execute(
    #     f"SELECT COUNT(*) FROM restaurants WHERE zip_code = '{zc}'"
    # )
    url = f"postgresql://postgres:postgres@{db_endpoint}:5432/postgres"
    engine = create_engine(url)
    connection = engine.connect()
    query= """SELECT COUNT(*) FROM  restaurants WHERE CAST(zip_code AS int) = 76065 """
    data = engine.execute(text(query)).fetchall()
    print(data)
    if data[0][0] > 0:
        return True
    elif data[0][0] == 0:
        return False
    