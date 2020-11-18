init python:
    def anti_bimbo_serum_function_on_apply(the_person, add_to_log):
        if the_person.personality == bimbo_personality: #WE only run if we have the bimbo personality
            the_person.int = renpy.random.randint(2,6)  #Restores intelligence to a roughly normal value
            if the_person.original_personality != None:
                the_person.personality = the_person.original_personality
            else:
                the_person.personality = get_random_personality()
        return



    anti_bimbo_serum_trait = SerumTrait(name = "Bimbo Reversal",
            desc = "This serum doesn't completely counter the bimbo serum, but it returns personality and intelligence to roughly pre-bimbo status.",
            positive_slug = "+$20 Value, Restores Intelligence, Restores Personality",
            negative_slug = "400 Serum Research",
            value_added = 20,
            research_added = 400,
            base_side_effect_chance = 50,
            on_apply = anti_bimbo_serum_function_on_apply,
            #requires = permanent_bimbo,   #TODO For some reason this doesn't work. Why doesn't this work?
            tier = 3,
            research_needed = 3000,
            exclude_tags = ["Personality"],
        )
