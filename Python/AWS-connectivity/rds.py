import boto3
from helper import *

def stop_instance():
    client = boto3.client('rds')
    dbs = client.describe_db_instances()
    bprint(dbs)

if __name__ == "__main__":
    stop_instance()