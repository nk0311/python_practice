# talking about zip

print({num: num * num for num in range(11)})
squares = {num: num * num for num in range(11)}


print(squares.keys())
print(squares.values())
print(squares.items())


players = ["Nina", "Bob", "Alice"]
scores = [100, 5, 97]

print(zip(players, scores))
for item in zip(players, scores):
    print(item)


for name, score in zip(players, scores):
    print(f"Name: {name} had a score of {score}:")


my_list1 = [1, 2, 3]
my_list2 = ["a", "b"]
print(list(zip(my_list1, my_list2)))