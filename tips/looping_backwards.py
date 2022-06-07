colors = ['red', 'green', 'blue', 'yellow']

# Don't do
for i in range(len(colors)-1, -1, -1):
    print(colors[i])

# Do this instead
for color in reversed(colors):
    print(color)