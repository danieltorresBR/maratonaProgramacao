verticeTriagulo = input().split()

a = float(verticeTriagulo[0])
b = float(verticeTriagulo[1])
c = float(verticeTriagulo[2])


if((abs(b-c))<a<(b+c) and (abs(a-c))<b<(a+c) and (abs(a-b))<c<(a+b)):
      print('Perimetro = {:.1f}'.format(a+b+c))
else:
      print('Area = {:.1f}'.format(((a+b)/2)*c))
