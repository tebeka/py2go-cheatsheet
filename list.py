# START
names = ['bugs', 'taz', 'tweety']
print(names[0])  # bugs
names.append('elmer')
print(len(names))  # 4
print(names[2:])  # ['tweety', 'elmer']
for name in names:
    print(name)

for i, name in enumerate(names):
    print('{} at {}'.format(name, i))
# END
