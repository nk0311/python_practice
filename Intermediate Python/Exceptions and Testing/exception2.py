def division(num):
    try:
            result = 3.14 / num
    except ArithmeticError:
            print("We had a general math error")
    except ZeroDivisionError:
            print("Divide by zero error")


# math error
division(0)

