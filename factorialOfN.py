n = int(input("Enter n : "))

factorial = 1
for i in range(1, n+1):
    factorial *= i
    
print("Factorial of first", n ,"natural no is ", factorial )