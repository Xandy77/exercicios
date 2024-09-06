# 5. Programa de lista de nomes:
nomes = ["Alice", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Heloisa", "Igor", "Joana"]

try:
    indice = int(input("Informe um indice: "))

    print(nomes[indice] if indice >= 0 and indice < 10 else 'Indice inexistente.')

except Exception as e:
    print(f'Não foi possível retornar o nome da lista. {e}.')


