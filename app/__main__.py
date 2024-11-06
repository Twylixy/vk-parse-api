from fastapi import FastAPI
from app.routers import app_router

app = FastAPI()
app.include_router(app_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.__main__:app", reload=True)
