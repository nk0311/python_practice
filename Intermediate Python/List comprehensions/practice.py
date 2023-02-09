import random

# Comprehensions, Slicing, Zip Excercise

my_list = [num for num in range(100) if num % 2 == 0]
print(my_list)


print(random.randint(0,100))

my_dict  = {num: random.randint(0, 100) for num in my_list}
print(my_dict)
print(my_dict.values())

names = ["Nina", "Max", "Floyd", "Lloyd"]
scores = {random.randint(0, 100) for name in names}
print(scores)

for name, score in zip(names, scores):
    print(f"{name} for {score} points")