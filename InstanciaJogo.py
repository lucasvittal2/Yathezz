import copy
#Instanciando Objeto do Jogo
__all__ = ["Inst_jogo","manipula_tabela","get_partidas","get_num_jogadores","get_tabJogadores","get_Yahtzee","get_jogador","get_nome_ind","get_pt_total","exibe_tabela"]

#Objetos
Jogadores =[]
dados = [0]*5
tabela = [[0,0,0,0,0,0,0],[0,0,0,0,0,[0,0,0],0]]

    #""""""{
     #   "sc_superior":
      #  {"Um": 0,"Dois": 0, "Tres": 0, "Quatro": 0,
       #   "Cinco": 0,"Seis": 0, "pts_total":0,"Bonus":0,
        #  "Total_sc_superior":0},
        #"sc_inferior":
        #{"trinca": 0, "Quadra": 0,"full_house":0,
        # "seq_max":0,"seq_min":0, "yahtzee":[0]*3,
        #"chance":0
         #}
         #}""""""
#Variáveis Globais
num_jogadores=0
partidas = 0

#funções:
def Inst_jogo():
    global num_jogadores
    global partidas
    global tabela
    global Jogadores
    nome = ""
    aux_jogadores= []
    aux_tabela = {}
    num_jogadores = int(input("Qual o número  de jogadores ?\n"))
    i = 0
    while(i < num_jogadores):
        nome = input("Qual o nome do jogador" + str(i+1) + " ?\n")
        aux_tabela = copy.deepcopy(tabela)
        Jogadores.append([nome, aux_tabela])
        i+=1
    partidas = input("Quantas terá o partidas jogo ?\n")

def procura_jogador(nome):
    global Jogadores
    i = 0
    while (Jogadores[i][0] != nome):
        i += 1
        if (i > num_jogadores - 1):
            print("*****************************\n")
            print("Erro: Jogador não encontrado!\n")
            return None
    return i

def manipula_tabela(nome_jogador,secao_tab,componente_tab, novo_val):
    global Jogadores
    global num_jogadores
    if(novo_val < 0):
        print("Erro: novo valor inválido\n")
        return
    i = procura_jogador(nome_jogador)
    if(i == None):
        return


    if secao_tab == "superior":
        print("entrou sc sup\n")
        if componente_tab == "um":
            if Jogadores[i][1][0][0]!= 0:
                print("Erro, não foi possível atualizar 'um'. Número de atualizações exedida\n")
                return
            Jogadores[i][1][0][0] = novo_val
        elif componente_tab == "dois":
            if Jogadores[i][1][0][1]!= 0:
                print("Erro, não foi possível atualizar 'dois'. Número de atualizações exedida\n")
                return
            Jogadores[i][1][0][1] = novo_val
        elif componente_tab == "tres":
            if Jogadores[i][1][0][2]!= 0:
                print("Erro, não foi possível atualizar 'tres'. Número de atualizações exedida\n")
            Jogadores[i][1][0][2] = novo_val
        elif componente_tab == "quatro":

            if Jogadores[i][1][0][3]!= 0:
                print("Erro, não foi possível atualizar 'quatro'. Número de atualizações exedida\n")
                print(Jogadores[i])
            Jogadores[i][1][0][3] = novo_val
        elif componente_tab == "cinco":
            if Jogadores[i][1][0][4]!= 0:
                print("Erro, não foi possível atualizar 'cinco'. Número de atualizações exedida\n")
            Jogadores[i][1][0][4] = novo_val
        elif componente_tab == "seis":
            if Jogadores[i][1][0][5]!= 0:
                print("Erro, não foi possível atualizar 'seis'. Número de atualizações exedida\n")
            Jogadores[i][1][0][5] = novo_val
        elif componente_tab == "pts_total":
            if Jogadores[i][1][0][6]!= 0:
                print("Erro, não foi possível atualizar 'pt_total'. Número de atualizações exedida\n")
            Jogadores[i][1][0][6] = novo_val
        else:
            print("Compenente inexistente na seção superior!\n")
    elif secao_tab == "inferior":
        if componente_tab == "trinca":
            if Jogadores[i][1][1][0]!= 0:
                print("Erro, não foi possível atualizar 'trinca'. Número de atualizações exedida\n")
                return
            Jogadores[i][1][1][0] = novo_val
        elif componente_tab == "quadra":

            if Jogadores[i][1][1][1]!= 0:
                print("Erro, não foi possível atualizar 'quadra'. Número de atualizações exedida\n")
                return
            Jogadores[i][1][1][1] = novo_val
        elif componente_tab == "fullhouse":
            if Jogadores[i][1][1][2]!= 0:
                print("Erro, não foi possível atualizar 'full_house'. Número de atualizações exedida\n")
                return
            Jogadores[i][1][1][2] = novo_val
        elif componente_tab == "seqmax":
            if Jogadores[i][1][1][3]!= 0:
                print("Erro, não foi possível atualizar 'seq_max'. Número de atualizações exedida\n")
                return
            Jogadores[i][1][1][3] = novo_val
        elif componente_tab == "seqmin":
            if Jogadores[i][1][1][4]!= 0:
                print("Erro, não foi possível atualizar 'seq_min'. Número de atualizações exedida\n")
                return
            Jogadores[i][1][1][4] = novo_val
        elif componente_tab == "yahtzee":
            if(Jogadores[i][1][1][5][0] == 0):
                Jogadores[i][1][1][5][0] = novo_val
            elif(Jogadores[i][1][1][5][1] == 0):
                Jogadores[i][1][1][5][1] = novo_val
            elif (Jogadores[i][1][1][5][2] == 0):
                Jogadores[i][1][1][5][2] = novo_val
            else:
                print("Atenção: número de yathezz excedido, não foi possível realizar alteração\n")
        elif componente_tab == "chance":
            if Jogadores[i][1][1][6]!= 0:
                print("Erro, não foi possível atualizar 'chance'. Número de atualizações exedida\n")
                return
            Jogadores[i][1][1][6] = novo_val
        else:
            print("Erro:Compenente inexistente na seção inferior!\n")
    else:
        print("Erro: Seção inexistente na tabela.\n")


def get_partidas():
    return partidas;
def get_num_jogadores():
    return num_jogadores;

def get_Yahtzee(nome_Jogador):
    lista=get_Jogador(nome_Jogador)
    if (lista[1][1][5][0]==50):
        return True
    else:
        return False
    
def get_tabJogadores():
    return Jogadores
def get_jogador(nome):
    i=0
    global Jogadores
    while(Jogadores[i][0] != nome):
        i+=1
        if(i >=len(Jogadores)):
            print("Jogador não encontrado\n")
            return None
    return Jogadores[i]
def get_nome_ind(ind):
    global Jogadores
    if(ind <= len(Jogadores) ):
        return Jogadores[ind - 1][0]
    print("Jogador não existente")
    return None
def get_pt_total(nome_jogador):

    i = procura_jogador(nome_jogador)
    if(i==None):
        return
    return Jogadores[i][1][0][5]
def exibe_tabela(nome_jogador):
    i = procura_jogador(nome_jogador)
    if(i==None):
        return
    print("Tabela do " + nome_jogador + " " +"\n"
          + "Seção superior\n" +
          "Um: " + str(Jogadores[i][1][0][0]) +"\n"+
          "Dois: " + str(Jogadores[i][1][0][1]) +"\n"+
          "Três: " + str(Jogadores[i][1][0][2]) +"\n"+
          "Quatro: " + str(Jogadores[i][1][0][3]) +"\n"+
          "Cinco: " + str(Jogadores[i][1][0][4]) +"\n"+
          "Seis: " + str(Jogadores[i][1][0][5]) +"\n"+
          "Ponto Total: " + str(Jogadores[i][1][0][6]) +"\n"+
          "Seção inferior\n" +
          "Trinca: " + str(Jogadores[i][1][1][0]) + "\n" +
          "Quadra: " + str(Jogadores[i][1][1][1]) + "\n" +
          "Full House: " + str(Jogadores[i][1][1][2]) + "\n" +
          "Seq Máx: " + str(Jogadores[i][1][1][3]) + "\n" +
          "Seq Mín: " + str(Jogadores[i][1][1][4]) + "\n" +
          "Yathezz: " + str(Jogadores[i][1][1][5][0]) + " " + str(Jogadores[i][1][1][5][1]) + " " + str(Jogadores[i][1][1][5][2]) + "\n" +
          "Chance: " + str(Jogadores[i][1][1][6]) + "\n"
          )

