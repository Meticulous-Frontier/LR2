# overrides the default make person function in the game
# so we can add / change person characteristics based on custom personalities.

init 1 python:
    # This will be called in game when a person is created orginal function in script.rpy
    def make_person():
        split_proportion = 20 #1/5 characters generated will be a premade character.
        return_character = None
        if renpy.random.randint(1,100) < split_proportion:
            return_character = get_premade_character()

        if return_character is None: #Either we aren't getting a premade, or we are out of them.
            return_character = create_random_person()

        update_random_person(return_character)

        return return_character

    # change the random person based other characteristics of personality
    def update_random_person(person):
        if (person.personality == cougar_personality):  # this can be applied to any random person, but the age could be to low, fix that here
            person.age = renpy.random.randint(40, 55)
        elif person.age > 40: # not cougar but old, that sounds wrong, fix it
            person.age = renpy.random.randint(18, 40)
        return