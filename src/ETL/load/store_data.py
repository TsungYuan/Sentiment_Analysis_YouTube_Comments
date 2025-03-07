import pandas as pd
import boto3
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def saveToCsv(df, filename):
    """
    Save a DataFrame to a CSV file.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        filename: (str): The path and name of the CSV file to save.
    """
    try:
        df.to_csv(filename, index=False)
        logger.info(f"Data save as {filename}.")
    except Exception as e:
        logger.error(f"Failed to the data: {str(e)}")


def saveToJson(df, filename):
    """
    Save a DataFrame to a JSON file.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        filename: (str): The path and name of the JSON file to save.
    """
    try:
        df.to_json(filename, orient="records", lines=True)
        logger.info(f"Data save as {filename}.")
    except Exception as e:
        logger.error(f"Failed to the data: {str(e)}")


def saveToS3(df, bucket_name, object_name, format='csv'):
    """
    Save the data as CSV and upload it to AWS S3 bucket.

    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        bucket_name: The name of the S3 bucket are going to be saved to.
        object_name: The name of the object of the CSV file in the bucket.
    """
    try:
        s3_client = boto3.client('s3')
        buffer = df.to_csv(index=False)
        s3_client.put_object(Bucket = bucket_name, Key = object_name, Body = buffer)

        logger.info(f"Data saved to s3://{bucket_name}/{object_name}")
    except Exception as e:
        print(f"Failed to save to S3: {e}")




