# from langchain_openai import ChatOpenAI
# from langchain_core import prompts
# from langchain_core.prompts import PromptTemplate
# from PIL import Image
# import base64
# import numpy as np
import openai
from core.utils import extract_json
import json

def Call_Analyst_GPT(url, api_key):
    openai.api_key = api_key
    
    prompt = '''
        다음 이력서를 분석해서 분석한 결과를 JSON 형식으로
        
        {
            "이름": type = str
            "전공": type = list(str)
            "직무경험": type = list(str)
            "기타": type = list(str)
        }
        으로 정리해 이때 JSON만 출력해
        '''
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages = [
                {
                    "role": "system",
                    "content": "너는 면접관이야"
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url" : f"{url}"}}
                    ]
                }
            ]
        )
        print(extract_json(response.choices[0].message.content))
        
        answer = json.loads(extract_json(response.choices[0].message.content))
        
        return answer

    except Exception as e:
        print(f"Error occurred in Call_Analyst_GPT: {e}")
        return None

def Call_Interview_GPT(reference_data, job_objective, api_key):
    openai.api_key = api_key
    
    data_prompt = f'''
    면접 질문 생성 참고용 데이터: \n{str(reference_data)}\n\n
    위 json 데이터를 참고해서,
    지원 직무 \n{job_objective}\n 에 대해
    약 20개 정도의 면접 질문을 Json 형식으로
    '''
    
    question_prompt = '''
    {
        "직무질문": type = list(str),
        "인성질문": type = list(str),
        "기술질문": type = list(str)
    }
    
    으로 직무 질문 5개, 인성 질문 5개, 기술 질문 10개로 정리해서 Json만 출력해'''
    
    prompt = data_prompt + question_prompt
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages = [
                {
                    "role": "system",
                    "content": "너는 면접관이야"
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                    ]
                }
            ]
        )
        print(extract_json(response.choices[0].message.content))
        
        answer = json.loads(extract_json(response.choices[0].message.content))
        
        return answer

    except Exception as e:
        print(f"Error occurred in Call_Interview_GPT: {e}")
        return None

def Call_Follow_Interview_GPT(reference_data, job_objective, ord_question, ord_answer, api_key):
    openai.api_key = api_key
    
    data_prompt = f'''
    면접 질문 생성 참고용 데이터: \n{str(reference_data)}\n\n
    지원 직무: \n{job_objective}\n
    이전 면접 질문: \n{ord_question}\n
    이전 면접 답변: \n{ord_answer}\n
    위 json 데이터를 참고해서,
    이전 면접 답변과 연관된 꼬리 질문(follow_question)을 Json 형식으로
    '''

    question_prompt = '''
    {
        "follow_question": type = str
    }
    
    으로 꼬리 질문 1개를 Json만 출력해'''

    prompt = data_prompt + question_prompt
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages = [
                {
                    "role": "system",
                    "content": "너는 면접관이야"
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                    ]
                }
            ]
        )
        print(extract_json(response.choices[0].message.content))
        
        answer = json.loads(extract_json(response.choices[0].message.content))
        
        return answer

    except Exception as e:
        print(f"Error occurred in Call_Follow_Interview_GPT: {e}")
        return None
    
def Call_Interview_Feedback_GPT(reference_data, job_objective, ord_question, ord_answer, api_key): # 피드백 프롬프트 개선 필요
    openai.api_key = api_key
    
    data_prompt = f'''
    면접 질문 생성 참고용 데이터: \n{str(reference_data)}\n\n
    지원 직무: \n{job_objective}\n
    면접 질문: \n{ord_question}\n
    면접 답변: \n{ord_answer}\n
    위 json 데이터를 참고해서,
    이전 면접 답변에 대한 피드백과 예시 답변을 Json 형식으로
    '''

    question_prompt = '''
    {
        "feedback": type = str
        "example_answer" : type = str
    }
    
    으로 피드백 1개를 Json만 출력해'''

    prompt = data_prompt + question_prompt
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages = [
                {
                    "role": "system",
                    "content": "너는 면접관이야"
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                    ]
                }
            ]
        )
        print(extract_json(response.choices[0].message.content))
        
        answer = json.loads(extract_json(response.choices[0].message.content))
        
        return answer

    except Exception as e:
        print(f"Error occurred in Call_Interview_Feedback_GPT: {e}")
        return None
    