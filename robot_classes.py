class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        return "Hello! My name is {}.".format(self.name)

    def work(self, job):
        return "{} is now {}.".format(self.name, job)

tom = Robot("Tom", "T-100")
jerry = Robot("Jerry", "J-200")

print(tom.introduce())
print(tom.work("cleaning the house"))

print()

print(jerry.introduce())
print(jerry.work("watering the plants"))