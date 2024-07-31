import openai
import numpy as np
import json

def cos_sim(a: list, b: list) -> float:
	return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))

def calculate_similarity(sentence_a: str, sentence_b: str) -> float:
	embed1 = openai.embeddings.create(
	model="text-embedding-3-small",
	input=sentence_a
		).data[0].embedding

	embed2 = openai.embeddings.create(
	model="text-embedding-3-small",
	input=sentence_b
		).data[0].embedding
	return cos_sim(embed1, embed2)

def treshold_check(cosine_similarity: float, threshold: float) -> bool:
	if cosine_similarity >= threshold:
		return False
	else:
		return True

def load_analyst_api_key(env_file_path):
    with open(env_file_path, 'r') as file:
        env_data = json.load(file)

        PORTFOLIO_ANALYSIS_API_KEY = env_data["PORTFOLIO_ANALYSIS_API_KEY"]
    return PORTFOLIO_ANALYSIS_API_KEY

def extract_json(json_str):
    try:
        # 첫 번째 {와 마지막 }의 위치를 찾음
        start_index = json_str.index('{')
        end_index = json_str.rindex('}')
        
        # 해당 위치 사이의 문자열을 추출
        extracted_str = json_str[start_index:end_index + 1]
        
        return extracted_str
    except ValueError as e:
        print("유효한 JSON 형식이 아닙니다:", e)
        return None