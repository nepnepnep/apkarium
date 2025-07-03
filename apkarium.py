from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os

API_TOKEN = os.getenv("API_TOKEN", "mysecrettoken_87236853")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()


def check_token(token: str):
    if token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.post("/upload/")
async def upload_apk(token: str, file: UploadFile = File(...)):
    check_token(token)
    if not file.filename.endswith(".apk"):
        raise HTTPException(status_code=400, detail="Only .apk files allowed")
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename}


@app.get("/list/")
def list_apks(token: str):
    check_token(token)
    files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(".apk")]
    return {"files": files}


@app.get("/download/{filename}")
def download_apk(filename: str, token: str):
    check_token(token)
    filepath = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(filepath, media_type='application/vnd.android.package-archive')