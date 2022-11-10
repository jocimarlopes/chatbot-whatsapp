import wikipedia

wikipedia.set_lang('pt')

frases = {
    0:'quem é ',
    1:'quem foi ',
    2:'quem foram ',
    3:'o que é ',
    4:'o que são ',
    5:'o que foram ',
    6:'quais são ',
    7:'quais foram ',
    8:'qual é ',
    9:'qual foi ',
    10:'sobre ',
    11:'qual o',
    11:'qual a'
}

def get_wiki(data):
    try:
        response = wikipedia.summary(data, sentences=2)
        return response
    except Exception as e:
        print(e)
        return 'não consegui buscar na Wiki, senhor.'

def wiki_search(frase):
    frase = frase.replace("pesquise ", "")
    for item in frases:
        if frases.get(item) in frase:
            return get_wiki(frase.split(frases[item]))