from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.core.db import create_tables
from backend.api.routers.patient import patient_router
from backend.api.routers.doctor import doctor_router
from backend.api.routers.appointment import appointment_router


@asynccontextmanager
async def lifespan(app: FastAPI): # noqa
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get('/')
async def main():
    return 'Heartbeat'

app.include_router(patient_router, prefix='/patient')
app.include_router(doctor_router, prefix='/doctor')
app.include_router(appointment_router, prefix='/appointment')
