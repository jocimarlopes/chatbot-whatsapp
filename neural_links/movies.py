import requests
from bs4 import BeautifulSoup
import ssl
import subprocess
import base64

ssl._create_default_https_context = ssl._create_unverified_context

URL = (base64.b64decode('aHR0cHM6Ly9vbmRlYmFpeGEuY29tL2luZGV4LnBocD9zPQ==')).decode('utf-8')

frases_movies = [
    "baixe o filme ",
    "baixe o filme do ",
    "baixe o filme da ",
    "baixa o filme do ",
    "baixa o filme da ",
    "baixar o filme ",
    "baixar filme ",
    "baixa filme ",
    "baixa o filme ",
    "baixe o último filme ",
    "baixar o último filme ",
    "baixar último filme ",
    "baixa o último filme ",
    "baixa último filme ",
    "baixe último filme ",
    "baixe o último filme do ",
    "baixa o ultimo filme do ",
    "baixe o último filme do ",
    "baixa o ultimo filme do ",
    "baixe último filme do ",
    "baixa último filme do "
]
frases_series = [
    "baixa a série ",
    "baixar a série ",
    "baixe a série ",
]


def run(args):
    print(args)
    i = 1
    go = URL + args

    page = requests.get(go)
    soup = BeautifulSoup(page.text, 'html.parser')

    list_movies = soup.find(id='capas_pequenas')

    filtered_list_movies = list_movies.find_all('a')
    new_list_links = []
    new_list = []

    try:
        for link in filtered_list_movies:
            if link.get('href') not in new_list_links:
                new_list_links.append(link.get('href'))
                new_list.append(link)
        for item in new_list:
            if i < 3:
                i = i + 1
                torrent_page = requests.get(item.get('href'))
                soup_torrent = BeautifulSoup(torrent_page.text, 'html.parser')

                list_movies_torrent = soup_torrent.find(id='lista_download')
                filtered_list_movies_torrent = list_movies_torrent.find_all(
                    'a')

                for obj in filtered_list_movies_torrent:
                    if 'magnet:' in obj.get('href'):
                        mgn = obj.get('href')
                        subprocess.call(
                            'gnome-terminal -x bash -c "cd ~/Downloads/ && webtorrent download {}; exec bash"'.format(mgn), shell=True)
                        return "Achei o filme senhor vou pôr a baixar"
    except Exception as e:
        print(e)
        return "Desculpe senhor, não consegui encontrar o filme."


def download_movie(text):
    for item in frases_movies:
        if item in text:
            print(item)
            text = text.replace(item, "")
            return run(text)
    for item in frases_series:
        if item in text:
            return "Desculpe senhor, eu baixo apenas filmes por enquanto."
