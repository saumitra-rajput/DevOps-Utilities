# Application Entry point

from app.api import app
import uvicorn

if __name__ == "__main__":
    
    # ASGI web server - Asynchronous Server Gateway Interface)
    uvicorn.run(
            "app.api:app",
            host="0.0.0.0",
            port=8080,
            reload=True
            )
