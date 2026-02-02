#5.	Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
a = int(input("Enter the leading coefficient (a):"))
b = int(input("Enter the coffecient of x (b): "))
c = int(input("Enter the constant term (c): "))

d = (b*b)-(4*a*c)
root1= (-b+ d**0.5) / (2*a)
root2= (-b- d**0.5) / (2*a)

if d>0:
    
    print("Root 1 : ",root1)
    print("Root 2 : ",root2)
    print("Roots are real and distict")

elif d==0:
    root1= (-b+ d**0.5) / (2*a)
    root2= (-b- d**0.5) / (2*a)
    print("Root 1 : ",root1)
    print("Root 2 : ",root2)
    print("Roots are equal")
else:
    root1= (-b+ d**0.5) / (2*a)
    root2= (-b- d**0.5) / (2*a)
    print("Root 1 : ",root1)
    print("Root 2 : ",root2)
    print("Roots are imginary")





