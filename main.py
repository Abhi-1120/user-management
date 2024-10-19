import uvicorn
from app import app

if __name__ == "__main__":
    try:
        uvicorn.run(
            app="app:app",
            reload=True if app.config.ENVIRONMENT != "production" else False,
            host="0.0.0.0",
            port=app.config.PORT
        )
    except Exception as e:
        print(f"Server exit with exception {e}")
