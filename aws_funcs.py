import io
from config import *
import sqlalchemy
from sqlalchemy import create_engine, text
import pandas as pd
import boto3

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

#this has been the trickest function so far. were checking the landing s3 bucket so see if the file name with the zipcode given exists. I cant count how many times ive had to change the process of this function alone
def aws_existence(zc):
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

