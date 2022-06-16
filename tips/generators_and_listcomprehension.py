
# list comprehension
# memory inefficient
[n for n in range(10)]

# generator expression
(n for n in range(10))
# expecially useful in combination with functions like sum, map, etc
sum(n for n in range(10))
# or with constructors
set(word for word in sentence.split())