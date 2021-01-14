init -1 python:
    def cum_fetish_get_dosage_requirement(the_person):
        if mc.energy > 30:
            if time_of_day < 4:
                return True
        else:
            return "You're too tired"


init 2 python:
     cum_fetish_get_dosage = Action("Give her cum dosage",  cum_fetish_get_dosage_requirement, "cum_fetish_get_dosage_label",
        menu_tooltip = "Give her cum, right here, right now.")

init 3 python:
    cum_fetish_role = Role(role_name = "Cum Fetish", actions = [ cum_fetish_get_dosage])


label cum_fetish_get_dosage_label(the_person):
    mc.name "[the_person.title] get on your knees. Its time for your dosage of cum."
    "[the_person.possessive_title] smiles wide."
    the_person.char "Oh!? Yes! its my favorite!"
    "[the_person.possessive_title] immediately drops to her knees. She doesn't even seem to care that there could be other people around."
    $ the_person.draw_person(position = "blowjob")
    # call fuck_person(the_person, private = False, start_position = cum_fetish_blowjob, start_object = make_floor(), girl_in_charge = True, position_locked = True) from _call_fuck_person_SBR30
    call get_fucked(the_person, private= False, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = False, allow_continue = False) from _call_get_fucked_SBR030
    return
