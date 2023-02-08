names = ["Bob", "Max", "Jen"]
print(len(names))
print([names[0]])

names[0] = "Mark"
print(names)

lottery_numbers = [1,4,1993,7]
print(sorted(lottery_numbers))

# will reverse the sort
print(sorted(lottery_numbers, reverse=True))

# to sort the list in place call .sort() method
lottery_numbers.sort()
print(lottery_numbers)

lottery_numbers.append(2345)
print(lottery_numbers)

lottery_numbers.insert(1, 55)
print(lottery_numbers)

# True or False 
print(1 in lottery_numbers)
