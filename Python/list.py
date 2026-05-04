list=["Korim",3,45,"Imran", 4]
# list[0]="Rahim"
# lenth=len(list)
list.append("Zahanara")
list.insert(2,"Naimur")
print("After insert:", list)
a=["Apple",True,5.5]
list.extend(a)
print("After extend: ",list)

# Removing element
list.remove("Naimur")
print("After Remove:", list)

# using pop()
list.pop()
print("Remove pop default:", list)
list.pop(2)
print("Remove spacific element:",list)

# Clear method
list.clear()
print("After clear: ", list)

# del method
language=["Python", "PHP", "JavaScript"]
del language(1)