init 5 python:
    def demand_panties_requirement(the_person):
        if the_person.vagina_visible() and not the_person.wearing_panties():
            return False
        if not (the_person.obedience >= 120 or the_person.effective_sluttiness() >= 30 or the_person.love >= 30):
            return "Requires: 120 Obedience\nor 30 Sluttiness or 30 Love"
        return True

label demand_panties_label(the_person):
    "You lean over and whisper softly in her ear..."
    mc.name "I want you to give me your panties..."

    if not the_person.wearing_panties():
        the_person "I would love to do that [the_person.mc_title], except that I'm not wearing any..."
        mc.name "Ah, I see, you were expecting something to happen today..."
        return

    $ test_outfit = the_person.outfit.get_copy()
    $ the_item = test_outfit.get_panties()
    if the_item.is_extension: #two piece item
        $ the_item = next((x for x in test_outfit.get_upper_ordered() if x.has_extension == the_item), None)
    $ removed_something = False

    if test_outfit.can_remove_panties():
        $ test_outfit.remove_clothing(the_item)
    else:
        $ test_outfit.strip_to_vagina()
        if test_outfit.has_clothing(the_item): # in case of crotchless/half-off panties
            $ test_outfit.remove_clothing(the_item)

    if the_person.location.privacy_level == 3 or the_person.location.get_person_count() > 1:
        the_person "Right here? In public?"
        if the_person.judge_outfit(test_outfit, temp_sluttiness_boost = -10):
            $ the_person.draw_person(emotion = "happy")
            "[the_person.possessive_title] smiles, clearly excited by the idea."
        else:
            the_person "I could do that [the_person.mc_title], but other people might notice if I start stripping down."
            mc.name "Why don't you stop wearing panties, so I don't have to ask for them?"
            the_person "Maybe next time..."
            # TODO: that's an order
            return
    else:
        $ apply_sex_modifiers(the_person) # quickly add and remove modifiers to get that sweet, sweet love bonus
        $ judge = the_person.judge_outfit(test_outfit)
        $ clear_sex_modifiers(the_person)
        if not judge:
            the_person "I'm sorry [the_person.mc_title], but my panties stay on for now."
            mc.name "For now?"
            "[the_person.title] smirks and changes the subject."
            return

    if the_person.can_remove_panties():
        $ the_person.draw_animated_removal(the_item)
        "[the_person.possessive_title] takes a quick look around and pulls off her [the_item.display_name], placing them in your hand."
        $ the_person.change_stats(obedience = 1, slut = 1, max_slut = 30)
        the_person "Is this what you were looking for?"
    else:
        $ old_outfit = the_person.outfit.get_copy()
        $ old_outfit.remove_clothing(the_item)

        the_person "This might take a minute..."
        if the_person.location.privacy_level == 4 or the_person.location.get_person_count() > 1:
            "[the_person.possessive_title] takes a quick look around and starts stripping down."
        else:
            "[the_person.possessive_title] starts stripping down, giving you her [the_item.display_name]."
        $ the_person.strip_to_vagina()
        if the_person.outfit.has_clothing(the_item):
            $ the_person.draw_animated_removal(the_item)
        the_person "Here you are, anything else I can do for you?"
        $ the_person.apply_outfit(old_outfit)
        $ the_person.draw_person()
        $ the_person.change_stats(obedience = 1, slut = 1, max_slut = 30)
        "She quickly puts her clothes back on."
        
    return
