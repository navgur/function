def palen():
#     list=[121,567,434]
#     i=0
#     count=0
#     while i<len(list):
#         rev=0
#         a=list[i]
#         while list[i]>0:
#             rev=(rev*10)+list[i]%10
#             list[i]//=10
#         if a==rev:
#             count=count+1
#             print("pailendromendrome=",a)
#         i=i+1
#     print(count)
# palen()    
    l=["nitin","rani",231,"aba","mom4"]
    i=0
    while i<len(l):
        if type(l[i])!=str:
           a = str(l[i])
    else:
        a=l[i]
    rev=''
    j=1
    while j <= len(a):
        rev+=a[-j]
        j+=1
    if a==rev:
        print("pailendrome",rev)
    else:
        print("not pailendrome",rev)
    i=i+1  
      
#       l=["nitin","rani",231,"aba","mom4"]
# i=0
# while i<len(l):
#     if type(l[i])!=str:
#         a = str(l[i])
#     else:
#         a=l[i]
#     rev=''
#     j=1
#     while j <= len(a):
#         rev+=a[-j]
#         j+=1
#     if a==rev:
#         print("pailendrome",rev)
#     else:
#         print("not pailendrome",rev)
#     i=i+1  
      