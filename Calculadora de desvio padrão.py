import math

n = int(input("O valor de n:"))
f = list()

count = 0
while count < n:
    x = float(input("Valor:"))
    f.append(x)
    count += 1

a = 0   
for i in f:
    a += i
    
x1= a/(len(f))
g = list()

for i in f:
    b = i**2 - 2*i*x1 + x1**2
    g.append(b)

d = 0
for i in g:
    d += i
    
Dp = (d/(n-1))**(1/2)
I = (Dp/x1)*100

print('Valor médio:{:.3f}'.format(x1))
print('Desvio padrão:{:.3f}'.format(Dp))
print('A medida tem uma incerteza de:{:.2f}'.format(I),"%") 
    
