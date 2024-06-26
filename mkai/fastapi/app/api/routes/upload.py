from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, HTTPException, Depends, File, UploadFile
# from schemas import response_body
import json, os
import boto3
from db.storage_setting import load_s3_client

router = APIRouter()
memory_storage = {}
env_file_path = "env.json"

@router.post("/api/upload")
async def upload(file:UploadFile=File(), memory_storage = memory_storage):
    # S3 객체이름이 정의되지 않으면, file_name을 사용
    content = await file.read()
    object_name = os.path.basename(file.filename)
    aws_s3_client, AWS_BUCKET_NAME = load_s3_client(env_file_path)

    print(AWS_BUCKET_NAME)

    # S3에 파일 업로드
    aws_s3_client.upload_fileobj(file.file, AWS_BUCKET_NAME, object_name)

    memory_storage[file.filename] = os.path.join(AWS_BUCKET_NAME, object_name)
    
    print(len(memory_storage.keys()))

    return JSONResponse(content={"filename": file.filename})

@router.post("api/portfolio-analysis")
async def asdk(filename):
    # S3에 업로드된 이력서 받아오게 구현
    try:
        content = memory_storage[filename].pop()
        return
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


