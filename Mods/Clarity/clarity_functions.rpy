init 1 python:
    def get_clarity_mult():
        clarity_mult = 1.0
        if perk_system.has_ability_perk("Intelligent Clarity"):
            clarity_mult += (mc.int * .05) #5% increase per intelligence point
        if perk_system.has_ability_perk("Charismatic Clarity"):
            clarity_mult += (mc.charisma * .05) #5% increase per charisma point
        if perk_system.has_ability_perk("Focused Clarity"):
            clarity_mult += (mc.focus * .05) #5% increase per charisma point

        return clarity_mult

    def add_intelligent_clarity_perk():
        if perk_system.has_ability_perk("Intelligent Clarity"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "You gain increase clarity based on your intelligence.", toggle = False, usable = False), "Intelligent Clarity")
        return

    def add_charismatic_clarity_perk():
        if perk_system.has_ability_perk("Charistmatic Clarity"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "You gain increase clarity based on your charisma.", toggle = False, usable = False), "Charismatic Clarity")
        return

    def add_intelligent_clarity_perk():
        if perk_system.has_ability_perk("Focused Clarity"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "You gain increase clarity based on your focus.", toggle = False, usable = False), "Focused Clarity")
        return
