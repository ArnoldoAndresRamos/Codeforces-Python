#Codeforces Problema 935 A
#implementacion *600
#https://codeforces.com/problemset/problem/935/A
#Fafa and his Company

n=int(input())
l=1
f=0

while l < n:
    if (n-l)%l == 0:
        f=f+1
    l=l+1    
print(f)
