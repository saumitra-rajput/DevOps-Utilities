# This script can perform Amazon s3 bucket resource listing, creation, deletion
# boto3 is using with client server 
# Requirement : AWS cli configured, AWS CLI access with the S3 permissions


import boto3

connection = boto3.client("s3")



# Example to get Bucket names

data = connection.list_buckets()
# print(type(data)) this return dict type

if data["Buckets"]:
    for bucket in data["Buckets"]:
        print(f"The Bucket name is: {bucket['Name']}")
else:
    print("Nothing to show: No bucket found.")


# Example to Create bucket

bucket_name = input("Enter the bucket Name: ").lower().strip()

if len(bucket_name) > 0:
    try:
        new_bucket = connection.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": "us-east-2"
             })
        print(f"Bucket created successfully:{bucket_name}")
    
    except Exception:
        print(f"Bucket already exists {bucket_name} or Error occured..")
else:
    print("Invalid input..")


# Example for delete amazon bucket

bucket_del = input("Enter the Bucket name to delete: ").lower().strip()

if bucket_del:
    try:
        # getting the all files and data of bucket

        buck_data = connection.list_objects_v2(Bucket=bucket_del)

        # check and del any files
        
        if "Contents" in buck_data:
            for files in buck_data["Contents"]:
                connection.delete_object(Bucket=bucket_del, Key=files["Key"])
        
        # delete the bucket

        connection.delete_bucket(Bucket=bucket_del)
        print(f"Bucket Deleted: {bucket_del}")

    except Exception:
        print("Error occured")
else:
    print("Invalid Input.")

