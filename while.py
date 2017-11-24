# START
# Largest Fibonacci under 10,000
a, b = 1, 1
while b < 10000:
    a, b = b, a + b
# END
print(a)
