##################################################################
##                                                              ##
##      CODIGO CRIADO PELO GRUPO TURING - POLI USP 2017         ##
##      https://www.facebook.com/grupoturing.poliusp            ##
##      Todos podem usar este codigo livremente                 ##
##                                                              ##
##################################################################

import pygame
import random


class Individuo():

    '''
    O individuo é o tomador de ações,

    Possui os atributos:
    -pesos: uma lista de floats utilizada para calcular a ação do indivíduo
             durante o jogo ex: ir para cima, para baixo ou ficar parado

    -score: um int que representa a pontuação associada
            à performance do indivíduo no final do jogo

    Possui as funções:
    -fitness: calcula o score do indivíduo

    -calcular_acao: calcula a ação tomada de acordo com os pesos e entradas
    '''

    def __init__(self, pesos):
        '''
        Este é o construtor de um indivíduo, ou seja, para gerar uma
        nova instância de indivíduo, o programa chama esta função.

        Ao criar um indivíduo, a notação em Python a ser seguida é:

            variavel = NomeDaClasse(atributo1, atributo2, etc.)

        O atributo (pesos) é o único a ser fornecido neste caso.

        Não é necessário escrever (self) ao criar um novo indivíduo.

        Exemplo: novo_individuo = Individuo([1.2123, 3.4123, -5.4123, ...])
                                                ^
                                                ^
                                             lista de pesos
        '''

        self.pesos = pesos
        self.score = 0

    def __str__(self):
        '''
        retorna o print do indivíduo, apresentando os pesos do mesmo
        de maneira mais fácil de ler.

        Ex: Suponha que tenhamos um indivíduo (ind1) com a
        seguinte lista de pesos:

        [1.214154,  3.414821, -5.4184512]

        Se executarmos o comando 'print(ind1)', teremos:

        >>>print(ind1)
        Pesos: 1.21  3.41 -5.41

        '''
        s = "   Pesos:"
        for i in range(len(self.pesos)):
            s += "%5.2f" % (self.pesos[i])

        s+= "  score = " + str(self.score)
        return s

# -------------------------------------------------------------------
    def fitness(self, gameState):
        '''
        Esta função determinará a pontuação de cada indivíduo ao final
        de uma rodada, atualizando o atributo score deste indivíduo.

        OBJETIVO: Implementar a função fitness, que avalia o desempenho
                  de um indivíduo e atualiza o atributo (self.score).

        Essa função recebe como entrada a variável gameState,
        que é uma lista com informações do jogo. A partir dela,
        é possível saber quando o jogo acaba.

            Informações em cada posição da lista:

                gameState[0] = player.y (float, normalizado de -1 a +1)
                gameState[1] = ball.x   (float, normalizado de -1 a +1)
                gameState[2] = ball.y   (float, normalizado de -1 a +1)
                gameState[3] = ball.speed_x
                gameState[4] = ball.speed_y
                gameState[5] = numBat (int, número de vezes que a bola
                               tocou o Player)
                gameState[6] = ganhou (boolean, se o player sobreviveu
                               o tempo definido (TRUE) ou não (FALSE) )

        Perceba que gameState será fornecida a partir do programa do jogo,
        que é um código pronto, no qual vocês não devem fazer modificações.

        Sejam criativos, e imaginem quais dos parâmetros acima
        vocês deveriam usar para avaliar o desempenho de um jogador de Pong

        APAGUE O TRECHO "pass" ao final desta função
        ESCREVA código necessário para implementá-la.

        Lembre-se de apagar o trecho "pass" nas funções seguintes
        '''
        self.score = 0
        for i in range(5):
            self.score -= pow(self.pesos[i], 2) / 25
        self.score += gameState[5]/30
# -------------------------------------------------------------------

# -------------------------------------------------------------------
    def calcular_acao(self, entrada):
        '''
        Esta função calculará a ação do indivíduo durante o jogo

        OBJETIVO: Implementar a decisão a partir dos pesos (self.pesos)
                  e da lista com valores de entradas (entrada).

        Aqui se faz a decisão de subir, descer ou permanecer
        parado com o cursor do jogador.

        O vetor de entradas possui 5 elementos: player.y, ball.x,
        ball.y, ball.speed_x, ball.speed_y

        Teoricamente, não é necessário saber as posições destas entradas.

        Utilizando esses parâmetros de entrada em combinação com
        os pesos atribuídos a cada um deles, deve-se retornar o int (Acao)

            Dicas: Essa função deve retornar -1 (sobe), 0(parado)
                   ou +1(desce).

                   As listas "self.pesos" e "entradas" tem que ter o
                   mesmo tamanho.

        Lembre-se: Você não deve resolver manualmente qual decisão
        o indivíduo deve tomar para cada caso, pois a inteligência
        artificial é que deverá descobrir os melhores pesos sozinha.
        '''
        # COMPLETE AQUI:
        # multiplicar as entradas pel
        # return Acao (-1, 0 ou 1)
        decision = 0

        for idx, v in enumerate(entrada):
            decision += self.pesos[idx] * v

        if decision < -0.33:
            return -1
        if decision < 0.33:
            return 0
        return 1
# -------------------------------------------------------------------

# -------------------------------------------------------------------
    def gera_individuo_aleatorio(self):
        '''
        OBJETIVO: criar um novo indivíduo com uma lista de
        pesos gerada aleatoriamente.

        Crie uma lista com 5 floats aleatórios
        Dica: a função random.random() retorna um float entre 0 e 1

        ex: valor_aleatorio = random.random()

        Use sua criatividade para também gerar valores negativos.

        Chame o contrutor da classe Individuo usando
        a lista de floats que você criar como argumento.

        '''
        lista_floats = []
        # COMPLETE AQUI:
        for i in range(5):
            lista_floats.append(random.gauss(0, .5))

        return Individuo(lista_floats)


#################################################################################################


class Geracao():

    '''
    A Geracao é onde ocorre toda a evolução,

    Esta classe possui o atributo:
           -individuos: uma lista de objetos da classe Individuo

    E possui as funções:
           -selecao
           -reproduzir
           -CrossOver
           -Mutacao
    '''

# -------------------------------------------------------------------
    def __init__(self, numInd):
        '''
        Este é o construtor de uma geração.

        O objeto Geracao deve ter um atributo (individuos), que é
        uma lista de indivíduos.

        Para isso, crie uma lista de indivíduos com (numInd) indivíduos,
        cada um com uma distribuição randômica de pesos
        que contenha 5 pesos.

        Dica: use a função gera_individuo_aleatorio() da classe Individuo
        '''
        individuos = []
        # COMPLETE AQUI:
        for i in range(numInd):
            individuos.append(Individuo.gera_individuo_aleatorio(Individuo))

        self.individuos = individuos

# -------------------------------------------------------------------

    def __str__(self):
            # nao precisa mexer aqui
            # retorna o print do individuo facil de ler
        for i in range(len(self.individuos)):
            print("Individuo %d:" % i)
            print(self.individuos[i])
        return ''


# -------------------------------------------------------------------


    def selecao(self, numSelec=4):
        '''
        OBJETIVO: selecionar os melhores indivíduos e eliminar os demais
                da lista comparando os scores. Manipule a lista de modo
                que apenas os melhores permaneçam na geração.
                Para isso, encontre os melhores individuos percorrendo a lista

                A lista atualizada deverá ter tamanho (numSelec).

                Dicas: O python permite mudar o tamanho das listas,
                       logo não é necessário criar uma nova lista.

                       Essa função não precisa retornar nada,
                       apenas alterar variáveis já existentes
        '''
        l = len(self.individuos)
        for i in range(l - numSelec):
            min = 0
            for j in range(l - i):
                if self.individuos[j].score < self.individuos[min].score:
                    min = j
            del self.individuos[min]


# -------------------------------------------------------------------

# -------------------------------------------------------------------


    def CrossOver(self, individuo1, individuo2, chanceCO=0.2):
        '''
        O Crossing-Over consiste em trocar trechos de indivíduos.
        No nosso exemplo, deveremos sortear aleatoriamente uma posicao
        da lista de pesos e permutar os pesos dessa posicao entre dois
        indivíduos. Esta permutacao deverá ocorre com chanceCO.

        OBJETIVO: Aplicar o crossing over com (chanceCO) de acontecer.

            Para isso, voce deve receber 2 objetos do tipo individuo.
            Lembrem-se que os valores trocados devem ter o mesmo locus!
            "Gene de cabelo nao troca com gene de olho"
            Dicas: A função random.random() retorna um float
                   aleatório entre 0 e 1.

                   A função CrossOver não precisa retornar nada,
                   apenas alterar individuo1 e individuo2 já existentes.
        '''

        if(random.random() < chanceCO):
            index = random.randint(0, len(individuo1.pesos)-1)
            individuo1.pesos[index], individuo2.pesos[index] = individuo2.pesos[index], individuo1.pesos[index]


# -------------------------------------------------------------------

# -------------------------------------------------------------------


    def Mutacao(self, individuo, chanceMut=0.05):
        '''
         OBJETIVO: Aplicar uma mutação com (chanceMut) de chance em cada peso do (individuo)
                 Existem diversas maneiras de fazer isso
                 Sugerimos fortemente que a mutação seja multiplicar o peso por um valor randômico entre -1.1 e 1.1
                 dica: a funcao random.random() retorna um float entre 0 e 1
                 dica: essa funcao nao precisa retornar nada, apenas alterar individuo já existente
        '''
        for i in range(len(individuo.pesos)):
            if(random.random() < chanceMut):
                individuo.pesos[i] *= random.random()*2.2 - 1.1

# -------------------------------------------------------------------

# -------------------------------------------------------------------
#
#
    def reproduzir(self, chanceCO, chanceMut, m=10):
        print('> Reproduzir()')
        '''
        OBJETIVO:
                Aumentar o numero de individuos para (m) individuos
                e aplicar o crossing over e a mutacao nos novos individuos
                Use os individuos anteriores para criar os proximos
                Existem diversas maneiras de fazer isso

                dica: voce deve chamar as funcoes CrossOver e Mutacao (faca elas primeiro)
                dica: Cuidado! Se voce fizer individuoA = individuoB,
                        O python passara por referencia e toda mudanca que voce fizer em individuoA, ocorrera no individuoB (e vice-versa).
                        O mesmo vale para listas
                        O jeito correto de fazer isso e: individuoA = individuoB(individuoA.pesos[:])
                        (Nao necessariamente voce vai precisar usar isso, foi so um aviso previo que faz muita gente erra por motivos de python)
                dica: essa funcao nao precisa retornar nada, a geracao e alterada globalmente
        '''
        newIndividuals = []
        n = len(self.individuos)
        for i in range(m - n):
            tmp = Individuo(self.individuos[i%n].pesos[:])
            self.Mutacao(tmp)
            # para criar um indice 'pseudoaleatorio'
            newIndex = (i + n//2) % n
            Geracao.CrossOver(Individuo, tmp, self.individuos[newIndex])

            newIndividuals.append(tmp)

        for ind in self.individuos:
            newIndividuals.append(ind)

        self.individuos = newIndividuals

        return
# -------------------------------------------------------------------
