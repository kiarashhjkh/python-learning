class animal:
    zoo_name = "Unknown"
    def __init__(self, name="Unknown", species="Unknown", age=0, sound="Unknown"):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def info(self):
        print(f"Animal name: {self.name}, species: {self.species}, age: {self.age}, sound: {self.sound} zoo: {self.zoo_name}")

    def make_sound(self):
        print(f"the {self.name} makes {self.sound} noise")

    def __str__(self):
        return f"Animal name: {self.name}, species: {self.species}, age: {self.age}, sound: {self.sound} zoo: {self.zoo_name}"


class bird_animal(animal):
    def __init__(self, name="Unknown", species="Unknown", age=0, sound="Unknown", wing_span = 0 , ):
        animal.__init__(self, name, species, age, sound)
        self.wing_span = wing_span

    def info(self):
        print(f"Animal name: {self.name}, species: {self.species}, age: {self.age}, sound: {self.sound},wing size: {self.wing_span} zoo: {self.zoo_name}")

    def make_sound(self):
        print(f"the {self.name} makes {self.sound} noise and flaps its {self.wing_span} cms wings")




lion = animal("lion", "mammal", 12, "roar")
lion.zoo_name = "eram"
lion.make_sound()
lion.info()
print(lion)
print("===============")
eagle = bird_animal("eagle", "bird", 10, "ka ka", 50)
eagle.zoo_name = "amazon"
eagle.make_sound()
eagle.info()
print(eagle)