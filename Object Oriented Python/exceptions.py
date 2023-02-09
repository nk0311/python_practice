
try:
    d = {}
    d["a"]
    int("a")
except ValueError:
    print("A value exception happened")
except KeyError:
    print("A key was not found")

print("End of the program")