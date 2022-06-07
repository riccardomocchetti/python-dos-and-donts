names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

# Don't do this
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '--->', colors[i])

# Do this instead
for name, color in zip(names, colors):
    print(name, '--->', color)