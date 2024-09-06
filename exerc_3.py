# 3. Programa que verifica se um número é par ou ímpar:
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


#try:
#    numero= int(input('Informe um número: '))

#    print(f'{numero} é par.') if numero % 2 == 0 else f'{numero} é impar.')
#except Exception as e:
#    print(f'Não foi possivel encontrar o numero. {e}.')