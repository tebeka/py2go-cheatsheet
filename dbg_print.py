from collections import namedtuple

Actor = namedtuple('Actor', 'name age')

# START
daffy = Actor(
    name='Daffy',
    age=80,
)
print('{!r}'.format(daffy))
# END
