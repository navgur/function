def count():
    list=["T","F","T","F","T","F","T"]
    i=0
    n=[]
    count=0
    while i<len(list): 
        if list[i]in "T":
            n.append(list[i])
            count=count+1      
        i=i+1
    print(count,"sheeps present in the array")         
count()     
