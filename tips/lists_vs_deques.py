from collections import deque

# don't do this
fruit = ['orange', 'apple', 'banana', 'strawberry']

del fruit[0]
fruit.pop(0)
fruit.insert(0, 'watermelon')


# do this instead
fruit = deque(['orange', 'apple', 'banana', 'strawberry'])

del fruit[0]
fruit.popleft()
fruit.appendleft('watermelon')