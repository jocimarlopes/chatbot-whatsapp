import requests
import base64

url = (base64.b64decode('aHR0cHM6Ly9hcGkubWF0aGpzLm9yZy92NC8/ZXhwcj0=')).decode('utf-8')

frases = [
    'quanto é ',
    'quanto são ',
    'quantos são ',
    'quantos é ',
    'quanto fica '
]
numerics = [
    {'c': '+', 'a': '%2B'},
    {'c': '-', 'a': '%2D'},
    {'c': 'x', 'a': '*'},
    {'c': '/', 'a': '%2F'},
    {'c': '*', 'a': '*'},
]

def get_response(n1, a, n2):
    try:
        response = requests.get(
            "{}{}{}{}".format(url, n1, a, n2))
        return "A resposta é {}".format(response.text)
    except Exception as e:
        print(e)
        return "Desculpe! Não consegui calcular, não entendi senhor."


def calculate_now(text):
    a = ''
    for item in frases:
        if item in text:
            text = text.replace(item, "")
    for item in numerics:
        if item['c'] in text:
            text = text.replace(' ', '')
            a = item['a']
            text = text.split(item['c'])
    if isNumber(text[0]) and isNumber(text[1]):
        return get_response(text[0], a, text[1])


def isNumber(value):
    try:
        float(value)
    except ValueError:
        return False
    return True
