from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.api import fireballs, cad

app = FastAPI(title="NASA ETL Project API")

# Authorize request for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In prod, replace by the real frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API NASA ETL Project is running"}

# Include of router for fireballs
app.include_router(fireballs.router, prefix="/api/fireballs", tags=["Fireballs"])

# Include router for CAD
app.include_router(cad.router, prefix="/api/cad", tags=["CAD"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
