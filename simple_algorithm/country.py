from wheel import Wheel

class Country(Wheel):
    def __init__(self, country, name, position):
        super().__init__(name, position)
        self.country = country

    def nation(self):
        print(f"This a {self.name} car from the {self.country} with driving position on the ")
