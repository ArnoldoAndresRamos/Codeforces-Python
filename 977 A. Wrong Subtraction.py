#codeforces Problema 977 A 
#Implementacion *500 
#https://codeforces.com/problemset/problem/977/A
#A. Wrong Subtraction 


n,k=list(map(int,input().split(" ")))
i=0
while i<k:
    ultimoNumero=n%10
    if ultimoNumero!=0:
        n=n-1
    else:
        n=n/10
    i+=1
print(int(n))
