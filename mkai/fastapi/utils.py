import openai
import numpy as np

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