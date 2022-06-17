import unittest
import boto3
import funcs
from funcs import *

class testing_to_csv_s3(unittest.TestCase):
    def test_to_csv_s3(self):
        s3 = boto3.resource(
            "s3",
            aws_access_key_id = access_key_id,
            aws_secret_access_key = secret_access_key
        )
        bucket = s3.Bucket('jcalkins-source')

        if bucket.creation_date:
            result = print("The bucket exists")
        self.assertEqual(result)


class testing_destination_bucket(unittest.TestCase):
    def test_destination_bucket(self):
        s3 = boto3.resource(
            "s3",
            aws_access_key_id = access_key_id,
            aws_secret_access_key = secret_access_key
        )
        bucket = s3.Bucket('jcalkins-temp-dest')

        if bucket.creation_date:
            result = print("The bucket exists")
            self.assertEqual(result)
        else:
            self.fail("could not reach destination bucket")


# status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

    # if status == 200:
    #     print(f"Successful S3 put_object response. Status - {status}")
    # else:
    #     print(f"Unsuccessful S3 put_object response. Status - {status}")