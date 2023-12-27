# boto3 -- pip install boto3

import boto3

s3_client = boto3.client('s3', aws_access_key_id='AKIAS3LJHOT555KCW2NV', aws_secret_access_key='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')


# print(s3_client)

# print(dir(s3_client))

# bucket_creation = s3_client.create_bucket(Bucket='python8amdec')

# print(bucket_creation)

# for ele in ['functions.py','inbuilt.py','caluclator.py']:
#     s3_client.upload_file(ele, 'python8amdec',ele)
    
# list of buckets in s3

# bucket_list = [ele['Name'] for ele in s3_client.list_buckets()['Buckets']]
# print("Existing buckets:", bucket_list)

# buck_name=input('enter the bucket name')

# if buck_name in bucket_list:
    # print('bucket alredy exists')
# else:
    # create_bucket= s3_client.create_bucket(Bucket=buck_name)


# print(s3_client.list_objects(Bucket='python8amdec')['Contents'])
# print(s3_client.list_objects(Bucket='python8amdec')['Contents'])

# file_list =[ele['Key'] for ele in s3_client.list_objects(Bucket='python8amdec')['Contents']]

# print(file_list)

# s3_client.download_file('python8amdec','functions.py','C:/Users/DoradlaHari/Downloads/downloaded_from_python.py')

# delete object 
# for ele in file_list:
    # s3_client.delete_object(Bucket='python8amdec',Key=ele)


s3_client.delete_bucket(Bucket='python8amdec')