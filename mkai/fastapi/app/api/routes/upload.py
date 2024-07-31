from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, HTTPException, Depends, File, UploadFile
# from schemas import response_body
import json, os, time
import boto3
from db.storage_setting import load_s3_client
from core.prompt_engine import *
from urllib.parse import unquote
import asyncio

router = APIRouter()
memory_storage = {} # {key: file name, value: file url in S3}
env_file_path = "env.json"
lock = asyncio.Lock()

async def schedule_deletion(key, file_url, aws_s3_client, AWS_BUCKET_NAME):
    await asyncio.sleep(300)  # 5분 대기 (300초)
    async with lock: # memory_storage에 대한 Lock 생성
        if key in memory_storage:
            del memory_storage[key]
            # S3에서 파일 삭제
            object_name = os.path.basename(file_url)
            aws_s3_client.delete_object(Bucket=AWS_BUCKET_NAME, Key=object_name)
            print(f"Deleted {key} from memory_storage and {object_name} from S3")

@router.post("/api/upload")
async def upload(file:UploadFile=File()):
    # S3 객체이름이 정의되지 않으면, file_name을 사용
    try:
        # 업로드된 파일의 URL 생성 - UNIXTIME 참고
        file_url_time = str(int(time.time()))

        content = file.file.read()

        file.file.seek(0)
        object_name = os.path.basename(file_url_time) + '.jpg'
        aws_s3_client, AWS_BUCKET_NAME = load_s3_client(env_file_path)

        # S3에 파일 업로드
        aws_s3_client.upload_fileobj(file.file, AWS_BUCKET_NAME, object_name)
        AWS_RESION = "ap-northeast-2"
        # 업로드된 파일의 URL 생성 - AWS S3 객체 URL은 일반적으로 다음과 같은 형식을 가집니다: https://{bucket_name}.s3.amazonaws.com/{object_name}
        file_url = f"https://{AWS_BUCKET_NAME}.s3.{AWS_RESION}.amazonaws.com/{object_name}"

        async with lock:
            memory_storage[file.filename] = file_url
            print(memory_storage)
        
        asyncio.create_task(schedule_deletion(file.filename, file_url, aws_s3_client, AWS_BUCKET_NAME))

        return JSONResponse(content={"filename": file.filename})
    finally:
        file.file.close()

@router.get("/api/memory-storage")
async def get_memory_storage():
    return JSONResponse(content=memory_storage)

@router.get("/api/portfolio-analysis")
async def asdk(request: Request):
    # S3에 업로드된 이력서 받아오게 구현
    filename = request.query_params.get("filename")
    api_key = request.query_params.get("apiKey")
    
    if not filename:
        raise HTTPException(status_code=400, detail="Filename query parameter is required")
    decoded_filename = unquote(filename)
    
    try:
        file_url_in_s3 = memory_storage[str(decoded_filename)]
        print(f"file_url_in_s3: {file_url_in_s3}")

        response = Call_Analyst_GPT(file_url_in_s3, api_key)

        return JSONResponse(content = response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/generate-interview-question")
async def get_interview_question(request: Request):
    
    # print(request.name)
    
    data = await request.json()
    
    api_key = data['apiKey']

    job_objective = data['job']
    reference_data = {
        "이름": data['name'],
        "전공": data['major'],
        "직무경험": data['project'],
        "기타": data['special']
    }
    
    print(job_objective, reference_data)
    
    try:
        response = Call_Interview_GPT(reference_data, job_objective, api_key)

        return JSONResponse(content = response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/upload/all")
async def upload_S3_all_info(request: Request):
    try:
        data = await request.json()

        # 업로드된 파일의 URL 생성 - UNIXTIME 참고
        file_url_time = str(int(time.time()))
        
        
        object_name = 'all_info'
        aws_s3_client, AWS_BUCKET_NAME = load_s3_client(env_file_path)

        # S3에 파일 업로드
        aws_s3_client.upload_fileobj(data, AWS_BUCKET_NAME, object_name)
        AWS_RESION = "ap-northeast-2"
        # 업로드된 파일의 URL 생성 - AWS S3 객체 URL은 일반적으로 다음과 같은 형식을 가집니다: https://{bucket_name}.s3.amazonaws.com/{object_name}
        file_url = f"https://{AWS_BUCKET_NAME}.s3.{AWS_RESION}.amazonaws.com/{object_name}"

        return JSONResponse(content={"object_name": object_name})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))