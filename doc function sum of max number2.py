def string():
    list=[10,14,2,23,19]
    i=0
    max=0
    max1=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        if list[i]>max1 and list[i]!=max:  
            max1=list[i]   
        i=i+1
    A=("42 =",max+max1)
    print(A)


    "q2"
    list=[99,2,2,23,19]
    i=0
    max=0
    max1=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        if list[i]>max1 and list[i]!=max:  
            max1=list[i]   
        i=i+1
    A=("122 =",max+max1)
    print(A)

string()
           
