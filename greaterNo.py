a = int(input("Enter the num1 : "))
b = int(input("Enter the num2 : "))
c = int(input("Enter the num3 : "))

if(a>b and a>c):
    print(a," is greater")
elif(b>a and b>c):
    print(b," is greater")
else:
    print(c," is greater")