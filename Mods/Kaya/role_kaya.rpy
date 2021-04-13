init 2 python:
    def kaya_mod_initialization():
        kaya_wardrobe = wardrobe_from_xml("ashley_Wardrobe")
        kaya_base_outfit = Outfit("kaya's base accessories")
        the_eye_shadow = heavy_eye_shadow.get_copy()
        the_eye_shadow.colour = [.26, .14, .21, 0.33]
        the_lipstick = lipstick.get_copy()
        the_lipstick.colour = [1.0, .21, .14, 0.33]
        the_bracelets = colourful_bracelets.get_copy()   #Change this
        the_bracelets.colour = [.71,.4,.85,1.0]
        kaya_base_outfit.add_accessory(the_eye_shadow)
        kaya_base_outfit.add_accessory(the_lipstick)
        kaya_base_outfit.add_accessory(the_bracelets)

        # init kaya role
        kaya_role = Role(role_name ="kaya", actions =[], hidden = True)

        #global kaya_role
        global kaya
        kaya = make_person(name = "Kaya", last_name ="Greene", age = 22, body_type = "thin_body", face_style = "Face_3",  tits="B", height = 0.92, hair_colour="black", hair_style = messy_hair, skin="tan" , \
            eyes = "brown", personality = kaya_personality, name_color = "#228b22", dial_color = "228b22" , starting_wardrobe = kaya_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 7, start_obedience = -18, start_happiness = 88, start_love = 0, \
            relationship = "Single", kids = 0, force_random = True, base_outfit = kaya_base_outfit,
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -2, False], ["classical", 1, False]],
            forced_sexy_opinions = [["taking control", 2, False], ["getting head", 2, False], ["drinking cum", -2, False], ["giving blowjobs", -2, False], ["public sex", 2, False]])

        kaya.generate_home()
        kaya.set_schedule(kaya.home, times = [0,1,2,3,4])
        #kaya.set_schedule(downtown_bar, times = [2,3])
        kaya.home.add_person(kaya)

        kaya.event_triggers_dict["intro_complete"] = False    # True after first talk

        # add appoint
        #office.add_action(HR_director_appointment_action)

        # kaya_intro = Action("kaya_intro",kaya_intro_requirement,"kaya_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        # mc.business.add_mandatory_crisis(kaya_intro) #Add the event here so that it pops when the requirements are met.

        # set relationships
        # town_relationships.update_relationship(kaya, stephanie, "Sister")
        # town_relationships.update_relationship(nora, kaya, "Friend")
        # town_relationships.update_relationship(lily, kaya, "Rival")

        kaya.add_role(kaya_role)
        return


init -2 python:
    def kaya_setup_intro_event_requirement():
        if alexia.is_employee() and day > alexia.event_triggers_dict.get("employed_since", 9999) + 7:
            return True
        return False



label kaya_setup_intro_event_label():
    $ the_person = kaya
    $ kaya.set_schedule(downtown, times = [2,3])    #TODO make this the coffee shop
    $ kaya.set_schedule(university, days = [0, 1, 2, 3, 4], times = [1])
    return
