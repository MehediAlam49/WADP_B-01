# for loop in range
# for i in range(10):
#     print(i)

# for i in range(21, 31):
#     print(i)

# loop in string

# lang=["Python",55,"c", 45.67, "go",True, False]

# for i in lang:
#     print(i)


# For loop in dictionary
my_dict={
    "name":"Zahanara",
    "age":22,
    "city": "dhaka"
}
# for value in my_dict.values():
#     print(value)

# for key,value in my_dict.items():
#     print(key, ":", value)

# languages=["Python", "PHP", "Javascript", "go", "swift"]

# for i in languages:
#     if i=="Javascript":
#         break
#     print(i)

# continue statement
languages=["Python", "PHP", "Javascript", "go", "swift"]

for i in languages:
    if i=="Javascript":
        continue
    print(i)