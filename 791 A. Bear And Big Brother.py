#CodeforcesProblema 791 A 
#Implementacion *600
#https://codeforces.com/contest/791/problem/A
#A. Bear And Big Brother 

a,b=list(map(int,input().split()))
i=0
while b>=a:
    i=i+1
    a=a*3
    b=b*2
print(i)
