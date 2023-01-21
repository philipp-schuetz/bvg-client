import requests

class Query:
    def __init__(self) -> None:
        pass
    
    def get_stops(self, location:str):
        query = f'https://v5.bvg.transport.rest/locations?poi=false&addresses=false&query={location}'
        r_json = requests.get(query).json()
        return r_json
    
