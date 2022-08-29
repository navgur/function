def sort():
    k=[3,4,5,6,7,8,3,4]
    i=0
    b=[]
    while i<len(k):
        if k[i]<=5:
            b.append(k[i])
        i=i+1
    print(b)
sort()    
