import sqlite3
from neural_links import database

con = sqlite3.connect('database/database.db', check_same_thread=False)
cur = con.cursor()

frases = {
    'human': [
        'quando eu falar ',
        'se eu falar ',
        'se eu disser ',
        'quando eu disser ',
        'quando falar ',
        'se falarem ',
        'caso falem ',
        'quando eu perguntar ',
        'quando eu fazer a pergunta '
    ],
    'robot': [
        ' você diz ',
        ' você fala ',
        ' tu diz ',
        ' tu fala ',
        ' você responde ',
        ' tu responde '
    ]
}

def to_learn(me, jarvis):
    try:
        database.learning_now(me, jarvis)
        return "Está salvo na memória senhor."
    except Exception as e:
        return "Desculpe senhor não consegui salvar na memória."

def search_in_memory(frase):
    try:
        return database.get_from_memory(frase)
    except Exception as e:
        print(e)
        return 'Não entendi, senhor. Peça novamente'

def learn_now(text):
    for item in frases['human']:
        if item in text:
            f = text.replace(item, "")
            for rob in frases['robot']:
                if rob in text:
                    s = f.split(rob)
            return to_learn(s[0], s[1])


def listening_all_time(me, jarvis):
    database.listening_all_time(me, jarvis)
