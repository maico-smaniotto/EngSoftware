class Nodo:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None

def hash_func(k):
    if k == 'DF':
        return 7
    k = list(k)
    return (ord(k[0]) + ord(k[1])) % 10

tabela_hash = [None] * 10

def inserir_na_tabela(nodo):
    indice = hash_func(nodo.sigla)
    nodo.proximo = tabela_hash[indice]
    tabela_hash[indice] = nodo

def imprimir_tabela():
    for i in range(10):
        print(f'{i}: ', end='')
        nodo_atual = tabela_hash[i]
        while True:
            if nodo_atual is None:
                print('None')
                break
            print(f'{nodo_atual.sigla}->', end='')
            nodo_atual = nodo_atual.proximo

def inserir_estados():
    inserir_na_tabela(Nodo('AC', 'Acre'))
    inserir_na_tabela(Nodo('AL', 'Alagoas'))
    inserir_na_tabela(Nodo('AP', 'Amapá'))
    inserir_na_tabela(Nodo('AM', 'Amazonas'))
    inserir_na_tabela(Nodo('BA', 'Bahia'))
    inserir_na_tabela(Nodo('CE', 'Ceará'))
    inserir_na_tabela(Nodo('DF', 'Distrito Federal'))
    inserir_na_tabela(Nodo('ES', 'Espírito Santo'))
    inserir_na_tabela(Nodo('GO', 'Goiás'))
    inserir_na_tabela(Nodo('MA', 'Maranhão'))
    inserir_na_tabela(Nodo('MT', 'Mato Grosso'))
    inserir_na_tabela(Nodo('MS', 'Mato Grosso do Sul'))
    inserir_na_tabela(Nodo('MG', 'Minas Gerais'))
    inserir_na_tabela(Nodo('PA', 'Pará'))
    inserir_na_tabela(Nodo('PB', 'Paraíba'))
    inserir_na_tabela(Nodo('PR', 'Paraná'))
    inserir_na_tabela(Nodo('PE', 'Pernabuco'))
    inserir_na_tabela(Nodo('PI', 'Piauí'))
    inserir_na_tabela(Nodo('RJ', 'Rio de Janeiro'))
    inserir_na_tabela(Nodo('RN', 'Rio Grande do Norte'))
    inserir_na_tabela(Nodo('RS', 'Rio Grande do Sul'))
    inserir_na_tabela(Nodo('RO', 'Rondônia'))
    inserir_na_tabela(Nodo('RR', 'Roraima'))
    inserir_na_tabela(Nodo('SC', 'Santa Catarina'))
    inserir_na_tabela(Nodo('SP', 'São Paulo'))
    inserir_na_tabela(Nodo('SE', 'Sergipe'))
    inserir_na_tabela(Nodo('TO', 'Tocantins'))
    
def inserir_aluno():
    inserir_na_tabela(Nodo('MS', 'Maico Smaniotto'))

imprimir_tabela()
inserir_estados()
imprimir_tabela()
inserir_aluno()
imprimir_tabela()