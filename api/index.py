from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from meta_ai_api import MetaAI

ai = MetaAI()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

class PromptRequest(BaseModel):
    message: str

@app.post("/send/")
async def send_prompt(request: PromptRequest):
    try:
        response = ai.prompt(message=request.message)
        return {"status": "success", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the NEST.AI API"}
