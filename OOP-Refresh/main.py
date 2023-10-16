class Hero:
    def __init__(self, name, superpower, country, can_fly=False):
        self.name = name
        self.superpower = superpower
        self.country = country
        self.can_fly = can_fly
        

    def is_flying(self): 
        if self.can_fly:
            print(f'{self.name} is still flying')
            return
        
        print(f'{self.name} is flying high in the sky!')
        self.can_fly = True

h1 = Hero("Blanka", "Electricity", "Brazil")

h2 = Hero("Guile", "Sonic Boom", "USA")

h1.is_flying()
h1.is_flying()