from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, HTTPException, Depends, File, UploadFile
# from schemas import response_body
import json

router = APIRouter()
memory_storage = {}

@router.post("/api/upload")
async def upload(file:UploadFile=File()):
    content = await file.read()
    memory_storage[file.filename] = content
    return JSONResponse(content={"filename": file.filename})