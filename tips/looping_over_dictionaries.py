import time

d = {"one": 1, "two": 2, "three": 3, "four": 4}


# Don't do this
start = time.perf_counter_ns()
for k in d:
    print(k, "-->", d[k])
print("Executed in", time.perf_counter_ns() - start, "nanoseconds")


# Do this instead
start = time.perf_counter_ns()
for k, v in d.items():
    print(k, "-->", v)
print("Executed in", time.perf_counter_ns() - start, "nanoseconds")