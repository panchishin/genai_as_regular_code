import json
import requests

class LLM:
    """
    A class to interact with a local LLM service using the Ollama.ai

    Format is either None or "json"
    """

    def __init__(self, *, directive, model="llama2:13b-chat-q6_K", format=None):
        self.directive = directive
        self.model = model
        self.format = format

    def process(self, *, data):
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": self.directive},
                {"role": "assistant", "content": "Understood"},
                {"role": "user", "content": data},
            ],
            "options" : {"temperature":0.01},
            "stream": False,
        }
        if self.format:
            payload["format"] = self.format

        response = requests.post("http://localhost:11434/api/chat", data=json.dumps(payload), stream=False)
        return response.json().get("message", {}).get("content","").strip()

