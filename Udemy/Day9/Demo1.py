colors = {
    "apple": "red",
    "banana": "yellow", 
    "pear": "green"
}

print(colors["apple"])

# add elements to dictionaries
colors["grapes"] = "purple"
print(colors)

# Wipe an existing dictionary
# colors = {}
# print(colors)

# Edit an item in a dictionary
colors["apple"] = "very red"
print(colors)

# Loop through a dictionary 
for thing in colors:
    # Just print out the key 
    print(thing)
    # Just print out the value
    print(colors[thing])