from datetime import date
class pet:
    def __init__(self, name, species, breed, age):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.medlist = []
    
    def meddate(self, med, duration):
        self.medlist.append([med,date.today() ,duration])

    def checkmeds(self):
        return self.medlist

p = pet('petname','speciesanme','poodle',10)
p.meddate('bravecto', 60)
p.meddate('med2', 10)
print(p.checkmeds())

