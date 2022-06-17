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
from config import gkey, dbendpoint
from pprint import pprint

#this is grabbing the restaurants from the zipcode we were given from the user. the zipcode is transformed into lat and long coordinates for the google api
def get_restaurants(zc):
    rest_names = []
    rest_addys = []
    #here i am getting the latitude and the longitude for the zipcode the user enters
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={zc}&sensor=true&key={gkey}"
    response = requests.get(url).json()
    lat = response['results'][0]['geometry']['location']['lat']
    lng = response['results'][0]['geometry']['location']['lng']
    #with that info we can go ahead and grab the restaurants from that zipcode within a 10 mile radius set to 16100 meters wich is a little over 10 miles
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

### here we are using pandas to print a sample from the dataframe (a sample print only one random row from the dataframe)
def random_from_df(df):
    pprint(df.sample())
    
# functions for category specific feature
def get_category():
    user_cat =input("What cotegory are we feeling today?: ")
    return user_cat

def get_category_restaurants(user_cat, zc):
    rest_names = []
    rest_addys = []
    #here i am getting the latitude and the longitude for the #zipcode the user enters
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={zc}&sensor=true&key={gkey}"
    response = requests.get(url).json()
    lat = response['results'][0]['geometry']['location']['lat']
    lng = response['results'][0]['geometry']['location']['lng']
    #with that info we can go ahead and grab the restaurants from #that zipcode within a 10 mile radius set to 16100 wich is a #little over 10 miles
    search_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=10500&keyword={user_cat}&key={gkey}"
    search = requests.get(search_url).json()
    for x in range(len(search['results'])-1):
        rest_names.append(search['results'][x]['name'])
        rest_addys.append(search['results'][x]['vicinity'])
    return rest_names, rest_addys