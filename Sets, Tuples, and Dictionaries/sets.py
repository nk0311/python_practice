my_set = {"a", 1, 2, 4, "Nina"}
print(my_set)

my_set.add("Orange")
print(my_set)

my_set.discard("Nina")
print(my_set)

# combining two sets

colors = {"Red", "Orange"}
numbers = {1, 2, 3}
print(colors)
print(numbers)
colors.update(numbers)
print(colors)



