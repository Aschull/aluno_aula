from fastapi import FastAPI
from app.configs.db.sqlite import Base, engine

from app.routers import health, student

app = FastAPI()

Base.metadata.create_all(engine)


app.include_router(health.router)
app.include_router(student.router)
