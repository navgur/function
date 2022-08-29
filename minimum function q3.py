def min():
    h=[5,7,8,5,3,2,4,5,6,1]
    i=0
    minn=h[0]
    while i<len(h):
        if h[i]<minn:
            minn=h[i]
        i=i+1
    print(minn)
min()            