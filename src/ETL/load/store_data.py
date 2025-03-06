import pandas as pd
import boto3

def saveToCsv(df, filename):
    """
    Save a DataFrame to a CSV file.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        filename: (str): The path and name of the CSV file to save.
    """
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


def saveToJson(df, filename):
    """
    Save a DataFrame to a JSON file.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        filename: (str): The path and name of the JSON file to save.
    """
    df.to_json(filename, orient="records", lines=True)
    print(f"Data saved to {filename}")

def saveToS3(df, bucket_name, object_name, format='csv'):
    """
    Save the data as CSV and upload it to AWS S3 bucket.

    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        bucket_name: The name of the S3 bucket are going to be saved to.
        object_name: The name of the object of the CSV file in the bucket.
    """
    s3_client = boto3.client('s3')
    buffer = df.to_csv(index=False)
    s3_client.put_object(Bucket = bucket_name, Key = object_name, Body = buffer)
    print(f"Data saved to s3://{bucket_name}/{object_name}")


