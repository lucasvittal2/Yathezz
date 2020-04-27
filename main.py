from InstanciaJogo import *
from partida import *
from jogador import *


def loop_jogo():
    i = 1
    j=0

    while(j<13):
        while(i <= get_num_jogadores()):
            nome=get_nome_ind(i)
            print("Vez de "+ nome)
            dados=lanca_dados(nome)

            secao_tab=input('Que secçao da tabela deseja escolher?(inferior ou superior)')
            comp_tabela=input('Que componente ta tabela deseja escolher?')
            val=calc_Pontuacao(dados,comp_tabela,nome)
            manipula_tabela(nome,secao_tab,comp_tabela,val)
            i=i+1
        j=j+1
    calc_Vencedor()
    resp=input("Deseja jogar novamente?(S(Sim) ou N(Nao)")
    if resp=='S':
        loop_jogo()

#test: Essa parte é descartável.
Inst_jogo()
print("Partidas: " + str(get_partidas()) +"\n" + "num_jogadores: " + str(get_num_jogadores()) + "\n" )
print(get_num_jogadores())
loop_jogo()
