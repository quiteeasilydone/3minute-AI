from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, HTTPException, Depends, File, UploadFile
# from schemas import response_body
import json, os, time
import boto3
from db.storage_setting import load_s3_client
from core.prompt_engine import *
from core.utils import *
from urllib.parse import unquote
import asyncio
import random
from schemas import question_model

router = APIRouter()
env_file_path = "env.json"

@router.post("/api/question/follow-question")
async def get_follow_question(request: question_model.followQuestionRequest): # 꼬리 질문 존재하면 꼬리 질문을 return, 존재하지 않으면 0 return
    # jSON 형태의 Body가 들어오면 거기에 추가해서 GPT Call
    # 면접 질문 생성 참고용 데이터: reference_data
    # 원래 질문: ord_question
    # 원래 답변: ord_answer
    data = request.dict()

    api_key = data['apiKey']

    job_objective = data['job']
    reference_data = {
        "이름": data['name'],
        "전공": data['major'],
        "직무경험": data['project'],
        "기타": data['special']
    }
    # ord_question_id: 10진수 숫자 3자리,
    # {MSD: 질문 성격    , 질문 성격: "직무 기반 질문" = 1, "인성 질문": = 2, "기술질문": = 3
    #  중간: 처음에 생성한 질문 번호
    # 마지막: 꼬리질문 번호}
    # ex) 직무 기반 질문인데 처음 생성한 질문 이라면 110 ( 꼬리질문이 아니고 처음 생성한 거면 LSB가 0)
    # ex) 직무 기반 질문인데 처음 생성한 질문에 대한 첫 꼬리 질문이라면 111
    # ex) 인성 질문인데 처음 생성한 질문 중 세 번째 질문에 대한 두 번째 꼬리 질문이라면 232

    ord_question = data['question']
    ord_answer = data['answer']

    try:
        nxt_question = Call_Follow_Interview_GPT(reference_data, job_objective, ord_question, ord_answer, api_key)

        return JSONResponse(content = nxt_question)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/question/feedback")
async def get_question_feedback(request: question_model.followQuestionRequest): # 질문에 대한 피드백을 저장, /api/question/follow-question가 요구하는 body에서 ord_question_id필드가 추가적으로 필요
    data = request.dict()

    default_content = {
        "feedback" : "피드백 할 것 없이 더할 나위 없는 훌륭한 답변입니다.",
        "example_answer" : ""
    }
    
    api_key = data['apiKey']

    job_objective = data['job']
    reference_data = {
        "이름": data['name'],
        "전공": data['major'],
        "직무경험": data['project'],
        "기타": data['special']
    }
    ord_question = data['question']
    ord_answer = data['answer']
    

    try:
        feedback = Call_Interview_Feedback_GPT(reference_data, job_objective, ord_question, ord_answer, api_key)

        print(feedback)
        under_threshold = threshold_check(calculate_similarity(feedback["example_answer"], ord_answer), 0.9)
        print(f'under_threshold: {under_threshold}')
        
        if under_threshold:
            return JSONResponse(content = feedback)
        else:
            return JSONResponse(content = default_content)
            


        # 이전 답변과 피드백


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
