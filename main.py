from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
from src.app import run_pipeline as execute_pipeline



app = FastAPI(title="DE Assistant")

UPLOAD_DIR = Path("data/raw")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
ALLOWED_EXTENSIONS = {".csv", ".json"}

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Pipeline Investigator API is running"
    }

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print("upload was clicked")
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file provided."
        )
    extension=Path(file.filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only CSV and JSON files are supported."
        )
    contents = await file.read()
    if not contents:
        raise HTTPException(
                    status_code=400,
                    detail="no content in the file"
                )
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        print(file_path)
        buffer.write(contents)
    
    return {
        "status": "success",
        "filename": file.filename,
        "file_path":file_path,
        "message": "File uploaded successfully."
    }
@app.post('/run_pipeline')
async def run_pipeline(filename:str):
    print("enter this run route")
    print(filename)
    file_path = UPLOAD_DIR / filename
    print(file_path)
    if not file_path.is_file():
        raise HTTPException(
            status_code=404,
            detail=f"Uploaded file not found: {filename}"
        )
    else:
        try:
            result=execute_pipeline(file_path)
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    
    