


# def calculator(x):
# #     a=x+x
# #     return a
# u=y*y
# r=calculator(20,25,"add")
# y=calculator(10,4,"multiply")
# print(r)
# print(y)  
# # 
# def calculator():
#     ope=["1.Addition","2.Subtraction","3.Multiple","4.Division"]
#     x=int(input("Choose your operation(1/2/3/4):-"))
#     if(x>=1 and x<=4):
#         a=int(input("Enter 1st number:-"))
#         b=int(input("Enter 2nd number:-"))
#         if(x==1):
#             print(a+b)
#         elif(x==2):
#             print(a-b)
#         elif(x==3):
#             print(a*b) 
#         elif(x==4):
#             print(a/b)
#         else:
#             print("Invalid")
#     else:
#         print("Choose correct option.")
# calculator()

# def cal():
#     a=int(input("enter the number"))
#     b=int(input("enter the number"))
#     ope=(input("enter the operations"))
#     if ope=="+":
#         print(a+b)
#     elif ope=="-":
#         print(a-b)
#     elif ope=="*":
#         print(a*b)
#     elif ope=="/":
#         print(a/b)  
#     else:
#         print("error") 
# cal() 
a=int(input("enter the number"))
b=int(input("enter the number"))
i=1
while  i<=4:
    if i==1:
        print("add=",a+b)
    if i==2:
        print("multiply=",a*b)
    if i==3:
            print("subtraction",a-b)
    if i==4:
        print("divide=",a/b)         
    i=i+1        


    
def multiply(a,b):
    i=0
    m=0
    x=[]
    while i<len(a):
        m=a[i]*b[i]
        x.append(m)
        i=i+1
    print(x) 
multiply([2,4,6,5],[7,8,9,6])       

             






  