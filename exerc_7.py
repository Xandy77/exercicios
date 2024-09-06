# 7. Programa de ordenação de lista de nomes:
nomes = []
while True:
    nome = input("Digite um nome (ou 'sair' para finalizar): ")
    if nome.lower() == 'sair':
        break
    nomes.append(nome)

nomes.sort()
print(f"Nomes em ordem alfabética: {nomes}")
print(f"Quantidade de nomes digitados: {len(nomes)}")

import os

nomes = []

while True:
    novo_nome = input('Informe o novo nome ou deixe em branco para encerrar: ')
    os.system('cls')
    if novo_nome != '':
        try:
            nomes.append(novo_nome)
            print(f'{novo_nome} inserido com sucesso.')
        except Exception as e:
            print(f'Não foi possível inserir o nome. {e}.')
        finally:
            continue

    else:
        break

nomes.sort()

print(f'Número de nomes na Lista: {len(nomes)}.')
for nome in nomes:
    print
