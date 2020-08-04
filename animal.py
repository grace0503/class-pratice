class Animal:
    def __init__(self,species,feet,gender):
        self.species = species
        self.feet = feet
        self.gender = gender
        
    def show_species(self):
        print('Hi , I am a {0} .'.format(self.species))

    def show_feet(self):
        print('I have {0} feet.'.format(self.feet))
        
    def show_gender(self):
        print('I am {0} .'.format(self.gender))

animal_1=Animal('chicken',2,'femal')
animal_1.show_species()
animal_2=Animal('pig',4,'male')
animal_2.show_gender()
animal_3=Animal('fish',0,'femal')
animal_3.show_feet()