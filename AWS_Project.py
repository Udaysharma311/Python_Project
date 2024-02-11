def show_buckets(S3_object):
    for bucket in S3_object.buckets.all():
        print(bucket.name)
        
        
        
def upload_file(s3_object, bucket_name, file_path, key_name,):
    try:
        file_data = open(file_path, 'rb')
        s3_object.Bucket(bucket_name).put_object(key=key_name, body=file_data)
        file_data.close()
    except:
        print("File uploaded successfully")
        
def list_name(s3_object, bucket_name):
    for obj in s3_object.Bucket(bucket_name).objects.all():
        print(obj.key)
        
def create_bucket(s3_object, bucket_name):
    try:
        s3_object.create_bucket(bucket = bucket_name,create_bucket_configuration={'LocationConstraint': 'ap-south-1'})
    except:
        print(f"{bucket_name} is created successfully")
