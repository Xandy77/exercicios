# 6. Programa para encontrar números primos em uma lista:
#numeros = list(range(1, 21))
#primos = [num for num in numeros if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]
#print(f"Números primos na lista: {primos}")


import math

def primo(numero):
    if numero < 2:
        return False
    else:
        ...
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
        else:
            ...
    return True

if __name__ == '__main__':
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    print('Lista de numeros primos:')

    for numero in numeros:
        if primo(numero):
            print(f'O numero {numero} é primo.')
        else:
            ... # (... é para ignorar o trecho seguinte)