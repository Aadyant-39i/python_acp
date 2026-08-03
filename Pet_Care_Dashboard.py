class Dog:

    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def info(self):
        print(f"Dog - Name: {self.__name}, Health: {self.__health}")

    def care(self):
        print(f"{self.__name} is wagging its tail!")

    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        if new_health >= 0:
            self.__health = new_health
            print(f"Health updated to {self.__health}")
        else:
            print("Health cannot be negative.")


class Cat:

    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def info(self):
        print(f"Cat - Name: {self.__name}, Health: {self.__health}")

    def care(self):
        print(f"{self.__name} is purring!")

    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        if new_health >= 0:
            self.__health = new_health
            print(f"Health updated to {self.__health}")
        else:
            print("Health cannot be negative.")


# Create objects
dog = Dog("Bug the Pug", 90)
cat = Cat("Mr Pineapple", 85)

# Polymorphism – same method, different behaviour
print("=== My Pet Care Dashboard ===\n")

for pet in (dog, cat):
    pet.info()
    pet.care()
    print()

# Encapsulation – direct change does NOT work
print("--- Direct change attempt ---")
dog.__health = 999
print(f"get_health() still shows: {dog.get_health()}")

# Setter – the only safe way to update
print("\n--- Updating Health ---")
dog.set_health(100)
cat.set_health(95)