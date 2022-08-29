def speed(a):
    if a<70:
        print("70")
    elif a>70:
        h=(a-70)//5
        if h<12:
            print(h)
        else:
            print("license suspended")  
v=int(input("enter the number"))            
speed(v)                 


