x = range(0, 100)
x = list(x)
x.append(1000)
a = []
for i in range(0, len(x) - 1):
    if (x[i] - x[i + 1])/(x[i] - x[i - 1]) < 10:
        a.extend([x[i], x.index(x[i])])
