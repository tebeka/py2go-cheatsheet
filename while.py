# START
a, b = 1, 1
while b < 10_000:
    a, b = b, a + b
# END
print(a)
