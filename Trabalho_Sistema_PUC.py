import sys
import json

def salvar_lista(lista_qualquer, nome_arquivo):
    with open(nome_arquivo,"w",encoding="utf-8") as arquivo_aberto:
        json.dump(lista_qualquer,arquivo_aberto,ensure_ascii=False)

def ler_lista(nome_arquivo):
    try:
        with open(nome_arquivo,"r",encoding="utf-8") as arquivo_aberto:
            lista_qualquer = json.load(arquivo_aberto)
            return lista_qualquer
    except FileNotFoundError:
        print("Arquivo não encontrado, retornando a lista vazia")
        return []

arquivo_aluno = "alunospuc_2.json"
arquivo_professores = "professorespuc.json"
arquivo_disciplina = "disciplina.json"
arquivo_turma = "turmas.json"
arquivo_matricula = "matricula.json"

def mostrar_menu_principal():
    print("MENU PRINCIPAL")
    print('1.Estudantes')
    print('2.Disciplinas')
    print('3.Professores')
    print('4.Turmas')
    print('5.Matrícula')
    print('0.Sair')
    return int(input('Informe a opção desejada: '))

def mostrar_menu_secundário():
    print('1. Incluir')
    print('2. Listar')
    print('3. Atualizar')
    print('4. Excluir')
    print('5. Voltar ao menu principal')
    return int(input("Escolha a ação desejada: "))

def listar(arquivo_aluno, arquivo_professores, arquivo_disciplina, arquivo_turma, arquivo_matricula):
    print("Você escolheu a opção Listar")
    if menu == 1:
        print("Lista de alunos: ")
        lista_qualquer = ler_lista(arquivo_aluno)
        if lista_qualquer:
            for dados_dicionario in lista_qualquer:
                print(dados_dicionario)
        else:
            print('Está lista está vazia')

    if menu == 2:
        print("Lista de disciplinas: ")
        lista_qualquer = ler_lista(arquivo_disciplina)
        if lista_qualquer:
            for dados_dicionario in lista_qualquer:
                print(dados_dicionario)
        else:
            print('Está lista está vazia')

    if menu == 3:
        print("Lista de professres: ")
        lista_qualquer = ler_lista(arquivo_professores)
        if lista_qualquer:
            for dados_dicionario in lista_qualquer:
                print(dados_dicionario)
        else:
            print('Está lista está vazia')

    if menu == 4:
        print("Lista das Turmas: ")
        lista_qualquer = ler_lista(arquivo_turma)
        if lista_qualquer:
            for dados_dicionario in lista_qualquer:
                print(dados_dicionario)
        else:
            print('Está lista está vazia')

    if menu == 5:
        print("Lista de Matrícula: ")
        lista_qualquer = ler_lista(arquivo_matricula)
        if lista_qualquer:
            for dados_dicionario in lista_qualquer:
                print(dados_dicionario)
        else:
            print('Está lista está vazia')

def cadastrar(arquivo_aluno, arquivo_professores, arquivo_disciplina, arquivo_turma, arquivo_matricula):
    print('Você escolheu a opção Cadastrar')
    if menu == 1:
        codigo = int(input('Digite o código do estudante: '))
        nome = input('Digite o nome do estudante: ')
        CPF = int(input('Digite o CPF do aluno: '))

        dados_dicionario = {
            "codigo": codigo,
            "nome": nome,
            "CPF": CPF
        }
        lista_qualquer = ler_lista(arquivo_aluno)
        lista_qualquer.append(dados_dicionario)
        salvar_lista(lista_qualquer, arquivo_aluno)

    if menu == 2:
        codigo = int(input('Digite o código da disciplina: '))
        nome = input('Digite o nome da disciplina: ')

        dados_dicionario = {
            "codigo": codigo,
            "nome": nome,
        }
        lista_qualquer = ler_lista(arquivo_disciplina)
        lista_qualquer.append(dados_dicionario)
        salvar_lista(lista_qualquer, arquivo_disciplina)

    if menu == 3:
        codigo = int(input('Digite o código do professor: '))
        nome = input('Digite o nome do professor: ')
        CPF = int(input('Digite o CPF do professor: '))

        dados_dicionario = {
            "codigo": codigo,
            "nome": nome,
            "CPF": CPF
        }
        lista_qualquer = ler_lista(arquivo_professores)
        lista_qualquer.append(dados_dicionario)
        salvar_lista(lista_qualquer, arquivo_professores)

    if menu == 4:
        codigo = int(input('Digite o código da Turma: '))
        nome = int(input('Digite o código do professor: '))
        disciplina = int(input('Digite o código da disciplina: '))
        dados_dicionario = {
            "codigo": codigo,
            "codigo_professor": nome,
            "codigo_disciplina": disciplina
        }
        lista_qualquer = ler_lista(arquivo_turma)
        if codigo in [turma['codigo'] for turma in lista_qualquer]:
            print('Código da Turma já Existente!')
        else:
            lista_qualquer.append(dados_dicionario)
            salvar_lista(lista_qualquer, arquivo_turma)

    if menu == 5:
        codigo = int(input('Digite o código da Turma: '))
        codigo_estudante = int(input('Digite o código da Turma: '))
        dados_dicionario = {
            "codigo": codigo,
            "codigo_estudante": codigo_estudante,
        }
        lista_qualquer = ler_lista(arquivo_matricula)
        if codigo in [turma['codigo'] for turma in lista_qualquer]:
            print('Código da Turma já Existente!')
        else:
            lista_qualquer.append(dados_dicionario)
            salvar_lista(lista_qualquer, arquivo_matricula)

def editar(arquivo_aluno, arquivo_professores, arquivo_disciplina, arquivo_turma, arquivo_matricula):
    if menu == 1:
        codigo_edicao = int(input("Qual o códido do aluno deseja editar? "))
        lista = ler_lista(arquivo_aluno)
        estudante_modificado = None
        for dados_dicionario in lista:
            if dados_dicionario["codigo"] == codigo_edicao:
                estudante_modificado = dados_dicionario
                break
        if estudante_modificado is None:
            print(f'Não foi encontrado estudante com esse código')
        else:
            estudante_modificado["codigo"] = int(input('Digite o novo código: '))
            estudante_modificado["nome"] = input('Digite o novo nome: ')
            estudante_modificado["CPF"] = int(input('Digite o novo CPF: '))
        salvar_lista(lista, arquivo_aluno)

    if menu == 2:
        codigo_edicao = int(input("Qual o códido da disciplina deseja editar? "))
        lista = ler_lista(arquivo_disciplina)
        disciplina_modficado = None
        for dados_dicionario in lista:
            if dados_dicionario["codigo"] == codigo_edicao:
                disciplina_modficado = dados_dicionario
                break
        if disciplina_modficado is None:
            print(f'Não foi encontrado disciplina com esse código')
        else:
            disciplina_modficado["codigo"] = int(input('Digite o novo código: '))
            disciplina_modficado["nome"] = input('Digite a nova disciplina: ')
        salvar_lista(lista, arquivo_disciplina)

    if menu == 3:
        codigo_edicao = int(input("Qual o códido do professor deseja editar? "))
        lista = ler_lista(arquivo_professores)
        professor_modificado = None
        for dados_dicionario in lista:
            if dados_dicionario["codigo"] == codigo_edicao:
                professor_modificado = dados_dicionario
                break
        if professor_modificado is None:
            print(f'Não foi encontrado professsor com esse código')
        else:
            professor_modificado["codigo"] = int(input('Digite o novo código: '))
            professor_modificado["nome"] = input('Digite o novo nome: ')
            professor_modificado["CPF"] = int(input('Digite o novo CPF: '))
        salvar_lista(lista, arquivo_professores)

    if menu == 4:
        codigo_edicao = int(input("Qual o códido da Turma deseja editar? "))
        lista = ler_lista(arquivo_turma)
        turma_modificado = None
        for dados_dicionario in lista:
            if dados_dicionario["codigo"] == codigo_edicao:
                turma_modificado = dados_dicionario
                break
        if turma_modificado is None:
            print(f'Não foi encontrado Turma com esse código')
        else:
            turma_modificado["codigo"] = int(input('Digite o novo código: '))
            turma_modificado["codigo_aluno"] = int(input('Digite o novo código do aluno: '))
            turma_modificado["codigo_disciplina"] = int(input('Digite o novo código da disciplina: '))
        salvar_lista(lista, arquivo_turma)

    if menu == 5:
        codigo_edicao = int(input("Qual o códido do professor deseja editar? "))
        lista = ler_lista(arquivo_matricula)
        matricula_modificado = None
        for dados_dicionario in lista:
            if dados_dicionario["codigo"] == codigo_edicao:
                matricula_modificado = dados_dicionario
                break
        if matricula_modificado is None:
            print(f'Não foi encontrado professsor com esse código')
        else:
            matricula_modificado["codigo"] = int(input('Digite o novo código: '))
            matricula_modificado["nome"] = int(input('Digite o novo nome: '))
        salvar_lista(lista, arquivo_matricula)

def excluir(arquivo_aluno, arquivo_professores, arquivo_disciplina, arquivo_turma, arquivo_matricula):
    if menu == 1:
        lista = ler_lista(arquivo_aluno)
        codigo_exclusao = int(input("Qual o códido do aluno deseja excluir? "))
        estudante_removido = None
        for dados_dicionario in lista:
            if dados_dicionario["codigo"] == codigo_exclusao:
                estudante_removido = dados_dicionario
                break
        lista.remove(estudante_removido)
        salvar_lista(lista, arquivo_aluno)

    if menu == 2:
        lista = ler_lista(arquivo_disciplina)
        codigo_exclusao = int(input("Qual o códido da disciplina deseja excluir? "))
        disciplina_removido = None
        for dados_dicionario in lista:
            if dados_dicionario["codigo"] == codigo_exclusao:
                disciplina_removido = dados_dicionario
                break
        lista.remove(disciplina_removido)
        salvar_lista(lista, arquivo_aluno)

    if menu == 3:
        lista = ler_lista(arquivo_professores)
        codigo_exclusao = int(input("Qual o códido do professor deseja excluir? "))
        professor_removido = None
        for dados_dicionario in lista:
            if dados_dicionario["codigo"] == codigo_exclusao:
                professor_removido = dados_dicionario
                break
        lista.remove(professor_removido)
        salvar_lista(lista, arquivo_professores)

    if menu == 4:
        lista = ler_lista(arquivo_turma)
        codigo_exclusao = int(input("Qual o códido da turma deseja excluir? "))
        turma_removido = None
        for dados_dicionario in lista:
            if dados_dicionario["codigo"] == codigo_exclusao:
                turma_removido = dados_dicionario
                break
        lista.remove(turma_removido)
        salvar_lista(lista, arquivo_turma)

    if menu == 5:
        lista = ler_lista(arquivo_matricula)
        codigo_exclusao = int(input("Qual o códido do professor deseja excluir? "))
        matricula_removido = None
        for dados_dicionario in lista:
            if dados_dicionario["codigo"] == codigo_exclusao:
                matricula_removido = dados_dicionario
                break
        lista.remove(matricula_removido)
        salvar_lista(lista, arquivo_matricula)


def listar_ações(arquivo_aluno):
    while True:
        menu_secundario = mostrar_menu_secundário()
        if menu_secundario == 1:
            cadastrar(arquivo_aluno, arquivo_professores, arquivo_disciplina,
                    arquivo_turma, arquivo_matricula)

        elif menu_secundario == 2:
            listar(arquivo_aluno, arquivo_professores, arquivo_disciplina,
                   arquivo_turma, arquivo_matricula)

        elif menu_secundario == 3:
            editar(arquivo_aluno, arquivo_professores, arquivo_disciplina,
                   arquivo_turma, arquivo_matricula)

        elif menu_secundario == 4:
            excluir(arquivo_aluno, arquivo_professores, arquivo_disciplina,
                    arquivo_turma, arquivo_matricula)

        elif menu_secundario == 5:
            print("Voltar ao menu principal")
            break
        else:
            print('Opção Inválida!')

while True:
        menu = mostrar_menu_principal()
        if menu == 0:
            print('Encerrando Programa')
            sys.exit()
        if menu == 1:
            print('Vocês escolheu a opção Estudantes')
            listar_ações(arquivo_aluno)
        elif menu == 2:
            print("Você escolheu a opção Disciplinas")
            listar_ações(arquivo_disciplina)
        elif menu == 3:
            print('Você escolheu a opção Professores')
            listar_ações(arquivo_professores)
        elif menu == 4:
            print('Você escolheu a opção Turmas')
            listar_ações(arquivo_turma)
        elif menu == 5:
            print('Você escolheu a opção Matrículas')
            listar_ações(arquivo_matricula)
        else:
            print("Valor inválido!")