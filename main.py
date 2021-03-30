import requests
import json
import time


def system():
    while True:
        date = requests.get("https://blockchain.info/ru/ticker").text
        d = json.loads(date)
        print(d[currency]['buy'])
        time.sleep(60)


currency = input("Введите валюту: ")
system()
