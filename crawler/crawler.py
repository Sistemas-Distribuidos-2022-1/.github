import requests

URL = "https://www.inf.ufg.br/"
resp = requests.get(URL)
print(resp.status_code)
print(resp.text)
