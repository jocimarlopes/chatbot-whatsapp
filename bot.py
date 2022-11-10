from neural_links import wikipedia_search
from neural_links import learning
from neural_links import date_now
from neural_links import temperatura
from neural_links import calculator
from neural_links import battery
import sqlite3

con = sqlite3.connect('database/learning.db', check_same_thread=False)
cur = con.cursor()

def init(frase_to_jarvis):
        #battery.battery()
        text = str(frase_to_jarvis).lower() #(speech.ouvir_microfone()).lower()
        text = text.replace("jarvis ", "")
        res = neural(text)
        text = ""
        return res


def neural(text):
    waiting = False
    if text:
        res = None
        if not res:
            res = learning.learn_now(text)
        if not res:
            res = learning.search_in_memory(text)
        if not res:
            res = calculator.calculate_now(text)
        if not res:
            res = battery.get_battery(text)
        if not res:
            res = date_now.dates(text)
        if not res:
            res = temperatura.weather(text)
        if not res:
            res = wikipedia_search.wiki_search(text)
        if not res:
            res = 'Desculpe, não entendi, ainda estou aprendendo'
        return res
