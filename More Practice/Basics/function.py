def say_hello():
    print("hello")

say_hello()

def add_num(num1, num2):
    return num1+num2

result = add_num(10,20)
print(result)

def even_check(number):
    result = number % 2 == 0
    return result

print(even_check(5))

def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass

print(check_even_list([2,3]))




