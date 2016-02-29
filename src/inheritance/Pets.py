# Python sample code for Class and Inheritance
# Pet extends object.
# from Pets import Pet

class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "{} is a {}".format(self.name, self.species)

    # Dog extends Pet
    class Dog(Pet):
        def __init__(self, name, species, chases_cats):
            Pet.__init__(self, name, species)  # base class Constructor
            self.chases_cats = chases_cats

        def chasesCats(self):
            return self.chases_cats

    class Cat(Pet):
        def __init__(self, name, species, hates_dogs):
            Pet.__init__(self, name, species)
            self.hates_dogs = hates_dogs

            def hatesDogs(self):
                self.hates_dogs

if __name__ == "__main__":
    print("Hello")