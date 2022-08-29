a=int(input("enter the number of size:"))
i=0
s=[]
while i<(a):
    val=int(input("enter the number:"))
    s.append(val)
    i=i+1
print(s) 
i=0
while i<len(s):
    if s[i]>=1 and s[i]<=7:
     i=i+1
print("true")                         

