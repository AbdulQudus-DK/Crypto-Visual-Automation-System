# main.py
from fastapi import FastAPI
from scheduler import start_scheduler

app = FastAPI(title="Crypto Visual Automation")

@app.on_event("startup")
def startup_event():
    start_scheduler()
    print("✅ Scheduler started.")

@app.get("/")
def home():
    return {"status": "running", "message": "Crypto Visual Automation active"}
