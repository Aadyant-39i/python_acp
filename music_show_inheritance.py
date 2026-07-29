from abc import ABC, abstractmethod



class Instrument(ABC):

    # Parent constructor
    def __init__(self, name, type):
        self.name = name
        self.type = type

    # Concrete method
    def display(self):
        print(f"Instrument: {self.name} | Type: {self.type}")

    # Abstract method
    @abstractmethod
    def play(self):
        pass



class Guitar(Instrument):

    def __init__(self, name, type, strings):
        super().__init__(name, type)
        self.strings = strings

    def play(self):
        print(f"{self.name} ({self.strings} strings) plays: Strum! Strum!")



class Piano(Instrument):

    def __init__(self, name, type, keys):
        super().__init__(name, type)
        self.keys = keys

    def play(self):
        print(f"{self.name} ({self.keys} keys) plays: Plink! Plink!")



class Drum(Instrument):

    def __init__(self, name, type, size):
        super().__init__(name, type)
        self.size = size

    def play(self):
        print(f"{self.name} ({self.size}) plays: Boom! Boom!")


guitar = Guitar("Acoustic Guitar", "String", 6)
piano = Piano("Grand Piano", "Keyboard", 88)
drum = Drum("Bass Drum", "Percussion", "Large")

print("=== Music Instrument Sound Show ===\n")

for instrument in [guitar, piano, drum]:
    instrument.display()
    instrument.play()
    print()
