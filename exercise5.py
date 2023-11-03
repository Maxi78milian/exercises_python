
r=0.5
a=1
n=10
sn=0
s_n=[]
for k in range(1,n+1):
    sn+=a*r**(k-1)
    s_n.append(sn)
    
print(s_n)

