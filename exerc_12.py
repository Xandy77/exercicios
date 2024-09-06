'''
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='auto', target='pt')

while True:
    try:
        texto = input('Texto a ser traduzido: ')
        texto_traduzido = tradutor.translate(texto)

        print(f'Text traduzido: "{texto_traduzido}')

        repetir = input('Deseja traduzir outro texto(s/n)?').lower

        if repetir == 's':
            continue
        else:
            break
    except:
        print('Não foi possível traduzir.')
'''

'''
Crie um programa que traduza qualquer texto em qualquer idioma para o português.
'''
# variavel "tradutor" recebe "GoogleTranslator(source='auto', target='pt')" 
# ele incia um loop "while true" , faz um "try"
# 
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='auto', target='pt')

while True:
    try:
        texto_original = input('Digite o texto a ser traduzido para o português ou aperte Enter para encerrar: ')
        if texto_original != '':
            texto_traduzido = tradutor.translate(texto_original)
            print(texto_traduzido)
            continue
        else:
            break
    except Exception as e:
        print(f'Não foi possível traduzir o texto. {e}.')
        break