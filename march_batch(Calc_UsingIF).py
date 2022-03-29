#operator menu
print( "Calcuator using If condition only")
print("1 => Addition")
print("2 => Substraction")
print("3 => Multiplication")
print("4 => Division")
print("5 => Modulus")
print("6 => Exponentiation")


#user input
user_choice = int(input("Enter Operator Choice(1-6): "))

if user_choice==1:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a+b
    print("Sum = ", c)
elif user_choice==2:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a-b
    print("Substraction = ",c)
elif user_choice==3:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a*b
    print("Product = ",c)
elif user_choice==4:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a/b
    print("Quotient = ",c)
elif user_choice==5:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a%b
    print("Remainder = ",c)
elif user_choice==6:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a**b
    print("Exponent = ",c)
else:
    print("Invalid Choice!")
    
