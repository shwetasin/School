
from app.leadmgmt.test import post_route

import uvicorn
from fastapi import FastAPI
from app.config import app_config



app = FastAPI()
   

# app=FastAPI()
app.include_router(post_route)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
