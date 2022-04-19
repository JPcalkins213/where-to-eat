import csv
from http import client
from sys import prefix
import config
import string
import requests
import pandas as pd
import numpy as np
import boto3
import io
import pprint
from pprint import pprint
from botocore.errorfactory import ClientError
from io import StringIO
from sqlalchemy import create_engine, text
from config import gkey, access_key_id, secret_access_key
from pprint import pprint

#this is grabbing the restaurants from the zipcode we were given from the user. the zipcode is transformed into lat and long coordinates for the google api
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

#asking for the zipcode from the user and sending it to the above function 
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

#this is grabbing the datafram we made turning it to a csv and sending it to an s3 bucket where it will be cleaned
def to_csv_s3(name, addy, zip_code):

    zip_array = []
    for x in range(len(name)):
        zip_array.append(zip_code)
    df = pd.DataFrame()
    df['zip_code'] = zip_array
    df['name'] = name
    df['address'] = addy 
    # print(df)
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
    # status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

    # if status == 200:
    #     print(f"Successful S3 put_object response. Status - {status}")
    # else:
    #     print(f"Unsuccessful S3 put_object response. Status - {status}")

#this has been the trickest function so far. were checking the landing s3 bucket so see if the file name with the zipcode given exists. I cant count how many times ive had to change the process of this function alone
def existence(zc):
    import boto3
    bucket='jcalkins-temp-dest'
    file_key = f'{zc}.csv'
    s3_client = boto3.client('s3', 
    aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
    result = s3_client.list_objects_v2(Bucket=bucket, Prefix=file_key)
    if 'Contents' in result:
        return True
    else:
        return False
    
### since we know the file exists, now we get the existing csv from the s3 bucket and convert it to a df
def csv_to_df(zc):
    s3_client = boto3.client('s3', 
    aws_access_key_id=access_key_id, 
    aws_secret_access_key=secret_access_key)
    bucket='jcalkins-temp-dest'
    file_key = f'{zc}.csv'
    response = s3_client.get_object(Bucket = bucket, Key = file_key)
    df = pd.read_csv(response.get("Body"))
    return df

### here we are using pandas to print a sample from the dataframe (a sample print only one random row from the dataframe)
def random_from_df(df):
    pprint(df.sample())

    ### for clarity; the code below is for the original way i planned for this application to be. originally it was to send the data i get into a csv and send that csv to aws rds. 
    # engine = create_engine(f'postgresql://postgres:postgres@{db_endpoint}:5432/jcalkins-final-destination')
    # data = engine.execute(
    #     f"SELECT COUNT(*) FROM restaurants WHERE zip_code = '{zc}'"
    # )
    # url = f"postgresql://postgres:postgres@{db_endpoint}:5432/postgres"
    # engine = create_engine(url)
    # connection = engine.connect()
    # query= """SELECT COUNT(*) FROM  restaurants WHERE CAST(zip_code AS int) = 76065 """
    # data = engine.execute(text(query)).fetchall()
    # print(data)
    # if data[0][0] > 0:
    #     return True
    # elif data[0][0] == 0:
    #     return False
    