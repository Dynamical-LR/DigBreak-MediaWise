from fastapi import FastAPI
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv('./pred.csv')

@app.get("/")
async def home():
   return {"data": "Hello World"}

@app.get('/sales')
async def sales():
   return {'labels': list(df['week'].values), 'values': list(df['pred'].values)}