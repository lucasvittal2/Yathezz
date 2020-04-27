from jogador import *
from collections import Counter
quant_update = { "um" : 0 , "dois" : 0 , "tres": 0 , "quatro" : 0 , "cinco": 0 , "seis": 0, "trinca": 0 , "quadra": 0 ,"fullhouse":0,"yathezz": 0,
                 "seq_max": 0 , "seq_min": 0 , "chance":0}
__all__ = ["calc_Pontuacao","calc_Vencedor","get_upate"]

#SECÇAO SUPERIOR

def calc_Num(num,dados):
    i=0
    Soma=0;
    while(i<5):
        if(dados[i]==num):
            Soma=Soma+num
        i=i+1
    return Soma

#SECÇAO INFERIOR

# Se Trinca -> num = 3, Se Quadra -> num = 4
def calc_Rep(num,dados):
    Soma=0
    lista=Counter(dados).values()
    if(num in lista):
        Soma= dados[0] + dados[1] + dados[2] + dados [3] + dados[4]
    return Soma
       

def calc_FullHouse(dados):
    Pont=0
    lista=Counter(dados).values()
    if((2 in lista) and (3 in lista)):
        Pont=25
    return Pont

def calc_SeqMin(dados):
    Pont=0
    if ((1 and 2 and 3 and 4 in dados) or (2 and 3 and 4 and 5 in dados) or (3 and 4 and 5 and 6 in  dados)):        
        Pont=30
    return Pont

def calc_SeqMax(dados):
    Pont=0
    if ((1 and 2 and 3 and 4 and 5 in dados) or (2 and 3 and 4 and 5 and 6 in dados)):        
        Pont=40
    return Pont

def calc_Yathzee(dados,nome):
    if calc_Rep(5,dados)!=0:
        if get_Yahtzee(nome):
            return 100      
        else:
            return 50
    else:
        return 0

def calc_Chance(dados):
    if(quant_update["yathezz"] > 1):
        return dados[0] + dados[1] + dados[2] + dados [3] + dados[4]
    else:
        return 0

#TOTAL    
    
def calc_Pontuacao(dados,comp_tabela,nome):
    global quant_update
    comp_tabela=comp_tabela.lower()
    if comp_tabela=="um":
        if(quant_update["um"] <=1):
            val=calc_Num(1,dados)
            quant_update["um"] +=1
    elif comp_tabela=="dois":
        if (quant_update["dois"] <= 1):
            val=calc_Num(2,dados)
            quant_update["dois"] += 1
    elif comp_tabela=="tres":
        if (quant_update["tres"] <= 1):
            val=calc_Num(3,dados)
            quant_update["tres"] += 1
    elif comp_tabela=="quatro":
        if (quant_update["quatro"] <= 1):
            val=calc_Num(4,dados)
            quant_update["quatro"] += 1
    elif comp_tabela=="cinco":
        if (quant_update["cinco"] <= 1):
            quant_update["cinco"] += 1
            val=calc_Num(5,dados)
    elif comp_tabela=="seis":
        if (quant_update["seis"] <= 1):
            val=calc_Num(6,dados)
            quant_update["seis"] += 1
    elif comp_tabela=="trinca":
        if (quant_update["trinca"] <= 1):
            val=calc_Rep(3,dados)
            quant_update["trinca"] += 1
    elif comp_tabela=="quadra":
        if (quant_update["quadra"] <= 1):
            val=calc_Rep(4,dados)
            quant_update["quadra"] += 1
    elif comp_tabela=="fullhouse":
        if (quant_update["fullhouse"] <= 1):
            val=calc_FullHouse(dados)
            quant_update["fullhouse"] += 1
    elif comp_tabela=="seqmin":
        if (quant_update["seqmin"] <= 1):
            val=calc_SeqMin(dados)
            quant_update["seqmin"] += 1
    elif comp_tabela=="seqmax":
        if (quant_update["seqmax"] <= 1):
            val=calc_SeqMax(dados)
            quant_update["seqmax"] += 1
    elif comp_tabela=="yahtzee":
        if (quant_update["yahtzee"] <= 3):
            val=calc_Yahtzee(dados,nome)
            quant_update["yahtzee"] += 1
    elif comp_tabela=="chance":
        if (quant_update["chance"] <= 1):
            val=calc_Chance(dados)
            quant_update["chance"] += 1
    if(checa_bonus()):
        val+=35

def checa_bonus():
    global quant_update
    soma =quant_update["um"] + quant_update["dois"] + quant_update["tres"] + quant_update["quatro"]+quant_update["cinco"] + quant_update["seis"]
    if(soma < 6):
        bonus = False
    else:
        bonus = True
    return bonus



    
    



def calc_PontSup(nome):
    lista=get_jogador(nome)
    Soma=0   
    while i<7:
        Soma= Soma + lista[1][0][i]
        i=i+1
    if Soma>62:
        Soma= Soma + 35
    return Soma


def calc_PontInf(nome):
    lista=get_jogador(nome)
    i=0
    j=0
    while i<5:
        Soma= Soma + lista[1][1][i]
        i=i+1
    while j<3:
        Soma= Soma + lista[1][1][5][j]
        j=j+1    
    Soma = Soma + lista[1][1][6]
    return Soma
def get_upate(comp_tab):
    global quant_update
    return quant_update[comp_tab]

def calc_PontTotal(nome):
    return calc_PontSup(nome) + calc_PontInf(nome)

def calc_Vencedor():
    i=0
    j=0
    PtMax=0
    pessoas=[]
    while(i<3):
        nome=get_nome_ind(i)
        Pt=calc_PontTotal(nome)
        pessoas.append([nome,Pt])
        if(Pt>PtMax):
            PtMax=Pt
        i=i+1
    print("O(s) vencedor(es) é(sao):")
    while(j<3):
        if(pessoas[j][1]==PtMax):
           print(pessoas[j][0])

    
    






