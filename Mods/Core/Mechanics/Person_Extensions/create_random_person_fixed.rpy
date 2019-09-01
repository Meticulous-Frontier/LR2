# same as VREN code except for adding a home location and adding it to the list of places
# the room object is a storage object, so every candidate stays in game memory
# causing the game to slow down and eventually crash on low mem systems
init -1 python:
    def create_random_person(name = None, last_name = None, age = None, body_type = None, face_style = None, tits = None, height = None, hair_colour = None, hair_style = None, skin = None, eyes = None, job = None,
        personality = None, custom_font = None, name_color = None, dial_color = None, starting_wardrobe = None, stat_array = None, skill_array = None, sex_array = None,
        start_sluttiness = None, start_obedience = None, start_happiness = None, start_love = None, start_home = None,
        title = None, possessive_title = None, mc_title = None, relationship = None, kids = None, SO_name = None, create_home_location = True):
        if name is None:
            name = get_random_name()
        if last_name is None:
            last_name = get_random_last_name()
        if age is None:
            age = renpy.random.randint(18,50)
        if body_type is None:
            body_type = get_random_body_type()
        if tits is None:
            tits = get_random_tit()
        if height is None:
            height = 0.9 + (renpy.random.random()/10)

        if hair_colour is None: #If we pass nothing we can pick a random hair colour
            hair_colour = generate_hair_colour() #Hair colour is a list of [string, [colour]], generated with variations by this function,
        elif isinstance(hair_colour, basestring):
            hair_colour = generate_hair_colour(hair_colour) #If we pass a string assume we want to generate a variation based on that colour.
        #else: we assume a full colour list was passed and everything is okay.

        if hair_style is None:
            hair_style = get_random_from_list(hair_styles).get_copy()
        else:
            hair_style = hair_style.get_copy() #Get a copy so we don't modify the master.

        hair_style.colour = hair_colour[1]

        # if hair_colour == "blond": #TODO: add random variation in hair colour, to add variety between people.
        #     hair_style.colour = [0.84,0.75,0.47,1]
        # elif hair_colour == "brown":
        #     hair_style.colour = [0.73,0.43,0.24,1]
        # elif hair_colour == "red":
        #     hair_style.colour = [0.3,0.05,0.05,1]
        # else: #black
        #     hair_style.colour = [0.1,0.09,0.08,1]

        if skin is None:
            skin = get_random_skin()
        if face_style is None:
            face_style = get_random_face()
        if skin == "white":
            body_images = white_skin
        elif skin == "tan":
            body_images = tan_skin
        else:
            body_images = black_skin

        emotion_images = Expression(name+"\'s Expression Set", skin, face_style)

        if eyes is None:
            eyes = get_random_eye()
        if job is None:
            job = get_random_job()
        if personality is None:
            personality = get_random_personality()

        if custom_font is None:
            #Get a font
            my_custom_font = get_random_font()

        if name_color is None:
            # Get a color
            name_color = get_random_readable_color()

        if dial_color is None:
            # Use name_color
            dial_color = copy.copy(name_color) #Take a copy

        skill_cap = 5
        stat_cap = 5

        if recruitment_skill_improvement_policy.is_owned():
            skill_cap += 2

        if recruitment_stat_improvement_policy.is_owned():
            stat_cap += 2

        if skill_array is None:
            skill_array = [renpy.random.randint(1,skill_cap),renpy.random.randint(1,skill_cap),renpy.random.randint(1,skill_cap),renpy.random.randint(1,skill_cap),renpy.random.randint(1,skill_cap)]

        if stat_array is None:
            stat_array = [renpy.random.randint(1,stat_cap),renpy.random.randint(1,stat_cap),renpy.random.randint(1,stat_cap)]

        if sex_array is None:
            sex_array = [renpy.random.randint(0,5),renpy.random.randint(0,5),renpy.random.randint(0,5),renpy.random.randint(0,5)]

        if start_love is None:
            start_love = 0

        if start_happiness is None:
            start_happiness = 100 + renpy.random.randint(-10,10)

        start_suggest = 0

        if start_obedience is None:
            start_obedience = renpy.random.randint(-10,10)

        if recruitment_obedience_improvement_policy.is_owned():
            start_obedience += 10

        if start_sluttiness is None:
            start_sluttiness = renpy.random.randint(0,10)

        if recruitment_slut_improvement_policy.is_owned():
            start_sluttiness += 20

        if starting_wardrobe is None:
            starting_wardrobe = default_wardrobe.get_random_selection(40)

        if create_home_location and start_home == None:
            start_home = Room(name+"'s home", name+"'s home", [], apartment_background, [],[],[],False,[0.5,0.5], visible = False, hide_in_known_house_map = False)
            #start_home.link_locations_two_way(downtown)
            start_home.add_object(make_wall())
            start_home.add_object(make_floor())
            start_home.add_object(make_bed())
            start_home.add_object(make_window())
            list_of_places.append(start_home)

        if relationship is None:
            relationship = get_random_from_weighted_list([["Single",100-age],["Girlfriend",50],["Fiancée",120-age*2],["Married",20+age*4]]) #Age plays a major factor.

        if kids is None:
            kids = 0
            if age >=28:
                kids += renpy.random.randint(0,1) #Young characters don't have as many kids

            if age >= 38:
                kids += renpy.random.randint(0,1) #As you get older you're more likely to have one

            if relationship == "Girlfriend":
                kids += renpy.random.randint(0,1) #People who are dating have kids more often than single people

            elif relationship != "Single":
                kids += renpy.random.randint(0,3) #And married/engaged people have more kids still

        if SO_name is None and relationship != "Single":
            SO_name = get_random_male_name()

        new_person = Person(name,last_name,age,body_type,tits,height,body_images,emotion_images,hair_colour,hair_style,skin,eyes,job,starting_wardrobe,personality,
            stat_array,skill_array,sex_list=sex_array,sluttiness=start_sluttiness,obedience=start_obedience,suggest=start_suggest, love=start_love, happiness=start_happiness, home = start_home,
            font = my_custom_font, name_color = name_color , dialogue_color = dial_color,
            face_style = face_style,
            title = title, possessive_title = possessive_title, mc_title = mc_title,
            relationship = relationship, kids = kids, SO_name = SO_name)

        # make sure we have an opinion about clothing
        if not any(x[0] in new_person.opinions for x in ["dresses", "pants", "skirts"]):
            the_opinion_key = get_random_from_list(["dresses", "pants", "skirts"])
            degree = get_random_from_list([-2,-1,1,2])
            new_person.opinions[the_opinion_key] = [degree, False]

        # make sure we have an opinion about shoes and makeup
        if not any(x[0] in new_person.opinions for x in ["boots", "high heels", "makeup"]):
            the_opinion_key = get_random_from_list(["boots", "high heels", "makeup"])
            degree = get_random_from_list([-2,-1,1,2])
            new_person.opinions[the_opinion_key] = [degree, False]

        # make sure we have an opinion about basic sex acts
        if not any(x[0] in new_person.sexy_opinions for x in ["kissing", "masturbating", "giving blowjobs", "being fingered"]):
            the_opinion_key = get_random_from_list(["kissing", "masturbating", "giving blowjobs", "being fingered"])
            degree = get_random_from_list([-2,-1,1,2])
            new_person.sexy_opinions[the_opinion_key] = [degree, False]

        # make sure we have an opinion about clothing to wear
        if not any(x[0] in new_person.sexy_opinions for x in ["skimpy outfits", "not wearing underwear", "showing her tits", "showing her ass", "skimpy uniforms"]):
            the_opinion_key = get_random_from_list(["skimpy outfits", "not wearing underwear", "showing her tits", "showing her ass", "skimpy uniforms"])
            degree = get_random_from_list([-2,-1,1,2])
            new_person.sexy_opinions[the_opinion_key] = [degree, False]

        return new_person

