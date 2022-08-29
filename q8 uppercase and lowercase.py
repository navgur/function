def function(a):
    i=0
    c=0
    c1=0
    while i<len(a):
        if a[i]>"A" and a[i]<"Z":
            c=c+1
        elif a[i]>"a" and a[i]<"z":
            c1=c1+1

        i=i+1
    print("uppercase=",c)
    print("lowercase",c1)
function("The Quick Brow Fox")                
