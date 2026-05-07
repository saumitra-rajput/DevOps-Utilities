from fastapi import FastAPI
from routers import metrics, aws

app = FastAPI(
        title="This is my First FastAPI",
        description="This API will return DevOps Utilities",
        version="1.0.0",
        doc_url="/docs",
        redoc_url="/redoc"
        )

@app.get("/")
def greet():
    """
    This is a greet API, For testing purpose.
    """
    return {"message": "Hello, I am DevOps Engineer",
            "Name":"Saumitra Rajput"
            }

@app.get("/health")
def health():
    return {
            "status": "healthy"
            }

app.include_router(metrics.router)

app.include_router(aws.router, prefix="/aws")
