from fastapi import FastAPI
from api import routers

app = FastAPI()

app.include_router(router=routers.router)