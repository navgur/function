def mass(bmi="weight/height"):
       if bmi<=18.5:
           return("underweight")
       elif bmi<=25.0:
            return ("normal")
       elif bmi<=30.0:
           return("overweight")
       elif bmi<=30:
           return("obse" )
       else:
          return("no")
bmi=int(input("enter the number"))          
z=mass(20)
print(z)
