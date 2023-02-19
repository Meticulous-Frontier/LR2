# generate random underwear for the lily new underwear event,
# instead of getting one from the default_wardrobe.xml

init 5 python:
    def lily_new_underwear_get_underwear(person):
        return person.generate_random_appropriate_outfit(outfit_type = "UnderwearSets", swap_bottoms = True, allow_skimpy = True)
