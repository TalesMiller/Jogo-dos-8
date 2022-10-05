from queue import PriorityQueue as pq
from copy import deepcopy
import copy
import random
import math
import time


class No(object):
    
    def __init__(self, matriz, Mover,Pai=None):
        self.matriz = matriz
        self.Mover = Mover
        self.Pai = Pai
        
        
    """Metodo espcial, o qual faz possivel que as classes possam ser compradas abertos. Tava bugando sem ele"""
    def __lt__(self,other): 
        return 0
    
    """Retorna a posição do bloco vazio/0."""
    def posicao_zero(self):
        for i in range(3):
            for j in range(3):
                if self.matriz[i][j] == 0:
                    return i,j
                

    def PegarInverso(self, matriz):

        lista=[] 
        for i in range(3):              #transformando matriz em uma lista
            lista.append(matriz[i][0])
            lista.append(matriz[i][1])
            lista.append(matriz[i][2])

        inv_count = 0
        k=0
        for i in range(8):
            k=i+1
            while k in range(9):            
                
                if (lista[k] and lista[i] and  lista[i] > lista[k]): 
                    inv_count= inv_count + 1

                k=k+1 
        return inv_count 
 
    # Verifica solucionabilidade da Matriz
    def ESolucionavel(self, matriz):  #matriz dada por nos inicial, se ela é SOLUCIONAVEL
 
        
        invCount = self.PegarInverso(matriz)
  
         
        if (invCount%2 == 0):
            return True
        else: 
            return False
        
    # Retorna o Tamanho apartir do Numero de Components fora de posição
    def Num_Comp_Fora(self, no_objetivo):
        total = 0
        
        for i in range(3):
            for j in range(3):
                if (self.matriz[i][j] == no_objetivo[0][0] and (i != 0 or j != 0)):      #compara a posicão do valor do no inicial, com a posicao do valor do no objetivo, percorre o no inicial todo até achar um valor igual, e marca sempre que qualquer um dos valores estiver fora de posicão em relacão ao objetivo
                    total = total + 1
                if(self.matriz[i][j] == no_objetivo[0][1] and (i != 0 or j != 1)):
                    total = total + 1
                if(self.matriz[i][j]== no_objetivo[0][2]and (i != 0 or j != 2)):
                    total = total + 1
                if(self.matriz[i][j]== no_objetivo[1][0]and (i != 1 or j != 0)):
                    total = total + 1
                if(self.matriz[i][j]== no_objetivo[1][1]and (i != 1 or j != 1)):
                    total = total + 1
                if(self.matriz[i][j]== no_objetivo[1][2]and (i != 1 or j != 2)):
                    total = total + 1                   
                if(self.matriz[i][j]== no_objetivo[2][0]and (i != 2 or j != 0)):
                    total = total + 1
                if(self.matriz[i][j] == no_objetivo[2][1]and (i != 2 or j != 1)):
                    total = total + 1
                if(self.matriz[i][j]== no_objetivo[2][2]and (i != 2 or j != 2)):
                    total = total + 1  

        return total
    
    # Retorna o tamanho da distancia Euclediana
    def Distan_Euclid(self, no_objetivo):
        total = 0

        for i in range(3):
            for j in range(3):
                if (self.matriz[i][j] == no_objetivo[0][0]):      #compara a posicão do valor do no inicial, com a posicao do valor do no objetivo, percorre o no inicial todo até achar um valor igual, e marca a distância euclidiana feita por pitagoras que a posicão do valor está da posicão do valor objetivo
                    linha = i
                    coluna = j
                    total = total + math.sqrt(abs(0-linha)*abs(0-linha) + abs(0-coluna)*abs(0-coluna))
                if(self.matriz[i][j]== no_objetivo[0][1]):
                    linha = i
                    coluna = j
                    total = total + math.sqrt(abs(0-linha)*abs(0-linha) + abs(1-coluna)*abs(1-coluna))
                if(self.matriz[i][j]== no_objetivo[0][2]):
                    linha = i
                    coluna = j
                    total = total + math.sqrt(abs(0-linha)*abs(0-linha) + abs(2-coluna)*abs(2-coluna))
                if(self.matriz[i][j]== no_objetivo[1][0]):
                    linha = i
                    coluna = j
                    total = total + math.sqrt(abs(1-linha)*abs(1-linha) + abs(0-coluna)*abs(0-coluna))
                if(self.matriz[i][j]== no_objetivo[1][1]):
                    linha = i
                    coluna = j
                    total = total + math.sqrt(abs(1-linha)*abs(1-linha) + abs(1-coluna)*abs(1-coluna))
                if(self.matriz[i][j]== no_objetivo[1][2]):
                    linha = i
                    coluna = j
                    total = total + math.sqrt(abs(1-linha)*abs(1-linha) + abs(2-coluna)*abs(2-coluna))                        
                if(self.matriz[i][j]== no_objetivo[2][0]):
                    linha = i
                    coluna = j
                    total = total + math.sqrt(abs(2-linha)*abs(2-linha) + abs(0-coluna)*abs(0-coluna)) 
                if(self.matriz[i][j]== no_objetivo[2][1]):
                    linha = i
                    coluna = j
                    total = total + math.sqrt(abs(2-linha)*abs(2-linha) + abs(1-coluna)*abs(1-coluna))
                if(self.matriz[i][j]== no_objetivo[2][2]):
                    linha = i
                    coluna = j
                    total = total + math.sqrt(abs(2-linha)*abs(2-linha) + abs(2-coluna)*abs(2-coluna))  

        return total
         
    # Retorna a Distancia de Manhattan.
    def Distanc_De_manhattan(self, no_objetivo):      #aqui foi passada uma matriz inicial por exemplo, ele pega o valor, e divide por 3, dando a linha, com esse mesmo valor, faz mod 3, dando a coluna
        total = 0

        for i in range(3):
            for j in range(3):
                if (self.matriz[i][j] == no_objetivo[0][0]):      #compara a posicão do valor do no inicial, com a posicao do valor do no objetivo, percorre o no inicial todo até achar um valor igual, e marca a distância de manhattan que a posicão do valor está da posicão do valor objetivo
                    linha = i
                    coluna = j
                    total = total + abs(0-linha) + abs(0-coluna)
                if(self.matriz[i][j]== no_objetivo[0][1]):
                    linha = i
                    coluna = j
                    total = total + abs(0-linha) + abs(1-coluna)
                if(self.matriz[i][j]== no_objetivo[0][2]):
                    linha = i
                    coluna = j
                    total = total + abs(0-linha) + abs(2-coluna)
                if(self.matriz[i][j]== no_objetivo[1][0]):
                    linha = i
                    coluna = j
                    total = total + abs(1-linha) + abs(0-coluna)
                if(self.matriz[i][j]== no_objetivo[1][1]):
                    linha = i
                    coluna = j
                    total = total + abs(1-linha) + abs(1-coluna)
                if(self.matriz[i][j]== no_objetivo[1][2]):
                    linha = i
                    coluna = j
                    total = total + abs(1-linha) + abs(2-coluna)                        
                if(self.matriz[i][j]== no_objetivo[2][0]):
                    linha = i
                    coluna = j
                    total = total + abs(2-linha) + abs(0-coluna) 
                if(self.matriz[i][j]== no_objetivo[2][1]):
                    linha = i
                    coluna = j
                    total = total + abs(2-linha) + abs(1-coluna)
                if(self.matriz[i][j]== no_objetivo[2][2]):
                    linha = i
                    coluna = j
                    total = total + abs(2-linha) + abs(2-coluna)  

        return total
    
    # Função que gera e retorna os nós.
    def Gerar_Nos(self):
        posicao_zero = self.posicao_zero() #localiza onde esta o 0 na matriz
        matriz = self.matriz #pega a parte da matriz em sí
        todosnos = [] #cria uma lista que guarda todos os nos.
        if not posicao_zero[0]-1<0: #checa se o 0 pode ser movido para cima  (se linha da posicao zero -1 for menor que zero)
            matriz_cima = deepcopy(matriz) #cria um deepcopy para não dar problema ao fazer os movimentos
            matriz_cima[posicao_zero[0]][posicao_zero[1]] = matriz_cima[posicao_zero[0]-1][posicao_zero[1]] #coloca o valor de baixo onde o zero estava(em baixo)
            matriz_cima[posicao_zero[0]-1][posicao_zero[1]] = 0 #coloca o zero em cima
            matriz_cima_no = No(matriz_cima,'Cima',self) 
            todosnos.append(matriz_cima_no) #o no é colocado em todosnos (filhos)
        if posicao_zero[0]+1<3:  ##checa se o 0 pode ser movido para baixo   (se linha da posicão zero +1 for maior que 2)
            matriz_baixo = deepcopy(matriz)
            matriz_baixo[posicao_zero[0]][posicao_zero[1]] = matriz_baixo[posicao_zero[0]+1][posicao_zero[1]] #coloca o valor de baixo onde o zero estava(em cima)
            matriz_baixo[posicao_zero[0]+1][posicao_zero[1]] = 0 #coloca o zero em baixo
            matriz_baixo_no = No(matriz_baixo, 'Baixo',self)
            todosnos.append(matriz_baixo_no)
        if not posicao_zero[1]-1<0: #(coluna) - 1 for menor que 0 ele não pode mover para a esquerda (pois ja esta na borda)
            matriz_esquerda = deepcopy(matriz)
            matriz_esquerda[posicao_zero[0]][posicao_zero[1]] = matriz_esquerda[posicao_zero[0]][posicao_zero[1]-1] #coloca o valor da esquerda onde o zero estava (a direita)
            matriz_esquerda[posicao_zero[0]][posicao_zero[1]-1] = 0 #coloca o zero a esquerda
            matriz_esquerda_no = No(matriz_esquerda,'Esquerda',self)
            todosnos.append(matriz_esquerda_no)
        if posicao_zero[1]+1<3: #y (coluna) + 1 for menor que 2 ele pode mover para a direita
            matriz_direita = deepcopy(matriz)
            matriz_direita[posicao_zero[0]][posicao_zero[1]] = matriz_direita[posicao_zero[0]][posicao_zero[1]+1] #coloca o valor da direita onde o zero estava (a esquerda)
            matriz_direita[posicao_zero[0]][posicao_zero[1]+1] = 0 #coloca o zero a direita
            matriz_direita_no = No(matriz_direita,'Direita',self)
            todosnos.append(matriz_direita_no)
        
        return todosnos
    
    # Guarda todos os pais do caminho_retorno de um nó.
    def caminho_retorno(self):#       Armazena em uma pilha todos os estados que foram passados, para futuramente, "desenhar" o caminho
        caminho = []
        caminho.append((self.Mover,self.matriz))
        n = self.Pai
        while n.Pai is not None:
            caminho.append((n.Mover,n.matriz))
            n = n.Pai
        caminho.append((n.Mover,n.matriz))
        caminho.reverse()
        return caminho

    def caminho_retorno_distancia(self):#.       Armazena em uma pilha todos os estados que foram passados, dita a distancia do nó atual até o nó raiz
        n = self.Pai
        d=0
        while n.Pai is not None:
            d = d + 1
            n = n.Pai
        return d

# Função de comparação da busca largura.
def comparacao(no, no2):               
    
    if no.matriz == no2.matriz: 
        return True
    else:
        return False

def CompMatriz(no,no2):
    for x in range(len(no2)):
        
        if no.matriz == no2[x].matriz:
            return False
    
    return True

# Função Busca em Largura
def busca_profundidade(no, objetivo):      #executando a busca em largura
    nocopia = copy.deepcopy(no) 
    abertos= [nocopia]              #abertos recebe a copia do no
    fechados = []
    filhos = []
        
        
    while (abertos !=[]):       #enquanto abertos for diferente de nulo
        x = abertos[-1]          #x recebe o valor mais a esquerda de abertos
        #print (x)
        if comparacao(x, objetivo): #compara, se x é o objetivo, se sim, retorna SUCESSO
            Desenha_Caminho(x.caminho_retorno())
            print("Quantos caminhos se mantiveram abertos: " + str(len(abertos)))
            print("Quantos caminhos foram fechados: " + str(len(fechados))+"\n") 
            return 0        #aqui ele entra
            
        else:
            
            Nosabertos = x.Gerar_Nos()      #encontra os filhos de x, vendo se estao em abertos ou fechados, e colocando em abertos os que nao estao nem em abertos nem em fechados
            
            for i in Nosabertos:
                if(CompMatriz(i,abertos + fechados)):
                    abertos.append(i)
                
                
                
        abertos.remove(x)
        fechados.append(x)

# Função Gulosa.
def Gulosa_Euclid(No_Inicial):

    abertos = pq() #priority queue, fila de prioridade. abertos
    fechados = []                       #fechados
    explorados = 0
    abertos.put((No_Inicial.Distan_Euclid(no_objetivo),No_Inicial)) #Coloca o nó inicial junto com a heuristica
    while not abertos.empty():  
       h, n = abertos.get() #abertos retorna uma heuristica e no.   remove um item com maior prioridade 
       if n.matriz in fechados:   #isto previne a repeticão de nós
           continue
       if h==0: #se a distancia for = 0 significa que ele esta no objetivo, portanto, retorna sucesso
           print('Sucesso!')
           Desenha_Caminho(n.caminho_retorno())
           print('O numero de nós explorados foram:%d'%explorados)
           return
       
       fechados.append(n.matriz)  #colocando n.matriz em fechados
       
       explorados+=1
       
       for nno in n.Gerar_Nos():      #pega os filhos, e os coloca na fila de prioridade, com a distancia euclidiana
           abertos.put((nno.Distan_Euclid(no_objetivo),nno))
           
def Gulosa_Numeros_Fora(No_Inicial):
    
    abertos = pq() #priority queue, fila de prioridade. abertos
    fechados = []                       #fechados
    explorados = 0
    abertos.put((No_Inicial.Num_Comp_Fora(no_objetivo),No_Inicial)) ##Coloca o nó inicial junto com a heuristica
    while not abertos.empty():  
       h, n = abertos.get() #abertos retorna uma heuristica e no.   remove um item com maior prioridade 
       if n.matriz in fechados:   #isto previne a repeticão de nós
           continue
       if h==0: #se a distancia for = 0 significa que ele esta no objetivo, portanto, retorna sucesso
           print('Sucesso!')
           Desenha_Caminho(n.caminho_retorno())
           print('O numero de nós explorados foram:%d'%explorados)
           return
       
       fechados.append(n.matriz)  #colocando n.matriz em fechados
       
       explorados+=1
       
       for nno in n.Gerar_Nos():      #pega os filhos, e os coloca na fila de prioridade, com o numero de componentes fora de posicao
           abertos.put((nno.Num_Comp_Fora(no_objetivo),nno))

def Aestrela(No_Inicial):

    abertos = pq() #priority queue, fila de prioridade. abertos
    fechados = []                       #fechados
    explorados = 0
    abertos.put((No_Inicial.Distanc_De_manhattan(no_objetivo),No_Inicial)) #coloca o primeiro no, com a heuristica de distancia de manhattan (nao foi colocada a distancia entre ele e o nó raiz pq ele é o próprio nó raiz :p)
    while not abertos.empty():  
       h, n = abertos.get() #remove um item com maior prioridade, com base na heuristica distancia de manhattan e  a distancia até o nó raiz
       if n.matriz in fechados:   #isto previne a repeticão de nós
           continue
       if n.Distanc_De_manhattan(no_objetivo)==0: #se a distancia de manhattan for = 0 significa que ele esta no objetivo, portanto, retorna sucesso (isso é apenas uma condicional para ver se chegou ao objetivo, porém sempre que um nó é adicionado é levado em consideracão a distância até o nó raiz)
           print('Sucesso!')
           Desenha_Caminho(n.caminho_retorno())
           print('O numero de nós explorados foram:%d'%explorados)
           return
       
       fechados.append(n.matriz)  #colocando n.matriz em fechados
       
       explorados+=1
       
       for nno in n.Gerar_Nos():      #pega os filhos, e os coloca na fila de prioridade, com a distancia de manhattan E A DISTANCIA DE RETORNO AO PAI
           abertos.put((nno.Distanc_De_manhattan(no_objetivo) + nno.caminho_retorno_distancia(),nno))

# Desenha a Matriz.         
def Desenha_Matriz(Caminho):
    print('+-+-+-+')
    for i in Caminho:
        print('|%d|%d|%d|'%(i[0],i[1],i[2]))
        print('+-+-+-+')
        
# Desenha o caminho.
def Desenha_Caminho(Caminho):
    for b in Caminho:
        print(b[0])
        Desenha_Matriz(b[1])
    print('Fim')
    print("tamanho caminho:", len(Caminho)) 

No_Inicial = No([[0,0,0],[0,0,0],[0,0,0]],'start')
no_objetivo = [[1,2,3],[4,5,6],[7,8,0]]
no_objetivodfs = No([[1,2,3],[4,5,6],[7,8,0]],'start')

# Entrada Manual.
def Entrada_Man(No_Inicial):
    Linha = []

    for i in range(3):
        Linha.append(input().split())

    for i in range(3):
        for j in range(3):
            Linha[i][j] = int(Linha[i][j])

    No_Inicial = Linha
    
    return No_Inicial

# Entrada Randomica.
def Entrada_Rand(No_Inicial):
    Linha = []

    i = 0

    while i < 9:
        x = random.randint(0,8)
        if(x not in Linha):
            Linha.append(x)
            i+=1

    No_Inicial[0][0] = Linha[0]
    No_Inicial[0][1] = Linha[1]
    No_Inicial[0][2] = Linha[2]
    No_Inicial[1][0] = Linha[3]
    No_Inicial[1][1] = Linha[4]
    No_Inicial[1][2] = Linha[5]
    No_Inicial[2][0] = Linha[6]
    No_Inicial[2][1] = Linha[7]
    No_Inicial[2][2] = Linha[8]
    return No_Inicial


Entrada = input("Qual tipo de entrada voce usara? Manual(1) Aleatoria(2)\n")
if(Entrada == '1'):
    No_Inicial.matriz = Entrada_Man(No_Inicial.matriz)
else:
    No_Inicial.matriz = Entrada_Rand(No_Inicial.matriz)

print("No original:\n+-+-+-+")
for i in No_Inicial.matriz:
    print('|%d|%d|%d|'%(i[0],i[1],i[2]))
    print("+-+-+-+")

if(No_Inicial.ESolucionavel(No_Inicial.matriz)):       #caso o no inicial não seja solucionável
    input("Pressione enter para a Gulosa com Euclidiana:")
    t_ini = time.time()
    Gulosa_Euclid(No_Inicial)
    t_fim = time.time()
    dif =  t_fim - t_ini
    print("dif:", dif)
    input("Pressione enter para a A* com Manhatam:")
    t_ini = time.time()
    Aestrela(No_Inicial)
    t_fim = time.time()
    dif =  t_fim - t_ini
    print("dif:", dif)
    input("Pressione enter para a Gulosa com Numeros Fora de posição:")
    t_ini = time.time()
    Gulosa_Numeros_Fora(No_Inicial)
    t_fim = time.time()
    dif =  t_fim - t_ini
    print("dif:", dif)
    input("Pressione enter para a Busca Profundidade:")
    t_ini = time.time()
    busca_profundidade(No_Inicial, no_objetivodfs)
    t_fim = time.time()
    dif =  t_fim - t_ini
    print("dif:", dif)
else:
    print("matriz não é solucionável")
    exit()