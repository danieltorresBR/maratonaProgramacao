n=int(float(input())*100)
print("NOTAS:")
cem = int(n/10000)
restoCem = n%10000
print(cem, "nota(s) de R$ 100.00")

cinquenta = int (restoCem/5000)
restoCinquenta = restoCem%5000
print(cinquenta, "nota(s) de R$ 50.00")

vinte = int (restoCinquenta/2000)
restoVinte = restoCinquenta%2000
print(vinte, "nota(s) de R$ 20.00")

dez = int (restoVinte/1000)
restoDez = restoVinte%1000
print(dez, "nota(s) de R$ 10.00")

cinco = int (restoDez/500)
restoCinco = restoDez%500
print(cinco, "nota(s) de R$ 5.00")

dois = int (restoCinco/200)
restoDois = restoCinco%200
print(dois, "nota(s) de R$ 2.00")

print("MOEDAS:")
moedaHum = int (restoDois/100)
restoMoedaHum = restoDois%100
print(moedaHum, "moeda(s) de R$ 1.00")

moedaCinquenta = int (restoMoedaHum/50)
restoMoedaCinquenta = restoMoedaHum%50
print(moedaCinquenta, "moeda(s) de R$ 0.50")

moedaVinteCinco = int (restoMoedaCinquenta/25)
restoMoedaVinteCinco = restoMoedaCinquenta%25
print(moedaVinteCinco, "moeda(s) de R$ 0.25")

moedaDez = int (restoMoedaVinteCinco/10)
restoMoedaDez = restoMoedaVinteCinco%10
print(moedaDez, "moeda(s) de R$ 0.10")

moedaCinco = int (restoMoedaDez/5)
restoMoedaCinco = restoMoedaDez%5
print(moedaCinco, "moeda(s) de R$ 0.05")

moedaHumCentavo = int (restoMoedaCinco/1)
restoMoedaHumCentavo = restoMoedaCinco%1
print(moedaHumCentavo, "moeda(s) de R$ 0.01")
