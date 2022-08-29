def square():
    u=(input("enter the number"))
    i = 0 
    d = []
    sum =""
    while i<len(u):  
        c = str(int(u[i])*int(u[i]))
        sum+=c
        i+=1
    d.append(int(sum))
    print(d)
square()    
