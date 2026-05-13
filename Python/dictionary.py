person={
    "name":"Shihab",
    "age":50,
    "city":"Dhaka"
}
# print(person["age"])
person["Email"]="shihab@gmail.com"
print("After add value",person)
person["age"]=22
print("After Modifying:", person)
print(len(person))

del person["age"]
print("After deleting :", person)
print(len(person))

# ----Pop()
