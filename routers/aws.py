from fastapi import APIRouter, HTTPException
from services.aws_service import get_bucket_info, get_ec2_info

router = APIRouter()

@router.get("/s3",status_code=200)
def get_buckets():

    try:
        bucket_info = get_bucket_info()
        return bucket_info
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

@router.get("/ec2",status_code=200)
def get_ec2():

    try:
        ec2_info = get_ec2_info()
        return ec2_info
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
            )
