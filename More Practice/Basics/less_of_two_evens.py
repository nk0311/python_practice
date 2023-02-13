'''
Write a function that returns the leser of two given numbers if both numbers
are even, but returns the greater if one or two numbers are odd
'''

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        # BOTH NUMBERS ARE EVEN!
        if a < b:
            result = a
        else:
            result = b
    else:
        # ONE OR BOTH NUMBERS ARE ODD
        if a > b:
            result = a
        else:
            result = b

    return result