# START
ages = {  # Correct for 2017
    'daffy': 80,
    'bugs': 79,
    'taz': 63,
}
ages['elmer'] = 80
print(ages['bugs'])  # 79
print('bugs' in ages)  # True

del ages['taz']

for name in ages:  # Keys
    print(name)

for name, age in ages.items():  # Keys & values
    print('{} is {} years old'.format(name, age))
# END
