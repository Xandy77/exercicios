'''
from googleapiclient.discovery import build

def buscar_videoaulas(api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    resposta = youtube.search().list(q="videoaulas Python", part="snippet", type="video", maxResults=5).execute()

    for item in resposta['items']:
        print("Título:", item['snippet']['title'])
        print("URL:", "https://www.youtube.com/watch?v=" + item['id']['videoId'], "\n")

# Insira sua chave de API correta aqui
api_key = 'SUA_CHAVE_REAL'
buscar_videoaulas(api_key)
'''

'''
Crie um programa que automatize uma busca na Internet por videoaulas sobre Python no Youtube.
'''

import pyautogui as auto
import time

auto.PAUSE = 0.5

auto.press('win')
auto.write('firefox')
auto.press('enter')
auto.hotkey('alt','space')
auto.press('x')
auto.write('youtube.com.br')
auto.press('enter')

time.sleep(2)

for i in range(4):
    auto.press('tab')

auto.write('Python')
auto.press('enter')     Python
