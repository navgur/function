from re import I


def square():
    i=1
    b=[]
    l=[]
    while i<=5:
        c=i*i
        b.append(c)
        i=i+1    
    j=26
    k=[]
    while j<=30:
        d=j*j
        k.append(d)
        j=j+1
    l.append(b)
    l.append(k)
    print(l)
square()    

