# START
def div(a, b):
    if b == 0:
        raise ValueError("b can't be 0")
    return a / b
# END


div(1, 2)

# START
try:
    div(1, 0)
except ValueError:
    print('OK')
# END
