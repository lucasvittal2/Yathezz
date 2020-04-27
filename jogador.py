from random import *
from InstanciaJogo import *
from partida import *


__all__ = ["lanca_dados","identificaResultado"]

#lança dados 1 vez
def aux_dados(numDados):
    dados=[0]*numDados
    i=0
    a=0
    while(i< numDados):
        a=randint(1,6)
        dados[i]=a
        i=i+1
    return dados

#funçao que pega indices de dados p/ relancar e relanca dados
def relanca(d1,d2):
    i=0
    a=0
    #d1=[0,1,4]
    #d2=[5,3,1,1,4]
    print(d1,d2)
    print(len(d1))
    while(i<len(d1) - 1):
        a=d1[i]
        d2[a]=randrange(1,6)
        i=i+1
    identificaResultado(d2)
    return d2    
        
#fucao transformar lista de string em int
# ["3","4","5""] --> [3,4,5]
def str_Int(lista):
    i=0
    while(i<len(lista)):
        lista[i]=int(lista[i])
        i=i+1
    return lista
def identificaResultado(dados):
    resultados = []

    if( 1 in dados and get_upate("um") < 1):
        resultados.append("um")
    if (2 in dados and get_upate("dois") < 1):
        resultados.append("dois")
    if(3 in dados and get_upate("tres") < 1):
        resultados.append("tres")
    if(4 in dados and get_upate("quatro") < 1):
        resultados.append("quatro")
    if(5 in dados and get_upate("cinco") < 1):
        resultados.append("cinco")
    if(6 in dados and get_upate("seis") < 1):
        resultados.append("seis")
    if(calc_FullHouse(dados) != 0 and get_upate("fullhouse") < 1):
        resultados.append("fullhouse")
    if(calc_Rep(3,dados) != 0 and get_upate("trinca") < 1):
        resultados.append("trinca")
    if (calc_Rep(4, dados) != 0 and get_upate("quadra") < 1 ):
        resultados.append("quadra")
    if (calc_SeqMin(dados) !=0 and get_upate("seq_min") < 1):
        resultados.append("seq_min")
    if (calc_SeqMax(dados) != 0 and get_upate("seq_max") < 1):
        resultados.append("seq_max")
    if(calc_Yathzee(dados) != 0 and get_upate("yathezz") < 3 ):
        resultados.append("yathezz")
    if(calc_Chance(dados) !=0):
        resultados.append("chance")
    print("**** Possiveis Resultados  **** \n")
    print(resultados)
          

def lanca_dados(nome):
    dados=aux_dados(5)
    print(dados)
    #exibe_Possibilidades(dados,nome)

    identificaResultado(dados)
    resp=input("Jogar os dados novamente (S(Sim) ou N(Nao))?")
    if(resp=="N"):
        return dados
    else:
        respD=input("Quais os índices dos dados quer relançar?(Ex:0,3,4 - Sem espaço entre as vírgulas)")
        Dados_relanc=str_Int(respD.split(","))
        print(Dados_relanc)
        print("\n")
        relanca(Dados_relanc,dados)
        print(dados)
        #exibe_Possibilidades(dados,nome)
        resp=input("Jogar os dados novamente (S(Sim) ou N(Nao))?")
        if(resp=="N"):
            return dados
        else:
            respD=input("Quais os índices dos dados quer relançar?(Ex:0,3,4 - Sem espaço entre as vírgulas)")
            Dados_relanc=str_Int(respD.split(","))
            relanca(Dados_relanc,dados)
            print(dados)
            #exibe_Possibilidades(dados,nome)
            return dados

