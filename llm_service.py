import asyncio
import json
import requests
import aiohttp
from time import time

default_models= ["llama3.2:latest", "qwen2.5-coder:7b", "llama3:8b-instruct-fp16"]

class LLM:
    """
    A class to interact with a local LLM service using the Ollama.ai

    Format is either None or "json"
    """

    def __init__(self, *, prompt, model=default_models[0], format=None):
        self.prompt = prompt
        self.model = model
        self.format = format

    def create_payload(self, data):
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": self.prompt},
                {"role": "assistant", "content": "Understood"},
                {"role": "user", "content": data},
            ],
            "options" : {"temperature":0.01},
            "stream": False,
        }
        if self.format:
            payload["format"] = self.format
        return payload

    def process(self, *, data):
        payload = self.create_payload(data)

        response = requests.post("http://localhost:11434/api/chat", data=json.dumps(payload), stream=False)
        return response.json().get("message", {}).get("content","").strip()

    async def aprocess(self, *, data):
        start = time()
        payload = self.create_payload(data)
        async with aiohttp.ClientSession() as session:
            async with session.post("http://localhost:11434/api/chat", data=json.dumps(payload)) as response:
                result = await response.text()
                print("Took",(time() - start))
                return json.loads(result).get("message", {}).get("content","").strip()

    async def amulti(self, *, data_list):
        tasks = [self.aprocess(data=data) for data in data_list]
        return await asyncio.gather(*tasks)
        