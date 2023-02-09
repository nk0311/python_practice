colors = ["Red", "Green", "Blue", "Orange"]
for color in colors:
    print(f"The color is: {color}")

print(list(enumerate(colors)))

for index, color in enumerate(colors):
    print(f"{index} color at: {color}")

hex_colors = {
    "Red": "#FF0000",
    "Green": "#008000",
    "Blue": "#0000FF",
}

for foo in hex_colors:
    print(foo)


# to loop over keys and values
print(hex_colors.items())

for key, value in hex_colors.items():
    print(key)
    print("---")
    print(value)


val = 0
while val < 5:
    print(val)
    val+= 1

# range based forloop
for num in range(0,3):
    print(f"Next value: {num}")

