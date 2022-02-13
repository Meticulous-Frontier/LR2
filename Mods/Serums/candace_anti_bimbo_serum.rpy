init 5 python:
    add_label_hijack("normal_start", "update_permanent_bimbo_serum")
    add_label_hijack("after_load", "update_permanent_bimbo_serum")

init 1 python:
    def anti_bimbo_serum_function_on_apply(the_person, the_serum, add_to_log):
        if the_person.personality == bimbo_personality: #WE only run if we have the bimbo personality
            the_person.int = renpy.random.randint(2,6)  #Restores intelligence to a roughly normal value
            if the_person.original_personality is None:
                the_person.personality = get_random_personality()
            else:
                the_person.personality = the_person.original_personality
        return

    anti_bimbo_serum_trait = SerumTrait(name = "Bimbo Reversal",
            desc = "This serum doesn't completely counter the bimbo serum, but it returns personality and intelligence to roughly pre-bimbo status.",
            positive_slug = "+$20 Value, Restores Intelligence, Restores Personality",
            negative_slug = "400 Serum Research",
            value_added = 20,
            research_added = 400,
            base_side_effect_chance = 50,
            on_apply = anti_bimbo_serum_function_on_apply,
            # requires = permanent_bimbo,       don't set, it will be handled by the loader functions.
            tier = 99,
            research_needed = 3000,
            exclude_tags = ["Personality"],
            clarity_cost = 2200,
            mental_aspect = 9,
            physical_aspect = 0,
            sexual_aspect = 0,
            medical_aspect = 2,
            flaws_aspect = 0,
            attention = 5
        )

    def enhanced_permanent_bimbo_on_apply(the_person, the_serum, add_to_log):
        if the_person.personality != bimbo_personality:
            the_person.original_personality = the_person.personality
        permanent_bimbo_on_apply(the_person, the_serum, add_to_log)
        return

    def unlock_anti_bimbo_serum(): # unlock the serum by setting the tier to 3 (instead of 99)
        found = find_in_list(lambda x: x.name == "Bimbo Reversal", list_of_traits)
        if found:
            found.tier = 3
        return

    def update_permanent_bimbo_serum_in_list():
        permanent_bimbo_in_serum_list = find_in_list(lambda x: x.name == "Permanent Bimbofication", list_of_traits)
        permanent_bimbo_in_serum_list.exclude_tags = ["Personality"]
        permanent_bimbo_in_serum_list.on_apply = enhanced_permanent_bimbo_on_apply
        return

    def add_anti_bimbo_serum_trait():
        found = find_in_list(lambda x: x.name == "Bimbo Reversal", list_of_traits)
        if not found:
            permanent_bimbo_in_serum_list = find_in_list(lambda x: x.name == "Permanent Bimbofication", list_of_traits)
            anti_bimbo_serum_trait.requires = [permanent_bimbo_in_serum_list]
            list_of_traits.append(anti_bimbo_serum_trait)
        return

label update_permanent_bimbo_serum(stack):
    python:
        update_permanent_bimbo_serum_in_list()
        add_anti_bimbo_serum_trait()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
