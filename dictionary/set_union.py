farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

all_animals_1 = farm_animals.union(wild_animals)
print(all_animals_1)

all_animals_2 = wild_animals | farm_animals
print(all_animals_2)