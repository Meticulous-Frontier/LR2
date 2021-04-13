
init 2 python:
    def ellie_mod_initialization():
        ellie_wardrobe = wardrobe_from_xml("ashley_Wardrobe")
        ellie_base_outfit = Outfit("ellie's base accessories")
        the_eye_shadow = heavy_eye_shadow.get_copy()
        the_eye_shadow.colour = [.71, .4, .85, 0.5]
        the_glasses = big_glasses.get_copy()
        the_glasses.colour = [.15, .15, .15, 1.0]
        the_lipstick = lipstick.get_copy()
        the_lipstick.colour = [.37, .02, .05, 0.75]
        the_necklace =gold_chain_necklace.get_copy()
        the_necklace.colour = [.95, .95, .78, 1.0]
        the_bracelet = copper_bracelet.get_copy()
        the_bracelet.colour = [.95, .95, .78, 1.0]
        ellie_base_outfit.add_accessory(the_eye_shadow)
        ellie_base_outfit.add_accessory(the_glasses)
        ellie_base_outfit.add_accessory(the_lipstick)
        ellie_base_outfit.add_accessory(the_necklace)
        ellie_base_outfit.add_accessory(the_bracelet)

        # init ellie role
        ellie_role = Role(role_name ="ellie", actions =[], hidden = True)

        #global ellie_role
        global ellie
        ellie = make_person(name = "Ellie", age = 24, body_type = "thin_body", face_style = "Face_13",  tits="DDD", height = 0.92, hair_colour="dark auburn", hair_style = bobbed_hair, skin="white" , \
            eyes = "light blue", personality = introvert_personality, name_color = "#228b22", dial_color = "228b22" , starting_wardrobe = ellie_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 0, start_obedience = 5, start_happiness = 103, start_love = -3, \
            title = "Ellie", possessive_title = "Your intern", mc_title = mc.name, relationship = "Single", kids = 0, force_random = True, base_outfit = ellie_base_outfit,
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -2, False], ["classical", 1, False]],
            forced_sexy_opinions = [["taking control", 2, False], ["getting head", 2, False], ["drinking cum", -2, False], ["giving blowjobs", -2, False], ["public sex", 2, False]])

        ellie.generate_home()
        ellie.set_schedule(ellie.home, times = [0,1,2,3,4])
        # ellie.set_schedule(downtown_bar, times = [2,3])
        ellie.home.add_person(ellie)
        ellie.idle_pose = "stand2"

        ellie.event_triggers_dict["intro_complete"] = False    # True after first talk

        # add appoint
        #office.add_action(HR_director_appointment_action)

        # ellie_intro = Action("ellie_intro",ellie_intro_requirement,"ellie_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        # mc.business.add_mandatory_crisis(ellie_intro) #Add the event here so that it pops when the requirements are met.

        # set relationships
        # town_relationships.update_relationship(ellie, stephanie, "Sister")
        # town_relationships.update_relationship(nora, ellie, "Friend")
        # town_relationships.update_relationship(lily, ellie, "Rival")

        ellie.add_role(ellie_role)
        return
