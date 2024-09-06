# 8. Programa para calcular a média de números decimais:
#quantidade = int(input("Digite a quantidade de números: "))
#numeros = []

#for _ in range(quantidade):
#    while True:
#        numero = float(input("Digite um número decimal entre 0 e 10: "))
#        if 0 <= numero <= 10:
#            numeros.append(numero)
#            break
#        else:
#            print("Número fora do intervalo. Tente novamente.")

#media = sum(numeros) / len(numeros)
#print(f"A média dos números digitados é: {media:.2f}")


import os
notas = []

while True:
    opcao = input('1 para inserir nota ou 2 para calcular a media: ')
    os.system('cls')
    match opcao:
        case '1':
            try:
                nova_nota = float(input('Informe um valor de 0 a 10: ').replace(',', '.'))
                if nova_nota <= 0 and nova_nota <= 10:
                    notas.append(nova_nota)
                    print('Nota inserida com sucesso.')
                else:
                    print('Nota inválida.')
            except Exception as e:
                print(f'Não foi possível inserir a nota. {e}.')
            finally:
                continue
        case '2':
            break
        case _:
            print('Opção inválida.')
            continue

print(f'Média: {(sum(notas)/len(notas)):,.2f}')