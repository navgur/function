list=[1450 ,960000,1050]
i=0
a=[]
while i<len(list):
    k=str(list[i])    
    j=0
    s=""
    while j<len(k):
        if k[j] != "0":
            s=s+(k[j])
        j=j+1
    a.append(s)
    i=i+1 
print(a)               

# i=0
# l=[]
# while(i<len(list)):
#     a=list[i]
#     while(a>0):
#         if a%10==0:
#             a=a%10
#         elif a%10!=0:
#             l.append(a)
#             a=0
#     i+=1
# print(l)

