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

    if test_outfit.can_remove_panties():
        $ test_outfit.remove_clothing(the_item)
    else:
        $ test_outfit.strip_to_vagina()
        if test_outfit.has_clothing(the_item): # in case of crotchless/half-off panties
            $ test_outfit.remove_clothing(the_item)

    if the_person.location.privacy_level == 3 or the_person.location.get_person_count() > 1:
        the_person "Right here? In public?"
        if demand_strip_judge_public(the_person, test_outfit, "not wearing underewar"):
            $ the_person.draw_person(emotion = "happy")
            "[the_person.title] smiles, clearly excited by the idea."
            jump .start_stripping
        else:
            the_person "I could do that [the_person.mc_title], but other people might notice if I start stripping down."
            call .thats_an_order from _demand_panties_public
            if _return:
                jump .start_stripping
            else:
                mc.name "Why don't you stop wearing panties, so I don't have to ask for them?"
                the_person "Maybe next time..."

    else:
        if demand_strip_judge_private(the_person, test_outfit, "not wearing underwear"):
            jump .start_stripping
        else:
            the_person "I'm sorry [the_person.mc_title], but my panties stay on for now."
            call .thats_an_order(private = True) from _demand_panties_private
            if _return:
                jump .start_stripping
            else:
                mc.name "For now?"
                "[the_person.title] smirks and changes the subject."
    return


label .thats_an_order(private = False):
    $ was_ordered = False
    $ obedience_requirement = demand_strip_get_obedience_req(the_person, test_outfit, min = 120, private = private)
    menu:
        "That's an order" if the_person.obedience >= obedience_requirement:
            mc.name "I must not have been clear enough."
            mc.name "Give me your panties. Now."
            $ the_person.draw_person(emotion = "angry")
            the_person "..."
            $ the_person.draw_person(emotion = "sad")
            $ the_person.change_stats(happiness = -2)
            "[the_person.title] is cowed into compliance by the tone of your voice."
            $ was_ordered = True
            pass
        "That's an order\n{color=#ff0000}{size=18}Requires: [obedience_requirement] Obedience{/size}{/color} (disabled)" if the_person.obedience < obedience_requirement:
            pass
        "Let it go":
            $ the_person.change_stats(obedience = -1)
            pass
    return was_ordered


label .start_stripping:
    $ modify_outfit = False
    if the_person.outfit == the_person.planned_outfit:
        $ modify_outfit = True

    if the_person.can_remove_panties():
        "[the_person.possessive_title] takes a quick look around and pulls off her [the_item.display_name], placing them in your hand."
        $ the_person.draw_animated_removal(the_item)
        $ the_person.change_stats(obedience = 1, slut = 1, max_slut = 30)
        $ the_person.update_outfit_taboos()
        the_person "Is this what you were looking for?"
    else:
        $ old_outfit = the_person.outfit.get_copy()
        $ old_outfit.remove_clothing(the_item)

        the_person "This might take a minute..."
        if the_person.location.privacy_level == 3 or the_person.location.get_person_count() > 1:
            "[the_person.possessive_title] takes a quick look around and starts stripping down."
        else:
            "[the_person.possessive_title] starts stripping down, giving you her [the_item.display_name]."
        $ the_person.strip_to_vagina()
        if the_person.outfit.has_clothing(the_item):
            $ the_person.draw_animated_removal(the_item)
        $ the_person.change_stats(obedience = 1, slut = 1, max_slut = 30)
        $ the_person.update_outfit_taboos()
        the_person "Here you are, anything else I can do for you?"
        $ the_person.apply_outfit(old_outfit)
        $ the_person.draw_person()
        "She quickly puts her clothes back on."
    
    if modify_outfit:
        $ the_person.planned_outfit = the_person.outfit.get_copy()
        
    return
