class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEspera:
    def __init__(self):
        self.cabeca = None
    
    def inserir(self, nodo):
        if self.cabeca is None:
            self.cabeca = nodo
            return        
        nodo_atual = self.cabeca
        while nodo_atual.proximo:            
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo

    def inserir_com_prioridade(self, nodo):
        if self.cabeca is None:
            self.cabeca = nodo
            return        
        if self.cabeca.cor == 'V':
            nodo.proximo = self.cabeca
            self.cabeca = nodo
            return
        nodo_atual = self.cabeca
        while nodo_atual.proximo:
            if nodo_atual.proximo.cor == 'V':
                nodo.proximo = nodo_atual.proximo
                nodo_atual.proximo = nodo
                return
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo
    
    def remover(self):
        if self.cabeca is None:
            return None
        nodo = self.cabeca
        self.cabeca = self.cabeca.proximo
        return nodo

    def imprimir(self):
        print('Lista ->', end='')
        nodo_atual = self.cabeca        
        while nodo_atual:
            print(f' [{nodo_atual.cor},{nodo_atual.numero}]', end='')
            nodo_atual = nodo_atual.proximo
        print('')

lista = None

def inserirSemPrioridade(nodo):
    lista.inserir(nodo=nodo)

def inserirComPrioridade(nodo):
    lista.inserir_com_prioridade(nodo=nodo)

def inserir():
    cor = input('Informe a cor do cartão (A/V): ')
    numero = int(input('Informe o número do cartão: '))
    nodo = Nodo(numero=numero, cor=cor)
    if nodo.cor == 'A':
        inserirComPrioridade(nodo)
    else:
        inserirSemPrioridade(nodo)

def imprimirListaEspera():
    lista.imprimir()

def atenderPaciente():
    nodo = lista.remover()
    if nodo is None:
        print('Nnenhum paciente para ser atendido.')
        return
    print(f'Atendendo o paciente cartão cor {nodo.cor} e número {nodo.numero}')

def menu():
    print('1 - Adicionar paciente à fila')
    print('2 - Mostrar pacientes na fila')
    print('3 - Chamar paciente')
    print('4 - Sair')
    opcao = int(input())
    match opcao:
        case 1:
            inserir()
        case 2:
            imprimirListaEspera()
        case 3:
            atenderPaciente()
        case 4:
            return
    menu()

lista = ListaEspera()
menu()