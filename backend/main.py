#placeholder
from fastapi import FastAPI
from routers.upload import router as upload_file
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/")
def root():
    return {"message": "hello"}
app.include_router(upload_file, prefix="/api")
