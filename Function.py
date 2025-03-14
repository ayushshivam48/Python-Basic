cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "saktiman"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end = " ")

print_len(cities)
print_len(heroes)

print_list(heroes)