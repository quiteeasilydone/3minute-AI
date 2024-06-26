from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, HTTPException, Depends, File, UploadFile
# from schemas import response_body
import json

router = APIRouter()
memory_storage = {}

@router.post("/api/upload")
async def upload(file:UploadFile=File(), memory_storage = memory_storage):
    memory_storage = {}
    content = await file.read()
    memory_storage[file.filename] = content
    print(len(memory_storage.keys()))
    return JSONResponse(content={"filename": file.filename})

@router.post("api/portfolio-analysis")
async def asdk(filename):
    content = memory_storage[filename].pop()
    return