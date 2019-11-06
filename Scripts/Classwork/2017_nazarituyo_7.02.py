class Pet(object):
    def __init__(self, a, c, f, n, no):
        self.animal = a
        self.color = c
        self.food = f
        self.name = n
        self.noise = no


pet1 = Pet('Dog', 'grey', 'kibble', 'Bendel', 'Bark')
pet2 = Pet('Mat', 'pink', 'raw meat', 'Pinky', 'Meow')
pet3 = Pet('Mouse', 'white', 'cheese', 'Stuart Little', 'Squeaks')
pet4 = Pet('Chick', 'yellow', 'grain', 'Henny Penny', 'Clucks')
all_pets = (pet1, pet2, pet3, pet4)


def print_name_and_food(pets):
    for pet in pets:
        print('Name:', pet.name, ', Food:', pet.food)


print_name_and_food(all_pets)
