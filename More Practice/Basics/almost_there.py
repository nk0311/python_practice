'''
Given an intiger n, return True if n is within 1- of either 100 or 200
'''

def almost_there(n):

    return (abs(100-n) <= 10) or (abs(200-n) <= 10)

print(almost_there(105))
print(almost_there(195))