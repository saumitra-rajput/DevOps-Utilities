# DevOps Utilities API

A FastAPI-based REST API that exposes DevOps utility endpoints for system metrics monitoring and AWS resource information.

---

## Project Structure

```
DevOps-Utilities/
├── app/
│   └── api.py              # FastAPI app definition & route registration
├── images/
│   └── image               # Image Handling 
├── resources/
│   └── bucket.py           # Amazon S3 operation create,list,delete  OPTIONAL
├── routers/
│   ├── metrics.py          # System metrics router
│   └── aws.py              # AWS resources router
├── services/
│   ├── metrics_service.py  # psutil-based system metrics logic
│   └── aws_service.py      # boto3-based AWS S3 & EC2 logic
├── main.py                 # Application entry point (uvicorn)
└── requirements.txt        # Python dependencies
```

---

## Prerequisites

- Python 3.8+
- AWS CLI configured with appropriate access (see [AWS Setup](#aws-setup) below)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/DevOps-Utilities.git
cd DevOps-Utilities
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

```bash
source venv/bin/activate
```

> On Windows, use: `venv\Scripts\activate`

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python3 main.py
```

The server will start at `http://0.0.0.0:8080` with hot-reload enabled.

---

## API Endpoints

| Method | Endpoint    | Description                          |
|--------|-------------|--------------------------------------|
| GET    | `/`         | Greet endpoint (health check)        |
| GET    | `/health`   | Returns API health status            |
| GET    | `/metrics`  | Returns CPU, Disk & Memory usage     |
| GET    | `/aws/s3`   | Lists S3 buckets (new vs old)        |
| GET    | `/aws/ec2`  | Lists EC2 instances and their states |

### Interactive API Docs

Once the server is running, visit:

- **Swagger UI:** [http://localhost:8080/docs](http://localhost:8080/docs)

![alt text](/images/image-1.png)

- **ReDoc:** [http://localhost:8080/redoc](http://localhost:8080/redoc)

![alt text](/images/image.png)
---

## AWS Setup

Before using the `/aws/s3` or `/aws/ec2` endpoints, make sure:

1. **AWS CLI is installed and configured:**

```bash
aws configure
```

You'll be prompted to enter:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., `us-east-2`)
- Output format (e.g., `json`)

2. **Your IAM user/role has the following permissions:**
   - `s3:ListAllMyBuckets` — for the S3 endpoint
   - `ec2:DescribeInstances` — for the EC2 endpoint

> The EC2 service queries the `us-east-2` region by default. Update `services/aws_service.py` if you need a different region.

---

## Dependencies

| Package   | Purpose                          |
|-----------|----------------------------------|
| `fastapi` | Web framework for building APIs  |
| `uvicorn` | ASGI server to run the app       |
| `psutil`  | System metrics (CPU, disk, RAM)  |
| `boto3`   | AWS SDK for Python               |

---

## Notes

- The `/metrics` endpoint marks the service as **"Service not Healthy"** if CPU usage exceeds **10%**. Adjust the `threshold` value in `services/metrics_service.py` as needed.
- The `/aws/s3` endpoint classifies buckets as **new** (created within the last 90 days) or **old** (older than 90 days).

![alt text](/images/image-2.png)
