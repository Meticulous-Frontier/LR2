init 1 python:

    def SB_breeding_fetish_on_day(person):
        if person.knows_pregnant() or person.is_lactating():
            person.change_happiness(2, add_to_log = False)
        elif person.is_highly_fertile(): #Always aroused when fertile.
            if person.arousal < 50:
                person.arousal = 50

#Requirement functions
    def breeding_fetish_going_off_BC_requirement(the_person):
        return True

    def breeding_fetish_bend_her_over_requirement(the_person):
        if the_person.energy < 50:
            return "She's too tired"
        if mc.energy < 50:
            return "You're too tired"
        return True

#Actions
    breeding_fetish_going_off_BC = Action("She goes off BC", breeding_fetish_going_off_BC_requirement, "breeding_fetish_going_off_BC_label")
    breeding_fetish_bend_her_over = Action("Bend her over", breeding_fetish_bend_her_over_requirement, "breeding_fetish_bend_her_over_label", menu_tooltip = "Bend her over right here and give your breeding stock a creampie")

#Role (vanilla actions + fetish actions)
    breeding_fetish_role = Role(role_name = "Breeding Fetish", actions = get_breeder_role_actions() + [breeding_fetish_going_off_BC, breeding_fetish_bend_her_over], on_day = SB_breeding_fetish_on_day)

#Other breeding fetish calls

    def reset_breeding_fetish(person):
        person.remove_role(breeding_fetish_role)
        person.add_role(breeding_fetish_role)


label breeding_fetish_going_off_BC_label(the_person):
    "[the_person.title] smiles as you walk up to her."
    the_person "Oh hey [the_person.mc_title]. Glad you are here, I wanted to tell you something."
    "She leans forward and whispers into your ear."
    the_person "Just thought you'd like to know... I decided to go off my birth control..."
    $ mc.change_locked_clarity(20)
    "She leans back. You should be careful if you decide to fuck her, she might be fertile!"
    the_person "Is there something I can do for you?"
    return

label breeding_fetish_bend_her_over_label(the_person):
    "You decide that it is time for [the_person.possessive_title] to take a load. You decide to bend her over and fuck her right here, right now."
    mc.name "[the_person.title], you haven't taken a load of cum in a while. Turn around, I'm going to give you one."
    if mc.location.get_person_count() < 2:
        "With no one around, [the_person.title] happily turns around for you."
    elif mc.is_at_work():
        the_person "Oh! Right here at the office? In front of... everyone?"
        mc.name "Of course."
        the_person "Oh... well okay... I guess you're the boss!"
    elif mc_at_home():
        the_person "Oh... right here? Like in front of the family?"
        mc.name "Of course."
        the_person "Oh my god... okay... if that's what you want!"
    elif mc.location == dungeon:
        if the_person.has_role(slave_role):
            the_person "Right here? In front of the other slaves?"
            mc.name "Of course."
            the_person "Oh! Yes master!"
        else:
            the_person "Right here? In front of your slaves?"
            mc.name "Of course."
            the_person "Oh my god... okay... if that's what you want!"
    elif mc.location == sex_store:
        if the_person == starbuck:
            the_person "Right here? In front of all of my customers?"
            mc.name "Of course"
            the_person "Oh god, this is gonna be hot... okay!"
        else:
            the_person "Right here? At the sex shop?"
            mc.name "Of course"
            the_person "Oh god, this is gonna be hot... okay!"
    elif mc.location == mall_salon:
        if the_person == salon_manager:
            the_person "Right here at the salon? In front of all my customers?"
            mc.name "Of course. Don't you want to?"
            the_person "Okay... I'm trusting you!"
        else:
            the_person "At the salon? That's kind of a weird place don't you think?"
            mc.name "Not at all. Don't you want to?"
            the_person "Of course!.. Okay... I'll do it!"
    else:
        the_person "Right here? In front of everyone?"
        mc.name "Of course"
        the_person "Oh god, this is gonna be hot... okay!"
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    "[the_person.title] turns around. You quickly get her ready to fuck."
    $ the_person.strip_outfit(exclude_upper = True, position = "standing_doggy")
    the_person "Oh my god... okay... where do you want me?"
    call fuck_person(the_person, start_position = bent_over_breeding, private = False) from _call_bend_over_breeder_01
    if the_person.has_creampie_cum():
        the_person "Oh fuck... every time you finish inside me is just so good..."
        "She rubs her belly and sighs."
        $ the_person.event_triggers_dict["LastBreedingFetish"] = day
    "When you finish, [the_person.possessive_title] cleans herself up a bit."
    $ the_person.review_outfit()
    $ the_person.draw_person()
    the_person "Mmm, that was nice..."
    return
