names = ["Nina", "Max", "Jimmy"]
print("Nina".lower())
print("Nina".upper())

upper_names= []
for name in names:
    upper_case_name = name.upper()
    upper_names.append(upper_case_name)

print(upper_names)
print("--------------------")
print([name.upper() for name in names])
