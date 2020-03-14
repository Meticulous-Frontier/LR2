# overrides default transition for now (it has no taboo break support)
# Original Code by BadRabbit
init 5 python:
    standing_grope.transitions.remove([standing_finger, "transition_standing_grope_standing_fingering"])
    standing_grope.transitions.append([standing_finger, "transition_standing_grope_standing_fingering_enhanced"])

label transition_standing_grope_standing_fingering_enhanced(the_girl, the_location, the_object):
    "You kiss [the_girl.title]'s neck from behind, distracting her from your hand sliding along her inner thigh and towards her crotch."
    if the_person.has_taboo("touching_vagina"):
        if the_girl.effective_sluttiness(standing_finger.associated_taboo) > standing_finger.slut_cap:
            if the_girl.outfit.vagina_available():
                "She gasps as you brush her sensitive pussy. She spreads her legs for you, giving you easy access."
            else:
                $ the_item = the_girl.outfit.get_lower_top_layer()
                if the_item:
                    "You slide your hand under her [the_item.name] and make her gasp as you brush her sensitive pussy."
                    "She spreads her legs and leans back against you, giving you easy access."
                else:
                    "She gasps as you brush her sensitive pussy. She spreads her legs for you, giving you easy access."
            $ the_girl.call_dialogue(standing_finger.associated_taboo+"_taboo_break")
            "You move your hand over her clit and feel her shiver in response to your touch."

        else:
            if the_girl.outfit.vagina_available():
                "She starts as you brush her sensitive pussy. She grabs your wrist and stops you from moving any further."
            else:
                $ the_item = the_girl.outfit.get_lower_top_layer()
                if the_item:
                    "She starts as you slide your hand under her [the_item.name]. She grabs your wrist and stops you from moving any further."
                else:
                    "She starts as you brush her sensitive pussy. She grabs your wrist and stops you from moving any further."
            $ the_girl.call_dialogue(standing_finger.associated_taboo+"_taboo_break")
            "She lets go of your hand, and you slide it down to your prize. She moans softly as you touch her, and shivers when you first touch her clit."
        "After teasing her for a moment you press two fingers between her slit, sliding them into the wet passage beyond her pussy lips."
        $ the_girl.break_taboo("touching_vagina")
    else:
        if the_girl.outfit.vagina_available():
            "You pet [the_girl.title]'s pussy, then slide two fingers inside of it. She gasps as they slip inside."
        else:
            $ the_item = the_girl.outfit.get_lower_top_layer()
            if the_item:
                "You slide a hand under her [the_item.name], bringing your hand right to her pussy."
                "She gasps as you tease it with two fingers, then slip them inside of the wet hole."
            else:
                "You pet [the_girl.title]'s pussy, then slide two fingers inside of it. She gasps as they slip inside."
        the_girl.char "Oh [the_girl.mc_title]... Ah..."

    return
