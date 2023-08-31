import requests
import os
from dotenv import load_dotenv
from bardapi import Bard

load_dotenv()


class Quote_api_call:
    def __init__(self, url, headers={}):
        self.url = url
        self.headers = headers

    def call_api(self):
        self.quotes_response = requests.get(self.url, headers=self.headers)
        if self.quotes_response.status_code == 200:
            quotes_data = self.quotes_response.json()
            return quotes_data
        else:
            print(f"Error: {self.quotes_response.status_code}")


class Bard_api_call:
    def __init__(self, token):
        self.token = token
        self.bard = Bard(token=self.token)

    def ask_bard(self, question):
        answer = self.bard.get_answer(question)
        return answer
