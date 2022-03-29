def add(a,b):
    return (a+b)
def substract(a,b):
    return (a-b)
def multiply(a,b):
    return (a*b)
def divide(a,b):
    return (a/b)
def modulus(a,b):
    return (a%b)
def exponent(a,b):
    return(a**b)

print( "Calcuator using If condition and Functions")
print("1 => Addition")
print("2 => Substraction")
print("3 => Multiplication")
print("4 => Division")
print("5 => Modulus")
print("6 => Exponentiation")

user_choice = int(input("Enter Operator Choice(1-6): "))

if user_choice==1:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    print("Sum = ", add(a,b))
elif user_choice==2:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    print("Substraction = ",substract(a,b))
elif user_choice==3:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    print("Product = ",multiply(a,b))
elif user_choice==4:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    print("Quotient = ",divide(a,b))
elif user_choice==5:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))

    print("Remainder = ",modulus(a,b))
elif user_choice==6:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    print("Exponent = ",exponent(a,b))
else:
    print("Invalid Choice!")
    
