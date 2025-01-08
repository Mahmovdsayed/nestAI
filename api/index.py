from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from meta_ai_api import MetaAI
import time

ai = MetaAI()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/send/")
async def send_prompt(message: str):
    try:
        start_time = time.time()
        response = await ai.prompt(message=message)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return {"status": "success", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the NEST.AI API"}
