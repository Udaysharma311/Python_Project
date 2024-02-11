import boto3
from aws import show_buckets, upload_file,list_name,create_bucket
s3_object = boto3.resource('s3')
file_path = 'mytextupload.txt'
show_buckets(s3_object)
#upload_file(s3_object, 'pythondevopswithuday', file_path, 'mytextupload.txt')
list_name(s3_object,'pythondevopswithuday')
create_bucket(s3_object , 'pythfordevopswithudaysharma')
