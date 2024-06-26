# from langchain_openai import ChatOpenAI
# from langchain_core import prompts
# from langchain_core.prompts import PromptTemplate
# from PIL import Image
# import base64
# import numpy as np
import numpy as np
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "이 이력서를 분석해서 이름, 전공, 프로젝트 경험, 기타 순으로 정리해줘"},
                {"type": "image_url", "image_url": {
                    "url": "https://3miniute-mkai-portfolio-bucket.s3.ap-northeast-2.amazonaws.com/%EC%9D%B4%EB%A0%A5%EC%84%9C001.jpg"
                }}
            ]
        }
    ]
)
# def encode_img_to_base64(image_path):
#     with open(image_path, "rb") as img_file:
#         base64_encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
#     return base64_encoded_image

# input_img = Image.open("./이력서001.jpg")

# llm = ChatOpenAI(model='gpt-4-vision-preview')
# answer = llm.invoke("https://cdn.eyesmag.com/content/uploads/posts/2022/03/22/main-d3bbc024-549a-4a23-9c08-5cb675d6b028.jpg" + "\n 이 사진을 묘사해봐")

print(response.choices[0].message.content)
# print(type(np.array2string(np.array(input_img))))


# answer_context = '''
# 이름: 홍길동

# 전공:
# - 컴퓨터공학과(석사)
# - 컴퓨터공학과(학사)

# 지원 직무: CI/CD

# 진행 프로젝트 목록:
# - AI 타이어 마모상태 점검 앱 개발
# - 실시간 분광 이미지 분산 처리 시스템 개발
# - 스마트 산업 설비 분석 서비스 개발
# - 자율주행 알고리즘 면허취득 프로젝트

# 이력상 특이점:
# - 10년 이상 경력
# - 다양한 산업체에서의 프로젝트 경험
# - 정보처리 기사, 전산회계 1급, 정보보안 산업기사 등의 다수 자격증 보유
# '''