# empty set
my_set = {}
print(type(my_set))
print(type(set()))

# tuple unpacking
student = {"Marc", 8, "Math", 3.4}
name, age, subject, gpa = student
print(name)
print(age)

my_dict = {"Key": "Value"}
print(my_dict)

my_dict["Key"] = "a new value"
print(my_dict)

print("key" in my_dict)

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
