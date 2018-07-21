import requests


class ApiRest:

    def __init__(self, url):
        self.url = url

    def get_request(self, parameters):
        response = requests.get(self.url, params=parameters)
        data = response.json()
        print(data)
        return data
