# 10. Programa de cadastro de cursos:
#cursos = []

#while True:
#    nome_curso = input("Digite o nome do curso (ou 'sair' para finalizar): ")
#    if nome_curso.lower() == 'sair':
#!SECTION        break
 #   duracao = int(input(f"Digite a duração do curso '{nome_curso}' em horas: "))
 #   periodo = input("Digite o período do curso (manhã, tarde, noite): ")
 #   vagas = int(input(f"Digite a quantidade de vagas para o curso '{nome_curso}': "))
#    cursos.append({"nome": nome_curso, "duracao": duracao, "periodo": periodo, "vagas": vagas})
#
#for curso in cursos:
#    print(f"Curso: {curso['nome']}, Duração: {curso['duracao']} horas, Período: {curso['periodo']}, Vagas: {curso['vagas']}")


'''
Crie um programa em que o usuário cadastre quantos cursos ele quiser (nome do curso, duração do curso em horas, Período do dia, quantidade de vagas) e exiba na tela.
'''

import os

cursos = []
 # opcao é uma váriavel que foi declarada
 # no case declaro um dicionario chamado curso
 # periodo do curso recebe uma string
 # se por acaso o usuario colocar uma letra diferente ele cai no exception
 # case 2: se o usuario informar um numero diferente do 1 pu 2 ele volta para digitar novamente
while True:
    opcao = input('1 para cadastrar novo curso ou 2 para exibir a lista de cursos cadastrados: ')
    os.system('cls')
    match opcao:
        case '1':
            curso = {}
            try:
                curso['Nome'] = input('Informe o nome do curso: ').capitalize()
                curso['Duração do curso'] = int(input('Informe a duração do curso: '))
                curso['Período'] = input('Matituino, Vespertino ou Noturno: ').lower()
                curso['Vagas'] = int(input('Informe o número de vagas: '))
                cursos.append(curso)
                print('Curso cadastrado com sucesso.')
            except Exception as e:
                print(f'Não foi possível cadastrar novo curso. {e}.')
            finally:
                continue
        case '2':
            for curso in cursos:
                for campo in curso:
                    print(f'{campo}: {curso.get(campo)}.')
                print('-'*30)
            break
        case _:
            print('Opção inválida.')
            continue