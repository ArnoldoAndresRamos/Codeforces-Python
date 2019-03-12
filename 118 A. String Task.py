#codeforces Problema 118 A
#implementación, string  *1100
#https://codeforces.com/contest/118/problem/A
#A.String Task

z=input()
x=z.lower()#convierte a minuscula
i=0; e=0; array=[]

while i<len(x):
    if x[i]=="a" or x[i]=="e" or x[i]=="i" or x[i]=="o" or x[i]=="u" or x[i]=="y":
         array.append("")
    else:
        array.append(".")
        array.append(x[i])
    i=i+1
    
resul=''.join(array)# ''.join()convierte una lista en cadena
print(resul)
