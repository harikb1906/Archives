import boto3
import json


def bprint(*content):
    print(json.dumps(content, indent=4, default=str))


def connect_cognito(NextToken=None, MaxResults=60):
    client = boto3.client('cognito-idp')
    bprint(client.list_user_pools(MaxResults=MaxResults))


def connect_s3():
    client = boto3.client('s3')
    bprint(client.list_buckets())


def connect_dynamodb(table="micrologx-restaurant-infra-demo-stack-dynamodb-table"):
    client = boto3.client('dynamodb')
    bprint(client.scan(TableName=table, Limit=3))


def connect_psql(db="dbecho"):
    import psycopg2
    conn = psycopg2.connect(
        database=db,
        user='django_default_user',
        password="abc123#",
        host="127.0.0.1",
        port=5432
    )
    print("Opened database successfully:\n" +str(conn))


def retrieve_secret(key):
    client = boto3.client("secretsmanager")
    secret = client.get_secret_value(SecretId=key)
    secret_string = json.loads(secret["SecretString"])
    username = secret_string["username"]
    password = secret_string["password"]
    return username, password


def main():
    from sys import argv
    service = argv[1]
    service_fn = eval("connect_" + service)
    service_fn()

if __name__ == "__main__":
    # connect_cognito()
    # connect_s3()
    # connect_dynamodb()
    # connect_psql()
    bprint(retrieve_secret('micrologx-demo-AuroraUser'))
