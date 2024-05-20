import csv

class Noh:
    def __init__(self, string):
        self.string = string
        self.esq = None
        self.dir = None

def criar_noh(string):
    return Noh(string)

def criar_arvore(perguntas):
    if len(perguntas) == 0:
        return None
    arvore = criar_noh(perguntas[0])
    arvore.esq = criar_arvore(perguntas[1:])
    arvore.dir = criar_arvore(perguntas[1:])
    return arvore

def insere_personagem(arvore, perguntas, personagem_dict):
    noh_atual = arvore

    #para cada pergunta exceto a ultima
    for p in perguntas[:-1]:
        if personagem_dict[p] == 1:
            noh_atual = noh_atual.esq
        else:
            noh_atual = noh_atual.dir
  
    #agora a ultima pergunta
    ultima_pergunta = perguntas[-1]
    if personagem_dict[ultima_pergunta] == 1:
        if noh_atual.esq != None:
            print("Erro: folha jÃ¡ ocupada " + noh_atual.esq.string + " e " + personagem_dict["nome"])
            exit(1)
        noh_atual.esq = criar_noh(personagem_dict["nome"])
    else:
        if noh_atual.dir != None:
            print("Erro: folha jÃ¡ ocupada " + noh_atual.dir.string + " e " + personagem_dict["nome"])
            exit(1)
        noh_atual.dir = criar_noh(personagem_dict["nome"])


def main():
    file_perguntas = open("akinator.csv", "r")
    csvreader = csv.reader(file_perguntas)
    
    
    #headers[0] = 4 2
    headers = next(csvreader)
    num_personagens, num_perguntas = map(int, headers[0].split())

    perguntas = []
    for i in range(1, num_perguntas+1):
        perguntas.append(headers[i])

    # print(num_personagens, num_perguntas)

    #print(perguntas)
    
    lista_dicts = []
    
    #Criando um dicionario para cada personagem
    for linha in csvreader:
        personagem_dict = {}
        personagem_dict['nome'] = linha[0]
        respostas = [int(i) for i in linha[1:]]
        
        for j in range(0, num_perguntas):
            personagem_dict[perguntas[j]] = respostas[j]

        #print(personagem_dict)
        lista_dicts.append(personagem_dict)

    #Vamos criar a Ã¡rvore, inicialmente com as perguntas, mas sem nenhum personagem
    arvore = criar_arvore(perguntas)
    
    #Agora vamos inserir os personagens na Ã¡rvore
    for personagem_dict in lista_dicts:
        insere_personagem(arvore, perguntas, personagem_dict)
    
    #Uma interface simples para o usuÃ¡rio, vai respondendo com 1 ou 0 e no final -1 para sair
    opi = 2
    atual = None
    while opi != -1:
        if atual is None:
            atual = arvore
        print(atual.string)
        opi = int(input())
        if opi == 1:
            atual = atual.esq
        elif opi == 0:
            atual = atual.dir
        elif opi == -1:
            break


if __name__ == "__main__":
    main()
