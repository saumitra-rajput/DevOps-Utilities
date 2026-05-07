import boto3
from datetime import datetime, timedelta, timezone


def get_bucket_info():
    connection = boto3.client("s3")
    s3 = connection.list_buckets()["Buckets"]
    current_date = datetime.now(timezone.utc).astimezone()

    new_buckets = []
    old_buckets = []

    for bucket in s3:
        bucket_name = bucket["Name"]
        creation_date = bucket["CreationDate"]
        days_ago_90 = current_date - timedelta(days=90)

        if creation_date < days_ago_90:
            old_buckets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)

    return {
            "Total_buckets": len(s3),
            "New_buckets": len(new_buckets),
            "Old_buckets": len(old_buckets),
            "New_buckets_name": new_buckets,
            "Old_buckets_name": old_buckets
            }


def get_ec2_info():
    client = boto3.client("ec2", region_name="us-east-2")

    response = client.describe_instances()
    
    ec2_ID = []
    instances = []
    ec2_state = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            ID = instance["InstanceId"]
            state = instance["State"]["Name"]
            
            # Improved Readability from GPT
            instances.append({
                        "InstanceId": instance.get("InstanceId"),
                        "State": instance.get("State", {}).get("Name"),
                        "InstanceType": instance.get("InstanceType"),
                        "PublicIP": instance.get("PublicIpAddress"),
                    })

            ec2_ID.append(ID)
            ec2_state.append(state)

    return {
            "Instances": instances,
            "Count": len(ec2_ID),
            "EC2_ID": ec2_ID,
            "EC2_state": ec2_state
            }

