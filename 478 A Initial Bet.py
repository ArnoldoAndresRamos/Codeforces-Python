#Codeforces Problema 478 A
#implementacion *1200
#https://codeforces.com/problemset/problem/478/A
#Initial Bet

c1,c2,c3,c4,c5=list(map(int,input().split()))

total=c1+c2+c3+c4+c5
if total%5==0:
    resul=total/5
else:
    resul=-1
    
print(int(resul))
