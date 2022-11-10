import os

frases_play = [
    'play',
    'volte a tocar',
    'volta a tocar',
    'toca a música ',
    'toque a música ',
    'toque a musica ',
    'tocar musica ',
    'toque música ',
    'toca música ',
    'tocar música ',
    'tocar a música '
]
frases_pause = [
    'pause',
    'pausar música',
    'pause a música',
    'parar música',
    'parar música',
    'pare a música'
]

def play_music(frase):
    frase = frase.replace("'", "")
    for item in frases_play:
        if item in frase:
            os.popen("spotify play " + frase.replace(item, ""))
            return "Pronto senhor, está tocando..."

def pause_music(frase):
    for item in frases_pause:
        if item in frase:
            try:
                os.popen("spotify pause")
                return "Pronto senhor, pausei a música."
            except:
                return "Desculpe senhor, acho que não tem música tocando."