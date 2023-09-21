import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url
        
        # URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        

    def get_response_body(self):
        
        response = requests.get(self.url)
        # response.raise_for_status()
        return response.content

    def load_json(self):
        return json.loads(self.get_response_body())