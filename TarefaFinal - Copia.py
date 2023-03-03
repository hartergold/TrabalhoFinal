import time
import os


# definição de classe

class Evento:
    def __init__(self, data, hora, description, duration):
        self.data = data
        self.hora = hora
        self.description = description
        self.duration = duration


# Listas a serem a usadas
recebetudo = []
data = []
hora = []
description = []
duration = []


# função do menu que dará os direcionamentos necessarios

def menu():
    print()
    print('=' * 31)
    print(f' |[1].Agendar novo compromisso|\n ''|[2].Excluir compromisso     '
          '|\n |[3].Modificar Comprimisso   |\n |[4].Consultar               '
          '|\n |[5].Listar todos            |\n |[6].Sair                    |'
          )
    print('=' * 31)
    while True:
        try:
            opcao = int(input('Escolha uma opção: '))
            if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                print('opção invalida digite novamente!')
                continue
            break
        except BaseException:
            print('Apenas números!')
            continue

    if opcao == 1:
        add_event()

    elif opcao == 2:
        Excluir_Compromisso()

    elif opcao == 3:
        os.system('cls')
        Modificar_Compromisso()

    elif opcao == 4:
        os.system('cls')
        Consultar_Compromisso()

    elif opcao == 5:
        os.system('cls')
        mostrarodos()

    elif opcao == 6:
        print('Saindo do programa...\nObrigado por utilizar!')
        time.sleep(2)
        os.system('cls')
        print('Fim')


# Funções que serão implementadas no codigo para as funcionalidades da agenda, com nomes autoexplicativos

def add_event():
    ac = ""
    print('Adicionar novo compromisso!')
    Evento.data = ""
    Evento.data = input('Digite a data no formato (dd/mm/aaaa):')
    while True:
        if recebetudo != []:
            achou = False
            for c in range(len(recebetudo)):
                if Evento.data == recebetudo[c].data:
                    achou = True
            if achou == True:
                print("Já tem um compromisso com essa mesma data!")
                ac = input("Deseja adicionar mesmo assim?[s/n]")
            if achou == False:
                break
            if ac == 's':
                break
            if ac == 'n':
                Evento.data = input('Digite novamente a data no formato (dd/mm/aaaa):')
        else: 
            break
    Evento.hora = input('Digite a hora(hh:mm):')
    Evento.description = input('Digite a descrição:')
    Evento.duration = input('Digite a duração (em horas):')
    while True:
        try:
            Evento.duration = float(Evento.duration)
            break
        except:
            print('Apenas Numeros por favor!')
            Evento.duration = input('Digite a duração a duração (em Horas):')
    print('O compromisso foi registrado!')
    print('Voltando ao menu...')
    time.sleep(2)
    os.system('cls')
    recebe = Evento(Evento.data, Evento.hora, Evento.description, Evento.duration)
    recebetudo.append(recebe)
    menu()


def mostrarodos():
    if recebetudo != []:
        print('Mostrando todos os compromissos!')
        for i in range(len(recebetudo)):
            time.sleep(1)
            print('=' * 25)
            print(
                f' DATA:{recebetudo[i].data}\n HORA:{recebetudo[i].hora}\n DESCRIÇÂO:{recebetudo[i].description}\n DURAÇÂO:{recebetudo[i].duration} Horas')
    else:
        print('Não há nenhum evento registrado!')
    print()
    retornar = input('Deseja retornar ao Menu[s/n]?')
    while retornar != 's' and retornar != 'n':
        print('Digite apenas s ou n!')
        retornar = input('Deseja retornar ao Menu[s/n]?')
        if retornar == 's' or retornar == 'n':
            break
    if retornar == 's':
        print('Retornando ao menu!')
        time.sleep(2)
        os.system('cls')
        menu()
    if retornar == 'n':
        os.system('cls')
        print('Saindo do programa...\nObrigado por utilizar!')
        time.sleep(2)
        print('Fim')


def Excluir_Compromisso():
    if recebetudo != []:
        print('Exibindo os compromissos!')
        for i in range(len(recebetudo)):
            time.sleep(1)
            print('=' * 20)
            print(
                f' DATA: {recebetudo[i].data}\n HORA:{recebetudo[i].hora}\n DESCRIÇÂO:{recebetudo[i].description}\n DURAÇÂO:{recebetudo[i].duration}')
            print('=' * 20)

        paradel = input('Digite a posição do evento a ser deletado!\n')
        while True:
            # tratamento para que sejam digitados somente numeros
            try:
                paradel = int(paradel)
                paradel -= 1
            except:
                pass
            # testa se o  numero digitado esta correspondente ao range da lista
            if paradel in range(len(recebetudo)):
                break
            # se não mostra uma mensagem e pede para digitar novamente
            else:
                print('Digite apenas números e posições existentes!')
                paradel = input('Digite uma posição VÁLIDA do compromisso para deletar!\n')
        # pede se o usuario realmente quer excluir
        confirm = input('Deseja realmente excluir[s/n]?')
        while confirm != 's' and confirm != 'n':
            print('digite apenas [s/n]!!')
            confirm = input('Deseja realmente excluir[s/n]?')
            if confirm == 's' or confirm == 'n':
                break
        if confirm == 's':
            recebetudo.pop(paradel)
            print('Compromisso excluido!')
            time.sleep(1.2)
            os.system('cls')
            print('Retornando ao menu!')
            menu()
        if confirm == 'n':
            print('Nenhum evento foi excluido.\nRetornando ao menu!')
            time.sleep(1.2)
            os.system('cls')
            menu()

    else:
        os.system('cls')
        print('Não há eventos disponiveis para excluir!')
        time.sleep(1.2)
        menu()


def Modificar_Compromisso():
    if recebetudo != []:
        print('Exibindo os compromissos!')
        for i in range(len(recebetudo)):
            time.sleep(1)
            print('=' * 25)
            print(
                f' DATA: {recebetudo[i].data}\n HORA:{recebetudo[i].hora}\n DESCRIÇÂO:{recebetudo[i].description}\n DURAÇÂO:{recebetudo[i].duration}')
        print()
        paramod = input('Digite a posição do evento a ser modificado!\n')
        while True:
            # tratamento para que sejam digitados somente numeros
            try:
                paramod = int(paramod)
                # para corresponder corretamente ao indice do elemento na lista fazemos -1
                paramod -= 1
            except:
                paramod = input('Digite a posição do evento a ser modificado!\n')
            # testa se o  numero digitado esta correspondente ao range da lista
            if paramod in range(len(recebetudo)):
                break
            # se não mostra uma mensagem e pede para digitar novamente
            else:
                print('Digite apenas posições existentes!')
                paramod = input('Digite uma posição VÁLIDA do compromisso para modicar!\n')

        confirm = input('Deseja realmente modificar?[s/n]?')
        while confirm != 's' and confirm != 'n':
            print('digite apenas [s/n]!!')
            confirm = input('Deseja realmente modificar?[s/n]?')
            if confirm == 's' or confirm == 'n':
                break
        if confirm == 's':
            Evento.description = input("Digite a nova descrição: ")
            Evento.duration = input("Digite a nova duração: ")
            while True:
                try:
                    Evento.duration = float(Evento.duration)
                    break
                except:
                    print('Apenas numeros!')
                    Evento.duration = input("Digite a nova duração: ")
            for k in range(len(recebetudo)):
                if recebetudo[paramod].data == recebetudo[k].data and recebetudo[paramod].hora == recebetudo[k].hora:
                    recebetudo[k].description = Evento.description
                if recebetudo[paramod].duration == recebetudo[k].duration:
                    recebetudo[k].duration = Evento.duration
            print('Compromisso modificado!')
            time.sleep(2)
            os.system('cls')
            print('Retornando ao menu!')
            menu()
        if confirm == 'n':
            print('Nennhum evento foi modificado.\nRetornando ao menu!')
            time.sleep(1.2)
            os.system('cls')
            menu()

    else:
        os.system('cls')
        print('Não há eventos disponiveis para modificar!')
        time.sleep(1)
        menu()


def Consultar_Compromisso():
    if recebetudo != []:
        encontrou = False
        metodo = input('[1] Para consultar pela data, [2] Para consultar pela data e hora: ')
        while True:
            if metodo == '1' or metodo == '2':
                try:
                    metodo = int(metodo)
                    os.system('cls')
                    break
                except:
                    pass
            print("Informação invalida digite novamente!")
            metodo = input('[1] Para consultar pela data, [2] Para consultar pela data e hora: ')
        # metodo de consulta 1
        if metodo == 1:
            search = input('Digite a data do evento que deseja buscar:\n')
            for c in range(len(recebetudo)):
                if search == recebetudo[c].data:
                    encontrou = True
                    print("="*25)
                    print(
                        f'|Data: {recebetudo[c].data} \n|Hora: {recebetudo[c].hora} \n|Descrição: {recebetudo[c].description} \n|Duração: {recebetudo[c].duration}')
                    
            if encontrou == False:
                print('Nenhum compromisso com essa data foi encontrado, volte ao menu e tente novamente!')
                time.sleep(1.5)
                os.system('cls')
        # metodo de pesquisa 2
        if metodo == 2:
            search1 = input('Digite a data a ser buscada:')
            search2 = input('DIgite a hora:')
            for i in range(len(recebetudo)):
                if search1 == recebetudo[i].data and search2 == recebetudo[i].hora:
                    encontrou = True
                    print("="*25)
                    print(
                        f'DATA: {recebetudo[i].data}\nHORA: {recebetudo[i].hora}\nDESCRIÇÂO: {recebetudo[i].description}\nDURAÇÂO: {recebetudo[i].duration}')

            if encontrou == False:
                print('Nenhum compromisso com essa data e hora foi encontrado, volte ao menu e tente novamente!')
                time.sleep(1.5)
                os.system('cls')
        menu()
    else:
        os.system('cls')
        print('Nenhum evento foi adicionado!')
        menu()


# Mensagem inicial e inicialização do programa
print('=' * 40)
print()
print(f'   Bem vindo a agenda de compromissos!')
print()
print(f'                          |Versão 0.0.1|')
print("Feito por: Wellinton Matheus e Eduardo Porfirio")
print('=' * 40)
menu()
