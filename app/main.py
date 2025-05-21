# Entry point for FastAPI application

from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'SmartAeroAI API running'}
