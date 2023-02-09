def add_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    else:
        return x - y

print(add_numbers(3, 2))
print(add_numbers(3, 2, operation="other"))