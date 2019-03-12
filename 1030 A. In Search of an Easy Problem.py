#Problema 1030  A
#implementacion *500
#https://codeforces.com/problemset/problem/1030/A
#In Search of an Easy Problem

n = int(input())
array =list(map(int,input().split(" ")))
i=0; suma=0
while i<n:
    print(array[i])
    suma=suma+array[i]
    i=i+1    
if suma>0:
    print("HARD")
else:
    print("EASY")
