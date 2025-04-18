import random
from functools import reduce


def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + " " + random.choice(list_2)


def capitalize_suffix(name):
    return name.capitalize()


def fire_in_name(name):
    return "Fire" in name


def concatenate_names(name1, name2):
    return name1 + name2


def display_name_info(names_list, fire_list, concatenated):
    for name in names_list:
        print(name)

    print(fire_list)
    print(concatenated)


prefixes = ["Mystic", "Golden", "Dark", "Shadow", "Silver"]
suffixes = ["storm", "song", "fire", "blade", "whisper"]

capitalised_suffixes = list(map(capitalize_suffix, suffixes))
random_names = [create_fantasy_name(prefixes, capitalised_suffixes) for _ in range(9)]
has_fire = list(filter(fire_in_name, random_names))
concatenated_names = reduce(concatenate_names, has_fire)
display_name_info(random_names, has_fire, concatenated_names)
