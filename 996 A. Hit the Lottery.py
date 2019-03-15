#Codeforces Problema 996 A
#programación dinamica, Algoritmo voraz *600 
#https://codeforces.com/contest/996/problem/A
#Hit the Lottery

n=int(input())
b=n%100;
n=n-b;
i=n/100;
 
if b<100:
    while b>=20:
        b=b-20;
        i=i+1;
if b<20:
     while b>=10:
        b=b-10
        i=i+1
        
if b<10:
    while b>=5:
        b=b-5
        i=i+1
		        
if b<5:
    while b>=1:
        b=b-1
        i=i+1
        
print(int(i))
