# START
class Cat:
    def __init__(self, name):
        self.name = name

    def greet(self, other):
        print("Meow {}, I'm {}".format(other, self.name))
# END


# START
grumy = Cat('Grumpy')
grumy.greet('Grafield')
# END
