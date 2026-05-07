from services.metrics_service import sys_metrics
from fastapi import APIRouter

router = APIRouter() # creating object for APIrouter class


@router.get("/metrics",status_code=200)

def get_metrics():
    
    try:
        metrics = sys_metrics()
        return metrics
    except:
        raise HTTPException(
                status_code=500,
                detail="Internal Server Error"
                )




