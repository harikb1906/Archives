#!/usr/bin/python
"""Usage: Add bucket name and credentials
          script.py <source folder> <s3 destination folder >"""

import os
from sys import argv
import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = ''
SECRET_KEY = ''
host = ''
bucket_name = ''

local_folder, s3_folder = argv[1:3]
walks = os.walk(local_folder)
# Function to upload to s3
def upload_to_aws(bucket, local_file, s3_file):
    """local_file, s3_file can be paths"""
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    print('  Uploading ' +local_file + ' as ' + bucket + '/' +s3_file)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print('  '+s3_file + ": Upload Successful")
        print('  ---------')
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False

"""For file names"""
for source, dirs, files in walks:
    print('Directory: ' + source)
    for filename in files:
        # construct the full local path
        local_file = os.path.join(source, filename)
        # construct the full Dropbox path
        relative_path = os.path.relpath(local_file, local_folder)
        s3_file = os.path.join(s3_folder, relative_path)
        # Invoke upload function
        upload_to_aws(bucket_name, local_file, s3_file)
