from pydantic import BaseModel
from typing import List, Optional


# 꼬리 질문 api 요청 데이터 모델
class followQuestionRequest(BaseModel):
    job: str
    name: str
    major: str
    project: str
    special: str
    question: str
    answer: str
    apiKey: str

# # 피드백 api 요청 데이터 모델
# class feedbackRequest(followQuestionRequest):
