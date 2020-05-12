n=int(input())
hora = int(n/3600)
restoHora = n%3600

minuto = int(restoHora/60)
restoMinuto = restoHora%60

print(hora,minuto,restoMinuto, sep=":")
