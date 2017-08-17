# START
# Largest Fibonacci under 10,000
a, b = 1, 1
while b < 10000:
    a, b = b, a + b
print(a)
# END

# START
while True:
    answer = input('are you sure? [yes/no] ')
    if answer not in ('yes', 'no'):
        print('error: Unknown answer')
        continue
    break
# Do something with answer
# END
