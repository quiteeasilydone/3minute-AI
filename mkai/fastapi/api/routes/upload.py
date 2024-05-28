from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, HTTPException, Depends
# from schemas import response_body
import json

router = APIRouter()

@router.post("/api/upload/")
async def upload(request: Request):
    data = await request.json()
    print(data)
    return {"filename": data}
# @router.post('/api')
# async def hi(asd):
#     return asd