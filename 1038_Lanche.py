a,b = input().split()

a = int(a)#codigo
b = int(b)#quantidade

if (a==1):
    total = b*4.00
elif (a==2):
    total = b*4.50
elif (a==3):
    total = b*5.00
elif (a==4):
    total = b*2.00
elif (a==5):
    total = b*1.50

print ("Total: R$ "'{:.2f}'.format(total))