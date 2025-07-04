from fastapi import FastAPI 
from app.api.v1 import image_routes

app = FastAPI(
    title="Prompt2Media Backend",
    description="Generates Images and Videos from Prompts",
    version="0.1"
)

app.include_router(image_routes.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Prompt2Media Backend is running!"}