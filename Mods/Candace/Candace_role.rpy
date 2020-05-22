#Candace, AKA Candi. Office bimbo. First met via Ophelia's story line. Can eventually corrupt, hire, and seduce her as revenge. Has default bimbo personality
# After hiring her, get discount on supplies purchased based on her sluttiness (she offers to seduce suppliers)
#Later, can develop anti bimbo serum to restore her. Transforms into Candace. Still slutty, but incredibly smart.
#Uses smarts to further seduce suppliers for a bigger discount
#TODO figure out max discounts. Probably 10-20%? Late game, supply discount is mostly flavor players are probably already profitable. Make available earlier via policy? "Logistics Coordinator?"
#Enjoys supply work, skirts, showing her ass.
init 2 python:
    def candace_mod_initialization():
        #TODO candance wardrobe and base outfit
        candace_base_outfit = Outfit("Candace's base accessories")
        the_glasses = modern_glasses.get_copy()
        the_glasses.colour = [.15, .15, .15, 1.0]
        the_eyeshadow = light_eye_shadow.get_copy()
        the_eyeshadow.colour = [.45,.31,.59,1.0]
        candace_base_outfit.add_accessory(the_glasses)
        candace_base_outfit.add_accessory(the_eyeshadow)

        candace_wardrobe = wardrobe_from_xml("Sarah_Wardrobe")
        # init candace role
        candace_role = Role(role_name ="It\'s Complicated", actions =[], hidden = False)

        global candace
        candace = make_person(name = "Candi", age = 29, body_type = "thin_body", face_style = "Face_3", tits = "FF", height = 0.94, hair_colour = ["platinum blonde", [0.789, 0.746, 0.691,1]], hair_style = windswept_hair, skin="white",\
            eyes = "dark blue", personality = bimbo_personality, name_color = "#d62cff", dial_color = "#d62cff", starting_wardrobe = sarah_wardrobe, \
            stat_array = [4,1,3], skill_array = [2,5,2,1,1], sex_array = [3,2,3,1], start_sluttiness = 35, start_obedience = -20, start_happiness = 102, start_love = 0, \
            title = "Candi", possessive_title = "Your acquaintance",mc_title = mc.name, relationship = "Girlfriend", SO_name = ophelia_get_ex_name(), kids = 0, base_outfit = candace_base_outfit,
            force_random = True, forced_opinions = [
                ["supply work", 2, True],        # she loves HR work
                ["skirts", 1, False],        #And Skirts
                ["the colour red", 2, False], #She loves red
            ], forced_sexy_opinions = [
                ["being_submissive", 1, False], # likes when others have their way with her
                ["giving handjobs", -2, False], # prefers to use other body parts...
            ])

        candace.generate_home()
        candace.set_schedule([1,2], candace.home)
        candace.set_schedule([3], office_store) #Buying office supplies for her employer.
        candace.home.add_person(candace)


        return
