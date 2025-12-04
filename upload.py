from fastapi import APIRouter, File, UploadFile
router = APIRouter()
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return{"filename": file.filename, "content_type":file.content_type, "size": len(contents)}