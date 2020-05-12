entrada = input().split()

inicio = int(entrada[0])
fim = int(entrada[1])

if(inicio>fim):
     tempo = (24-inicio)+fim
     print("O JOGO DUROU", tempo,"HORA(S)")

elif(inicio<fim):
     tempo = fim-inicio
     print("O JOGO DUROU", tempo,"HORA(S)")

elif(inicio==fim):
     print("O JOGO DUROU 24 HORA(S)")
