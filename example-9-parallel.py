from llm_service import LLM
from time import time
import asyncio

print("""
Multiple calls in parallel
""")


answer_question = LLM(prompt="""Respond with the singluar obvious answer.  Then give 2 sentences of more detail.""")


data_to_parse = (
    'What color is the sky?',
    'What is the capital of France?',
    'What is the speed of light?',
    'What is the largest mammal?'
)

print("Parallel calls")
start = time()
results = asyncio.run(answer_question.amulti(data_list=data_to_parse))
print("All calls took",(time() - start),"\n")
# for sentence, result in zip(data_to_parse, results):
#     print(f"Q: {sentence} A: {result.replace("\n"," ")}\n")


start = time()
for sentence in data_to_parse:
    # print(f"Q: {sentence} A: {answer_question.process(data=sentence).replace("\n"," ")}\n")
    result = answer_question.process(data=sentence).replace("\n"," ")
print("All calls took",(time() - start),"\n")
