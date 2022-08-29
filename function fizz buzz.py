def retun(a):
    if a%3==0 and a%5==0:
        return("fizz buzz")
    elif a%5==0:
        return("buzz")
    elif a%3==0:
        return("fizz buzz")
    else:
        print("wrong")    
h=retun(15)
print(h)       
