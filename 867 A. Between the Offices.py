#Problema 867 A
#implementación *600
#https://codeforces.com/problemset/problem/867/A
#Between the Offices

d=int(input())
v=input()
i=0;vs=0;vf=0

while i<d-1:
    if v[i]=="F" and v[i+1]=="F":
        i=i+1
        
    elif v[i]=="S" and v[i+1]=="S":
        i=i+1
        
    elif v[i]=="S" and v[i+1]=="F":
        vs=vs+1
        i=i+1
        
    elif v[i]=="F" and v[i+1]=="S":
        vf=vf+1
        i=i+1
        
if vf>=vs:
    print("NO")
else:
    print("YES")
