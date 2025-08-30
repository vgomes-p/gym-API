from fastapi import FastAPI
from fastapi_pagination import add_pagination
from athletes.routes import router as athletes_router
from measurements.routes import router as measurements_router
from routines.routes import router as routines_router

app = FastAPI(title="Gym Workout API")

app.include_router(athletes_router)
app.include_router(measurements_router)
app.include_router(routines_router)

add_pagination(app)

@app.get("/")
def read_root():
    return {"message": "Gym Workout API is running!"}