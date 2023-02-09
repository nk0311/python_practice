def add_numbers(x, y):
    return x + y

result = add_numbers(3,4)
print(result)

def add_numbers2(x, y, z=1):
    return x + y + z

result2 =add_numbers2(3, 5, 2)
print(result2)

def create_query(language="JavaScript", num_stars=10, sort="desc"):
    return f"language: {language}, num_stars is {num_stars}, sort is {sort}"

print(create_query())
