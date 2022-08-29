def prime(m):
    count=0
    i=1
    while i<=m:
        if m %i==0:
            count=count+1
        i=i+1
    if count==2:
       print("prime number")                   
    else:
       print("not prime number")    
       i=i+1
prime(13)    

# count=0
# i=1
# while i<=13:
#     if 13 %i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print("prime number")                   
# else:
#     print("not prime number")    
#     i=i+1    