def maxx():
    h=[[0,5],[4,7],[7,8,9],[4,8,6,2,4,8,6],5,7] 
    i=0
    max=len(h[0])
    maxlist=0
    min=len(h[0])
    minlist=(h[0])
    while i<len(h):
        if type (h[i])==list:
        
         if (len(h[i]))>max:
            maxlist=h[i]
         if (len(h[i]))<min:
             minlist=h[i] 
        i=i+1
    print(maxlist) 
    print(minlist)
maxx()                           

                 

