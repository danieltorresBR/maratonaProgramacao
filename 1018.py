n=int(input())
print(n)
cem = int(n/100)
restoCem = n%100
print(cem, "nota(s) de R$ 100,00")

cinquenta = int (restoCem/50)
restoCinquenta = restoCem%50
print(cinquenta, "nota(s) de R$ 50,00")

vinte = int (restoCinquenta/20)
restoVinte = restoCinquenta%20
print(vinte, "nota(s) de R$ 20,00")

dez = int (restoVinte/10)
restoDez = restoVinte%10
print(dez, "nota(s) de R$ 10,00")

cinco = int (restoDez/5)
restoCinco = restoDez%5
print(cinco, "nota(s) de R$ 5,00")

dois = int (restoCinco/2)
restoDois = restoCinco%2
print(dois, "nota(s) de R$ 2,00")

hum = int (restoDois/1)
restoHum = restoDois%1
print(hum, "nota(s) de R$ 1,00")
