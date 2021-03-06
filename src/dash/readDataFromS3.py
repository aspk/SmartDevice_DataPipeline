import boto3
import pandas as pd

#low-level functional API
client = boto3.client('s3')

#high-level object-oriented API
resource = boto3.resource('s3')

#object of your s3 bucket
my_bucket = resource.Bucket('anshu-insight')

with open('uploadedFromS3.csv', 'w') as out_file:
    for obj in my_bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read()
        out_file.write(str(body))
        out_file.write('\n')

