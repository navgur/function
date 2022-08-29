def even():
    list=[3,6,4,2,3,4,5] 
    i=0
    a=[]
    while i<len(list):
        if list[i]%2==0:
            a.append(list[i])
        i=i+1
    print(a)    
even()               

