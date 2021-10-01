import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}


def get(url, data, headers=headers):
    return requests.get(url, params=data, headers=headers).json()


def post(url, data, headers=headers):
    return json(url, data, headers=headers)


def json(url, data, headers=headers):
    return requests.post(url, json=data, headers=headers).json()


def form(url, data, headers=headers):
    return requests.post(url, data=data, headers=headers).json()
