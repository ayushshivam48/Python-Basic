student = {
    "name" : "Ayush Shivam",
    "subject" : {
        "phy" : 93,
        "chem" : 90,
        "maths" : 98,
    }
}
print(student)
print(student["subject"])
print(student["subject"]["chem"])
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
print(student.values())
print(student.items())

pairs = list(student.items())
print(pairs[0])

# print(student["name2"])  #throw error
print(student.get("name2"))  #throw none 

new_dict = {"name" : "Shivam" ,"city" : "delhi"}  #old name is updated with new name in original dictonary
student.update(new_dict)
print(student)
