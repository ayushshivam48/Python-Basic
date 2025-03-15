def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

print(fact(9))

def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
fruits = ["mango", "litchi", "apple", "banana"]
print_list(fruits) 