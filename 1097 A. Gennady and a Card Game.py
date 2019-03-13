#Codeforces Problema 1097 A
#implementacion *600
#https://codeforces.com/problemset/problem/1097/A
#A. Gennady and a Card Game

cMesa=input()

c1,c2,c3,c4,c5 = list(map(str,input().split()))

if c1[1]==cMesa[1] or c1[0]==cMesa[0]:
    resul="YES"
    
elif c2[1]==cMesa[1] or c2[0]==cMesa[0]:
    resul="YES"
    
elif c3[1]==cMesa[1] or c3[0]==cMesa[0]:
    resul="YES"
    
elif c4[1]==cMesa[1] or c4[0]==cMesa[0]:
    resul="YES"
    
elif c5[1]==cMesa[1] or c5[0]==cMesa[0]:
    resul="YES"
 
else:
    resul="NO"

print(resul)
