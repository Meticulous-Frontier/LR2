
init 2 python:
    def sakari_mod_initialization():
        #sakari_wardrobe = wardrobe_from_xml("ashley_Wardrobe")
        sakari_base_outfit = Outfit("sakari's base accessories")
        the_glasses = modern_glasses.get_copy()
        the_glasses.colour = [.15, .15, .15, 1.0]
        the_lipstick = lipstick.get_copy()
        the_lipstick.colour = [.15, .15, .15, 0.5]
        the_rings = garnet_ring.get_copy()   #Change this
        the_rings.colour = [.82,.15,.15,1.0]
        sakari_base_outfit.add_accessory(the_lipstick)
        sakari_base_outfit.add_accessory(the_rings)
        sakari_base_outfit.add_accessory(the_glasses)

        # init sakari role
        sakari_role = Role(role_name ="sakari", actions =[], hidden = True)

        #global sakari_role
        global sakari
        sakari = make_person(name = "Sakari", last_name ="Greene", age = 42, body_type = "thin_body", face_style = "Face_14",  tits="C", height = 0.92, hair_colour=["bald", [0.414, 0.305, 0.258,0]], hair_style = long_hair, skin="tan" , \
            eyes = "brown", personality = sakari_personality, name_color = "#228b22", dial_color = "228b22" , \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 7, start_obedience = 18, start_happiness = 88, start_love = 0, \
            relationship = "Single", kids = 1, force_random = True, base_outfit = sakari_base_outfit,
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -2, False], ["classical", 1, False]],
            forced_sexy_opinions = [["taking control", 2, False], ["getting head", 2, False], ["drinking cum", -2, False], ["giving blowjobs", -2, False], ["public sex", 2, False]])

        sakari.generate_home()
        sakari.set_schedule(sakari.home, times = [0,1,2,3,4])   #Hide Sakari at home until we are ready to use her
        sakari.home.add_person(sakari)

        sakari.event_triggers_dict["intro_complete"] = False    # True after first talk

        # add appoint
        #office.add_action(HR_director_appointment_action)

        # sakari_intro = Action("sakari_intro",sakari_intro_requirement,"sakari_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        # mc.business.add_mandatory_crisis(sakari_intro) #Add the event here so that it pops when the requirements are met.

        # set relationships
        town_relationships.update_relationship(sakari, kaya, "Daughter", "Mother")
        # town_relationships.update_relationship(nora, sakari, "Friend")
        # town_relationships.update_relationship(lily, sakari, "Rival")

        sakari.add_role(sakari_role)
        return
