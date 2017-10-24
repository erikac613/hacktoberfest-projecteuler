x = list(range(0, 1000, 3))
y = list(range(0, 1000, 5))
z = list(set(x + y))
print(sum(z))
