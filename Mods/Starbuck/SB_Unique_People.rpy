init 2 python:
    SB_STARBUCK_INTRO_COMPLETE = False
    SB_SHOP_STAGE_ONE_DAY = 9999
    SB_SHOP_STAGE_TWO_DAY = 9999

    #starbuck ACTIONS#
    starbuck_vaginal_skillup = Action("Ask about improving vaginal skill", starbuck_vaginal_skillup_requirement, "starbuck_vaginal_skillup_label")
    starbuck_anal_skillup = Action("Ask about improving anal skill", starbuck_anal_skillup_requirement, "starbuck_anal_skillup_label")
    starbuck_oral_skillup = Action("Ask about improving oral skill", starbuck_oral_skillup_requirement, "starbuck_oral_skillup_label")
    starbuck_foreplay_skillup = Action("Ask about improving foreplay", starbuck_foreplay_skillup_requirement, "starbuck_foreplay_skillup_label")
    starbuck_arousal_reduction_one = Action("Ask about lasting longer", starbuck_arousal_reduction_one_requirement, "starbuck_arousal_reduction_one_label")
    starbuck_arousal_reduction_two = Action("Ask about lasting even longer", starbuck_arousal_reduction_two_requirement, "starbuck_arousal_reduction_two_label")
    starbuck_sex_store_investment_one = Action("Ask about investing in her store", starbuck_sex_store_investment_one_requirement, "starbuck_sex_store_investment_one_label")
    starbuck_sex_store_investment_two = Action("Ask about stock levels", starbuck_sex_store_investment_two_requirement, "starbuck_sex_store_investment_two_label")
    starbuck_sex_store_investment_three = Action("Ask about further investment", starbuck_sex_store_investment_three_requirement, "starbuck_sex_store_investment_three_label")
    starbuck_sex_store_promo_one = Action("Ask how business is going", starbuck_sex_store_promo_one_requirement, "starbuck_sex_store_promo_one_label")
    starbuck_sex_store_promo_two = Action("Ask if advertising is working", starbuck_sex_store_promo_two_requirement, "starbuck_sex_store_promo_two_label")
    starbuck_sex_store_promo_three = Action("Ask if women are coming in", starbuck_sex_store_promo_three_requirement, "starbuck_sex_store_promo_three_label")
    starbuck_sex_store_promo_four = Action("Ask if couples are coming in", starbuck_sex_store_promo_four_requirement, "starbuck_sex_store_promo_four_label")
    starbuck_sex_store_promo_five = Action("Ask if couples are coming in", starbuck_sex_store_promo_five_requirement, "starbuck_sex_store_promo_five_label")
    starbuck_spend_the_night = Action("Spend the night with her", starbuck_spend_the_night_requirement, "starbuck_spend_the_night_label")

    def SB_make_swing():
        the_swing = Object("sex swing",["Sit","Low", "Swing"], sluttiness_modifier = 10, obedience_modifier = 10)
        return the_swing

    def SB_make_counter():
        the_counter = Object("counter",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0)
        return the_counter

    def SB_mod_initialization(action_mod):
        starbuck_personality = Personality("starbuck", default_prefix = "relaxed",
        common_likes = ["skirts", "small talk", "the colour blue", "makeup"],
        common_sexy_likes = ["lingerie","taking control",  "doggy style sex", "creampies"],
        common_dislikes = ["working", "research work", "production work"],
        common_sexy_dislikes = [ "masturbating", "giving handjobs"],
        titles_function = starbuck_titles, possessive_titles_function = starbuck_possessive_titles, player_titles_function = starbuck_player_titles)

        starbuck_wardrobe = wardrobe_from_xml("Starbuck_Wardrobe")

        starbuck_home = Room("Starbuck's home", "Starbuck's home", [], apartment_background, [],[],[],False,[0.5,0.5], visible = False, hide_in_known_house_map = False, lighting_conditions = standard_indoor_lighting)
        starbuck_home.add_object(make_wall())
        starbuck_home.add_object(make_floor())
        starbuck_home.add_object(make_bed())
        starbuck_home.add_object(make_window())

        #starbuck_home.link_locations_two_way(downtown)
        list_of_places.append(starbuck_home)

        # init starbuck role
        starbuck_role = Role(role_name ="Sex Shop Owner", actions =[starbuck_vaginal_skillup, starbuck_anal_skillup, starbuck_oral_skillup, starbuck_foreplay_skillup, starbuck_sex_store_investment_one, starbuck_sex_store_investment_two, starbuck_sex_store_investment_three, starbuck_sex_store_promo_one, starbuck_sex_store_promo_two, starbuck_sex_store_promo_three, starbuck_sex_store_promo_four, starbuck_sex_store_promo_five, starbuck_spend_the_night])

        #global starbuck_role
        global starbuck
        starbuck = Sex_Shop_Owner(name = "Starbuck", last_name = "Thrace", age = 32, body_type = "curvy_body", tits="E",  height = 0.95,  body_images = white_skin, expression_images = Expression("Starbuck\'s Expression Set", "white", "Face_4"), hair_colour= ["golden blonde", [0.895, 0.781, 0.656,1]], hair_style = messy_short_hair.get_copy(), skin="white" , \
            eyes = ["green",[0.245, 0.734, 0.269, 1.0]], job = "Sex Shop Owner", wardrobe = starbuck_wardrobe, personality = starbuck_personality, stat_list = [3,4,3],  skill_list = [1,1,4,2,1],  sluttiness = 42,  obedience = -22, suggest = 0, sex_list = [3,3,4,4], love = 0, happiness = 119, \
            home = starbuck_home, font = get_random_font(), work = None, name_color = "#cd5c5c", dialogue_color = "#cd5c5c" , face_style = "Face_4", special_role = [starbuck_role], relationship = "Single")

        starbuck.schedule[1] = sex_store
        starbuck.schedule[2] = sex_store
        starbuck.schedule[3] = sex_store

        starbuck.home.add_person(starbuck)

        # Add a counter to the sex shop
        sex_store.add_object(SB_make_counter())

        # Add StarBuck introduction event to sex store
        starbuck.on_room_enter_event_list.append(starbuck_introduction_event_action)
        return

    # create mod event to trigger creation
    starbuck_introduction_event_action = ActionMod("Starbuck's Sex Shop", starbuck_introduction_requirement, "starbuck_greetings", initialization = SB_mod_initialization, menu_tooltip = "Starbuck's Sex Shop", category = "Misc", allow_disable = False, options_menu = "SB_mod_options_menu")

    #def SB_starbuck_fetish_available():
    #    if SB_get_fetish_count(starbuck) < store.max_fetishes_per_person:


init -1 python:
    def starbuck_introduction_requirement(the_person):
        if mc.location == sex_store:    # only trigger event when in sex store
            return True
        return False

    def starbuck_vaginal_skillup_requirement(the_person):
        if starbuck.shop_progress_stage >= 2:
            if mc.sex_skills["Vaginal"] == 8:
                if mc.business.funds >= 5000:
                    if mc.location == sex_store:
                        return True
                else:
                    return "You need more money."
            elif mc.sex_skills["Vaginal"] < 8:
                return "Max out your vaginal skill first."
            return False
        return False


    def starbuck_anal_skillup_requirement(the_person):
        if starbuck.shop_progress_stage >= 3:
            if mc.sex_skills["Anal"] == 8:
                if mc.business.funds >= 8000:
                    if mc.location == sex_store:
                        return True
                else:
                    return "You need more money."
            elif mc.sex_skills["Anal"] < 8:
                return "Max out your anal skill first."
            return False
        return False

    def starbuck_foreplay_skillup_requirement(the_person):
        if starbuck.shop_progress_stage >= 1:
            if mc.sex_skills["Foreplay"] == 8:
                if mc.business.funds >= 1000:
                    if mc.location == sex_store:
                        return True
                else:
                    return "You need more money."
            elif mc.sex_skills["Foreplay"] < 8:
                return "Max out your foreplay skill first."
            return False
        return False

    def starbuck_oral_skillup_requirement(the_person):
        if starbuck.shop_progress_stage >= 2:
            if mc.sex_skills["Oral"] == 8:
                if mc.business.funds >= 2500:
                    if mc.location == sex_store:
                        return True
                else:
                    return "You need more money."
            elif mc.sex_skills["Oral"] < 8:
                return "Max out your oral skill first."
            return False
        return False

    def starbuck_arousal_reduction_one_requirement(the_person):
        if SB_MOD_MC_AROUSAL_MULT == 1.0:
            if mc.business.funds >= 500:
                if mc.location == sex_store:
                    return True
            else:
                return "You need more money"
        return False

    def starbuck_arousal_reduction_two_requirement(the_person):
        if SB_MOD_MC_AROUSAL_MULT == SB_MOD_MC_AROUSAL_1ST_MULT:
            if mc.business.funds >= 5000:
                if mc.location == sex_store:
                    return True
            else:
                return "You need more money"
        return False

    def starbuck_sex_store_investment_one_requirement(the_person):
        if the_person.shop_progress_stage == 0:
            if mc.business.funds >= 1000:
                return True
            else:
                return "You need more money"

    def starbuck_sex_store_investment_two_requirement(the_person):
        if the_person.shop_progress_stage == 1:
            if (SB_SHOP_STAGE_ONE_DAY + 7) < day:
                if mc.business.funds >= 5000:
                    return True
                else:
                    return "You need more money"
            else:
                return "Wait for her stock to balance out"

    def starbuck_sex_store_investment_three_requirement(the_person):
        if the_person.shop_progress_stage == 2:
            if (SB_SHOP_STAGE_TWO_DAY + 7) < day:
                if mc.business.funds >= 15000:
                    return True
                else:
                    return "You need more money"
            else:
                return "Wait for her stock to balance out"

    def starbuck_sex_store_promo_one_requirement(the_person):
        if the_person.shop_progress_stage > 0:
            if the_person.shop_investment_rate == 1.0:
                return True
        return False

    def starbuck_sex_store_promo_two_requirement(the_person):
        if the_person.shop_progress_stage > 0:
            if the_person.shop_investment_rate == 2.0:
                return True
        return False

    def starbuck_sex_store_promo_three_requirement(the_person):
        if the_person.shop_progress_stage > 1:
            if the_person.shop_investment_rate == 3.0:
                if starbuck.sluttiness > 60:
                    if starbuck.love > 50:
                        return True
                    else:
                        return "Requires 50 Love"
                else:
                    return "Requires 60 sluttiness"
        return False

    def starbuck_sex_store_promo_four_requirement(the_person):
        if the_person.shop_progress_stage > 1:
            if the_person.shop_investment_rate == 4.0:
                if starbuck.sluttiness > 70:
                    if starbuck.love > 60:
                        return True
                    else:
                        return "Requires 60 Love"
                else:
                    return "Requires 70 sluttiness"
        return False

    def starbuck_sex_store_promo_five_requirement(the_person):
        if the_person.shop_progress_stage > 2:
            if the_person.shop_investment_rate == 5.0:
                if starbuck.sluttiness > 90:
                    if starbuck.love > 70:
                        return True
                    else:
                        return "Requires 70 Love"
                else:
                    return "Requires 90 sluttiness"
        return False

    def starbuck_spend_the_night_requirement(the_person):
        if the_person.shop_investment_rate == 6.0:
            if time_of_day < 4:
                return "It isn't night"
            else:
                return True

#SBS10
label starbuck_vaginal_skillup_label(the_person):
    "You explain to [the_person.possessive_title] that you feel like you've stopped improving your skill at vaginal sex. You ask if she has any tips or products for further improvement."
    the_person.char "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of cock rings."
    the_person.char "Personally, I recommend this one, although it is definitely a little pricey..."
    "[the_person.possessive_title] picks one off the shelf, it looks like it has a number of features, like vibration and heat. You eye the price tag warily"
    mc.name "I dunno... is it really worth that much?"
    the_person.char "DEFINITELY. If you can afford it, [the_person.mc_title], it will help take your girl's orgasms to the next level..."
    menu:
        "Purchase ($5000)":
            $ mc.business.funds += -5000
            $ mc.sex_skills["Vaginal"] = 10
            the_person.char "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 70:
                "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person.char "Now... did you maybe want some help... trying this out?"
                menu:
                    "Fuck her" if  mc.current_stamina > 0:
                        "You take a quick look at the instructions. Looks like it should be fairly easy to keep with you and use with your partners from now on..."
                        mc.name "Sounds good, [the_person.title]. Since you recommended it, its only fair you be the first to feel it."
                        the_person.char "Ah... I can't wait! Let's go!"
                        "She quickly takes off some clothes to give you easy access."
                        $ the_person.strip_outfit_to_max_sluttiness(exclude_upper = True)
                        $ mc.current_stamina += -1
                        call fuck_person(the_person, start_position = missionary, start_object = mc.location.get_object_with_name("floor"), skip_intro = True, private = True) from _call_fuck_person_SBS10
                        if the_person.arousal > 160:
                            the_person.char "Oh wow... I've never... I came so many times..."
                            $ the_person.change_obedience (5)
                            $ the_person.change_slut_temp (5)
                            $ the_person.change_slut_core (5)
                            the_person.char "Let's do that again soon!"
                        elif the_person.arousal > 100:
                            the_person.char "Oh wow... The orgasms that thing gives..."
                            $ the_person.change_obedience (2)
                            $ the_person.change_slut_temp (2)
                            $ the_person.change_slut_core (2)
                            the_person.char "Let's do that again soon!"
                        else:
                            the_person.char "Thanks for the fuck!"
                        
                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.reset_arousal()
                        $ the_person.review_outfit(show_review_message = False)

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."

                    "Fuck her\n{size=22}Requires Stamina{/size} (disabled)" if the_person.sluttiness > 60 and mc.current_stamina == 0:
                        "You thank her for the offer, but decide against it for now."
        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

#SBS20
label starbuck_anal_skillup_label(the_person):
    #TODO you offer to make dinner. It takes up time, but you can slip serum to your mom and sister.
    "You explain to [the_person.possessive_title] that you feel like you need something to help take anal sex to the next level. You ask if she has any tips or products for further improvement."
    the_person.char "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of lubrications."
    the_person.char "You see [the_person.mc_title], the key to great anal sex, is using the perfect lube!"
    the_person.char "Personally, I recommend this one, although it is definitely a little pricey..."
    "[the_person.possessive_title] picks one off the shelf. You eye the price tag warily"
    the_person.char "This company has made a ton of advances in lube technology recently."
    the_person.char "This one has full effectiveness with just a small application, and is designed to both lubricate, AND increases blood flow to the nerve endings, making anal more pleasurable for the receiver!"
    mc.name "I dunno... is it really worth that much?"
    the_person.char "DEFINITELY. If you can afford it, [the_person.mc_title], it will help take butt play to the next level..."
    menu:
        "Purchase ($8000)":
            $ mc.business.funds += -8000
            $ mc.sex_skills["Anal"] = 10
            the_person.char "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 90:
                "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person.char "Now... did you maybe want some help... trying this out?"
                menu:
                    "Fuck her ass" if  mc.current_stamina > 0:
                        "You take a quick look at the instructions. Looks like it should be fairly easy to keep with you and use with your partners from now on..."
                        mc.name "Sounds good, [the_person.title]. Since you recommended it, its only fair I use it on you first!"
                        the_person.char "Ah... I can't wait! Let's go!"
                        "She quickly takes off some clothes to give you easy access."
                        $ the_person.strip_outfit_to_max_sluttiness(exclude_upper = True)
                        $ mc.current_stamina += -1
                        call fuck_person(the_person, start_position = SB_anal_standing, start_object = mc.location.get_object_with_name("counter"), skip_intro = True, private = True) from _call_fuck_person_SBS20
                        if the_person.arousal > 160:
                            the_person.char "Oh wow... I've never... I came so many times!"
                            $ the_person.change_obedience (5)
                            $ the_person.change_slut_temp (5)
                            $ the_person.change_slut_core (5)
                            the_person.char "Let's do that again soon!"
                        elif the_person.arousal > 100:
                            the_person.char "Oh wow... I came so hard!"
                            $ the_person.change_obedience (2)
                            $ the_person.change_slut_temp (2)
                            $ the_person.change_slut_core (2)
                            the_person.char "Let's do that again soon!"
                        else:
                            the_person.char "Thanks for the fuck!"

                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.reset_arousal()
                        $ the_person.review_outfit(show_review_message = False)

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."

                    "Fuck her\n{size=22}Requires Stamina{/size} (disabled)" if the_person.sluttiness > 90 and mc.current_stamina == 0:
                        "You thank her for the offer, but decide against it for now."
        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

#SBS30
label starbuck_oral_skillup_label(the_person):
    #TODO you offer to make dinner. It takes up time, but you can slip serum to your mom and sister.
    "You explain to [the_person.possessive_title] that you feel like you've stopped improving your skill at oral sex. You ask if she has any tips or products for further improvement."
    the_person.char "Oh [the_person.mc_title]... I think I can probably help you with that!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of instructional books and videos."
    the_person.char "Personally, I recommend this one, although it is definitely a little pricey..."
    "[the_person.possessive_title] picks a video off the shelf. You eye the price tag warily."
    mc.name "Cunnilingus, multiple orgasms, and squirting. The all in one how to guide."
    mc.name "I dunno... is it really worth that much?"
    the_person.char "DEFINITELY. If you can afford it, [the_person.mc_title], it will help you make your girl orgasm over and over again..."
    menu:
        "Purchase ($2500)":
            $ mc.business.funds += -2500
            $ mc.sex_skills["Oral"] = 10
            the_person.char "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 45:
                "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person.char "Now... did you maybe want some help... trying this out?"
                menu:
                    "Eat her pussy" if  mc.current_stamina > 0:
                        mc.name "Sounds good, [the_person.title]."
                        the_person.char "Ah... okay! Let me close up really quick, I have a movie player in the back. We can go back and watch it together and then try it out!"
                        "You head to the back of hte store with [the_person.possessive_title]. Watching the video, you learn several new tips and tricks for giving awesome oral."
                        "When you finish, you see [the_person.possessive_title] looking at you."
                        the_person.char "Wow, that was interesting!... you ready to give it a try, [the_person.mc_title]?"
                        "She quickly takes off some clothes to give you easy access."
                        $ the_person.strip_outfit_to_max_sluttiness(exclude_upper = True)
                        call fuck_person(the_person, start_position = SB_Oral_Laying, start_object = mc.location.get_object_with_name("floor"), skip_intro = True, private = True) from _call_fuck_person_SBS30
                        if the_person.arousal > 160:
                            the_person.char "Oh my god, I came so many times... did you make me squirt?"
                            $ the_person.change_obedience (5)
                            $ the_person.change_slut_temp (5)
                            $ the_person.change_slut_core (5)
                            the_person.char "Let's do that again soon!"
                        elif the_person.arousal > 100:
                            the_person.char "Oh wow... That felt so good!"
                            $ the_person.change_obedience (2)
                            $ the_person.change_slut_temp (2)
                            $ the_person.change_slut_core (2)
                            the_person.char "Let's do that again soon!"
                        else:
                            the_person.char "Thanks for the fuck!"

                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.reset_arousal()
                        $ the_person.review_outfit(show_review_message = False)

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."
                        "You head back to your house and watch the video. You pick up several new tips and tricks to try next to eat a girl out!"

                    "Eat her pussy\n{size=22}Requires Stamina{/size} (disabled)" if the_person.sluttiness > 60 and mc.current_stamina == 0:
                        "You thank her for the offer, but decide against it for now."
                        "You head back to your house and watch the video. You pick up several new tips and tricks to try next to eat a girl out!"
        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

#SBS40
label starbuck_foreplay_skillup_label(the_person):
    #TODO you offer to make dinner. It takes up time, but you can slip serum to your mom and sister.
    "You explain to [the_person.possessive_title] that you feel like you've stopped improving your skill at foreplay. You ask if she has any tips or products for further improvement."
    the_person.char "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of sex toys."
    the_person.char "Personally, I recommend this one, although it is definitely a little pricey..."
    "[the_person.possessive_title] picks one off the shelf, it looks like it has a number of features, like vibration and heat. You eye the price tag warily"
    mc.name "I dunno... is it really worth that much?"
    the_person.char "DEFINITELY. If you can afford it, [the_person.mc_title], it will help take your girl's orgasms to the next level..."
    menu:
        "Purchase ($1000)":
            $ mc.business.funds += -1000
            $ mc.sex_skills["Foreplay"] = 10
            the_person.char "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 30:
                "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person.char "Now... did you maybe want some help... trying this out?"
                menu:
                    "Finger her" if  mc.current_stamina > 0:
                        "You take a quick look at the instructions. Looks like it should be fairly easy to keep with you and use with your partners from now on..."
                        mc.name "Sounds good, [the_person.title]. Since you recommended it, its only fair you be the first to feel it."
                        the_person.char "Ah... I can't wait! Let's go!"
                        "She quickly takes off some clothes to give you easy access."
                        $ the_person.strip_outfit_to_max_sluttiness(exclude_upper = True)
                        $ mc.current_stamina += -1
                        call fuck_person(the_person, start_position = standing_grope, skip_intro = True, private = True) from _call_fuck_person_SBS40
                        if the_person.arousal > 160:
                            the_person.char "Oh wow... I've never... I came so many times..."
                            $ the_person.change_obedience (5)
                            $ the_person.change_slut_temp (5)
                            $ the_person.change_slut_core (5)
                            the_person.char "Let's do that again soon!"
                        elif the_person.arousal > 100:
                            the_person.char "Oh wow... The orgasms that thing gives..."
                            $ the_person.change_obedience (2)
                            $ the_person.change_slut_temp (2)
                            $ the_person.change_slut_core (2)
                            the_person.char "Let's do that again soon!"
                        else:
                            the_person.char "Thanks for the fuck!"

                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.reset_arousal()
                        $ the_person.review_outfit(show_review_message = False)

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."

                    "Fuck her\n{size=22}Requires Stamina{/size} (disabled)" if the_person.sluttiness > 60 and mc.current_stamina == 0:
                        "You thank her for the offer, but decide against it for now."
        "Not right now":
            "You thank her for the help, but decide against it for now."
    return


#SBS50
label starbuck_arousal_reduction_one_label(the_person):
    $ global SB_MOD_MC_AROUSAL_MULT
    "You explain to [the_person.possessive_title] that you feel like you're having trouble pleasing the women you've been with lately. You ask if she has anything that can help you last longer during sex"
    the_person.char "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of numbing creams and similar products."
    the_person.char "While there are a ton of products on the market to help with you are talking about, the one I've gotten the best feedback from is this one."
    "[the_person.possessive_title] picks a cream off the shelf. You eye the price tag warily"
    mc.name "I dunno... is it really worth that much?"
    the_person.char "I have gotten a lot of good reviews from men... and their women! It's made so you only have to apply it once a day, and just gives a slight numbing effect."
    the_person.char "Perfect to last just a bit longer, no matter when you have sex that day!"
    menu:
        "Purchase ($500)":
            $ mc.business.funds += -500
            $ SB_MOD_MC_AROUSAL_MULT = SB_MOD_MC_AROUSAL_1ST_MULT
            the_person.char "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
            "Before you leave, you take a look at the instructions. Hopefully this will help let you last longer! You head to the bathroom and apply a little bit of it."
            "NOTE: You now gain arousal at 90 percent of the normal rate"
        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

#SBS60
label starbuck_arousal_reduction_two_label(the_person):
    #TODO you offer to make dinner. It takes up time, but you can slip serum to your mom and sister.
    $ global SB_MOD_MC_AROUSAL_MULT
    "You explain to [the_person.possessive_title] that you feel like you're still having trouble pleasing the women you've been with lately, even with the numbing cream. You ask if she has anything that can help you last longer during sex"
    the_person.char "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of pharmaceutical products."
    the_person.char "While there are a ton of products on the market to help with you are talking about, the one I've gotten the best feedback from is this one."
    "[the_person.possessive_title] picks a pill off the shelf. You eye the price tag warily"
    mc.name "I dunno... is it really worth that much?"
    the_person.char "This company has made a ton of advances in this area recently!"
    the_person.char "They've done numerous double blind studies. Almost all men who took it daily found they lasted longer in bed!"
    menu:
        "Purchase ($5000)":
            $ mc.business.funds += -5000
            $ SB_MOD_MC_AROUSAL_MULT = SB_MOD_MC_AROUSAL_2ND_MULT
            the_person.char "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
            "Before you leave, you take a look at the instructions. You take a pill out and swallow it with a quick gulp of water."
            "NOTE: You now gain arousal at 75 Percent of the normal rate"
        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

label starbuck_sex_store_investment_one_label(the_person):
    mc.name "So, I'm seriously considering investing in your shop. What kind of stock can you get if I invest $1000?"
    the_person.char "Oh! That would be amazing! Well, with that money, I could get basic toys, creams, and lubricants. There are some pretty good creams for male endurance enhancement you can get..."
    the_person.char "As well as some toys for better foreplay and masturbation. Some dildos, male masturbation sleeves, vibrating rings..."
    "That sounds like a pretty list of stuff that you would be interested in buying if you were to go to a sex shop."
    "Do you want to invest?"
    menu:
        "Invest $1000":
            "You discuss with [the_person.possessive_title] for a while what the terms of your investment are. Once you are both happy, you write her a check from your business account."
            $ mc.business.funds += -1000
            $ the_person.change_happiness (20)
            $ the_person.change_obedience (5)
            the_person.char "Don't worry, [the_person.mc_title]! You won't regret this!"
            "Even if the business winds up flopping, in your heart you know you are doing the right thing, helping this widow achieve her dream of owning a sex shop."
            $ starbuck.shop_investment_total += 1000
            $ starbuck.shop_stage_one_investment_total += 1000
            $ starbuck.shop_progress_stage = 1
            $ starbuck.shop_investment_rate = 1.0
            $ SB_SHOP_STAGE_ONE_DAY = day
        "Reconsider":
            "You decide you need more time to consider the investment."
            mc.name "Sorry, [the_person.title], I haven't made up my mind yet. Thanks for the info though, I'll be back when I've reconsidered."
            "[the_person.possessive_title] frowns, but she nods in understanding."
            the_person.char "Of course, [the_person.mc_title]. It is a lot of money we are talking about, you should be careful with your hard earned money!"
    return

label starbuck_sex_store_investment_two_label(the_person):
    "While things at [the_person.possessive_title]'s sex shop have definitely picked up, you can't help but notice there are several sections of the store that lack variety."
    "There are some dildos, but only a couple varieties. Same with condoms, lubricants, and other items."
    "You decide to bring it up with [the_person.possessive_title]."
    mc.name "Hey [the_person.title]. I see things are going good around here, but I'm curious. You've got basic items around the store, but why don't you have more variety?"
    "She frowns and responds."
    the_person.char "Well, I'd love to have more variety, but unfortunately I'm not bringing in very much profit. I'm in the black now, thanks to your investment, but I'm not really making enough to expand inventory significantly."
    "You watch as a customer comes in the store. He looks around for a bit, then leaves. You wonder how much business you are missing out on due to the lack of stock."
    mc.name "Have you done any research on what it would take to get more variety in?"
    "She nods."
    the_person.char "I have. And its too much for me to ask from you. You've already done so much for me and shop..."
    "You interrupt her."
    mc.name "How much?"
    "[the_person.possessive_title] clears her throat."
    the_person.char "Well, the way I added it up, to expand beyond just basic stock, and include a variety of novelty items, edibles, and accessories would be about $5000."
    "You consider the amount. It is steep, to be sure, but it also might be a good investment."
    if starbuck.shop_investment_rate == 3.0 :
        "It might also open up new opportunities with [the_person.possessive_title]. You wouldn't mind a few more excuses to get intimate with her..."
    "Do you want to invest?"
    menu:
        "Invest $5000":
            "You discuss with [the_person.possessive_title] for a while what the terms of your investment are. Once you are both happy, you write her a check from your business account."
            $ mc.business.funds += -5000
            $ the_person.change_happiness (20)
            $ the_person.change_love (5)
            $ the_person.change_obedience (5)
            the_person.char "Wow... are you really doing this? I can hardly believe it. Don't worry, I won't let you down!"
            "Even as you write you check, she is already going on about the stock she'll be able to get."
            the_person.char "...hmmm... OH! And edible underwear! And nipple clamps! Maybe some handcuffs..."
            $ starbuck.shop_investment_total += 5000
            $ starbuck.shop_stage_two_investment_total += 5000
            $ starbuck.shop_progress_stage = 2
            "She is so excited, you can tell already, this is an investment that is going to pay off for you... one way or another!"
            $ SB_SHOP_STAGE_TWO_DAY = day

        "Reconsider":
            "You decide you need more time to consider the investment."
            mc.name "Sorry, [the_person.title], I haven't made up my mind yet. Thanks for the info though, I'll be back when I've reconsidered."
            "[the_person.possessive_title] frowns, but she nods in understanding."
            the_person.char "Of course, [the_person.mc_title]. It is a lot of money we are talking about, you should be careful with your hard earned money!"
    return

label starbuck_sex_store_investment_three_label(the_person):
    "You take a look around at the sex shop. You see a sexy looking redhead checking out some lingerie. In the back corner is a guy looking at strapons. In an aisle you see a couple looking at edibles."
    "Everyone seems to be shopping and finding what they are looking for... but you can't help but have a nagging in you head that you could make the store even better."
    mc.name "Hey [the_person.title]. Looks like things are going great here, how is business?"
    the_person.char "Oh, its been great! I've been meeting so many new people, and I'm actually making a decent income now!"
    "She gives you a warm smile. It nice seeing her so happy with her work."
    mc.name "Are you pretty happy with all the stuff you are able to keep in stock now? Seems like you've got just about anything you could ever need."
    the_person.char "Well, I don't know about EVERY thing, but we definitely have a great selection now."
    mc.name "What do you mean?"
    the_person.char "Well, goodness, there is so much stuff out there, theres no way we could fit it all in this little store. That's why I'm saving up."
    the_person.char "The store next to us recently went ouf of business, once I save up enough money, I'm gonna buy it out and expand my store. Turn this place into [the_person.name]'s MEGA sex shop!"
    "You consider what she is saying."
    mc.name "What kind of stuff could you carry with the extra space that you aren't carrying now?"
    the_person.char "Oh, well in here we sell mostly accessories, lingerie, that kind of thing, but with more room we could get in all kinds of kinky stuff. Sex furniture, like chairs and swings, massage tables..."
    "Wow, you had no idea there was so much stuff out there..."
    the_person.char "...could even get into bondage gear, fetish items like furry tail butt plugs... I mean, the sky is the limit, you know?"
    "So far, all of your investments in the shop have paid off... plus, you start to imagine what it would be like to try some of these items with [the_person.possessive_title]..."
    mc.name "Let's say I was interested in investing again... How much would you need to make all that happen?"
    "[the_person.possessive_title]'s mouth drops in surprise."
    the_person.char "Well... my estimates put it at about $15000. But please, don't think you have to do that! I'm making decent money, I'll be able to afford it eventually..."
    "You consider the investment."
    menu:
        "Invest $15000":
            "How about this. You've done an incredible job managing this place. How about if I front the money, and from now on we're partners?"
            the_person.char "Wow... partners?... I mean... you're talking business partners, right?"
            if starbuck.shop_investment_rate > 3.0:
                mc.name "[the_person.title], I'd be lying if I said I don't thoroughly enjoy the time we've spent together. So yeah, we would be business partners, but I'd also love the excuse to spend more time with you."
                $ the_person.draw_person(emotion = "happy")
                if starbuck.love > 60:
                    the_person.char "Oh, [the_person.mc_title]... I'm so glad to hear that. I feel the same way."
                else:
                    the_person.char "Wow... that's nice to hear! I'm interesting in spending more time with you in the future too."
            else:
                mc.name "Of course, we'll keep things perfectly professional..."
            $ mc.business.funds += -15000
            $ the_person.change_happiness (20)
            $ the_person.change_love (10)
            $ the_person.change_obedience (10)
            the_person.char "Wow... this is it! The opportunity of a lifetime. I'm speechless [the_person.mc_title]. Thank you so much!"
            "Even as you write you check, she is beginning to plan the expansion to the shop."
            $ starbuck.shop_investment_total += 15000
            $ starbuck.shop_stage_three_investment_total += 15000
            $ starbuck.shop_progress_stage = 3

        "Reconsider":
            "You decide you need more time to consider the investment."
            mc.name "Sorry, [the_person.title], I haven't made up my mind yet. Thanks for the info though, I'll be back when I've reconsidered."
            "[the_person.possessive_title] frowns, but she nods in understanding."
            the_person.char "Of course, [the_person.mc_title]. It is a lot of money we are talking about, you should be careful with your hard earned money!"
    return

#SBS70
label starbuck_sex_store_promo_one_label(the_person):
    the_person.char "Well, it is going okay. Thanks to your investment, I'm finally turning a profit at least!"
    the_person.char "But, I feel like I'm just not getting the foot traffic I need. I need to find a way to attract more customers."
    "You consider what she is saying. Given the nature of the store, what you really need is some seriously sexy advertising."
    "You check out [the_person.possessive_title]. She has an amazing body. Maybe you should get her to pose with some of her product, take some pictures and turn it into an ad!"
    "[the_person.possessive_title] sees you checking her out, and the wheels turning in your head as you think about it."
    the_person.char "[the_person.mc_title]? Are you still with me here? Or are you too busy checking me out?"
    "You give her a smile as a plan comes together."
    mc.name "I know just what you need to do [the_person.title], that will help drive traffic here. You need to do some advertising!"
    "[the_person.possessive_title] shakes her head."
    the_person.char "I do, but it doesn't seem to be very effective."
    mc.name "That's right, because your advertising is so plain! What you need to do is get a sexy woman in your advertising, in some lingerie, showing of some of the products you have for sale!"
    "She thinks about your proposal."
    the_person.char "That sounds great, [the_person.mc_title], but... where am I going to find a model for something like that? Let alone pay her?"
    "You pretend to think hard about it."
    mc.name "Well, [the_person.title], I think YOU are pretty fucking sexy..."
    "[the_person.possessive_title] quickly realizes you are suggesting that she dresses up in lingerie for some advertising."

    if the_person.sluttiness > 50 : #We easily pass the sluttiness check.
        the_person.char "Oh! I mean, that would be fun for sure... but... do you really think I'm sexy enough for that?"
        "You give her another once over."
        mc.name "Absolutely. If I was a guy and I saw you in some lingerie on an advertisement, I'd be sure to come check the store out!"
        the_person.char "Hmm... okay! If nothing else, I'll have some nice pictures I can send to guys who hit me up on my dating app..."
    elif the_person.sluttiness > 20 :  #Barely passes the sluttiness check.
        the_person.char "Oh... I don't know [the_person.mc_title]. I mean, believe me, I love sex, I even opened a shop... But to put myself out there in public like that? Are you sure I'm sexy enough for that?"
        "You make a show of checking her out."
        mc.name "Absolutely. If I was a guy and I saw you in some lingerie on an advertisement, I'd be sure to come check the store out!"
        the_person.char "Hmm... okay, I mean, we can give a shot anyway. What's the worst that could happen?"
    else: #She fails the sluttiness check. Give dialogue to come back when shes sluttier.
        the_person.char "Wow, [the_person.mc_title]. I'm sorry I just... I don't think I could do that. To put myself out there in public like that?"
        "[the_person.possessive_title] considers for a bit."
        the_person.char "No, I'm sorry [the_person.mc_title]. It's a great idea, I just don't think I'm ready to do something like that. I'm sorry!"
        "You understand she's just not ready for something like that. Maybe at some point in the future she'd be willing to do something like that."
        return

    $ SB_advert_one_outfit = Outfit("Lingerie Set Classic Black")
    $ SB_advert_one_outfit.add_upper(lace_bra.get_copy(),colour_black)
    $ SB_advert_one_outfit.add_lower(lace_panties.get_copy(), colour_black)
    $ SB_advert_one_outfit.add_feet(garter_with_fishnets.get_copy(), colour_black)

    $ SB_advert_two_outfit = Outfit("Lingerie Set Blue Nightgown")
    $ SB_advert_two_outfit.add_upper(thin_bra.get_copy(),colour_sky_blue)
    $ SB_advert_two_outfit.add_lower(cute_panties.get_copy(), colour_sky_blue)
    $ SB_advert_two_outfit.add_upper(nightgown_dress.get_copy(), colour_sky_blue)

    $ SB_advert_three_outfit = Outfit("Lingerie Set Pink Onepiece")
    $ SB_advert_three_outfit.add_upper(lacy_one_piece_underwear.get_copy(),colour_pink)
    $ SB_advert_three_outfit.add_feet(fishnets.get_copy(), colour_pink)

    $ the_person.wardrobe.add_underwear_set(SB_advert_one_outfit)
    $ the_person.wardrobe.add_underwear_set(SB_advert_two_outfit)
    $ the_person.wardrobe.add_underwear_set(SB_advert_three_outfit)

    "Yes! [the_person.possessive_title] is gonna show off her amazing body of hers while you take pictures!"
    "You coordinate with her on the items you want to advertise and some outfits that would be suitable to show them off."
    #Pose walking away#
    "You collect the items, while [the_person.possessive_title] grabs a few sets of lingerie. You meet her in the back room."
    #pose standing#
    "Once in the backroom, you can see that [the_person.possessive_title] has three outfits picked out. Some classic black lingerie with fishnet and garter belt, a light blue nightgown, and a pink lacy one piece."
    "The first item to model is a bottle of some good quality, oil based lube. You figure a regular standing pose should work for this."
    "Which lingerie should you have her use for this?"
    menu:
        "The classic black set":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.outfit = SB_advert_one_outfit.get_copy()
            $ the_person.draw_person()
        "The blue nightgown":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.outfit = SB_advert_two_outfit.get_copy()
            $ the_person.draw_person()
        "the pink one piece":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.outfit = SB_advert_three_outfit.get_copy()
            $ the_person.draw_person()
    "Now dressed in her outfit, [the_person.possessive_title] hands you her phone. She grabs the first item, the bottle of lubricant."
    mc.name "Wow... you look great..."
    "You murmur. She smiles at your compliment."
    mc.name "Okay, why don't you just stand and put your hand on your hip."
    $ starbuck.draw_person(position = "stand4", emotion = "happy")
    "[the_person.possessive_title] strikes a pose for you. You take several pictures, trying to find the best angles to show off her body... and the product."
    "You can tell that [the_person.possessive_title] is actually enjoying herself and your attention. Her cheeks are starting to get a little flushed."
    $ the_person.change_arousal(10)
    "The next item for her to model will be a male masturbation sleeve."
    "It is designed to look like a famous porn actress' asshole, so you figure to model this product, [the_person.possessive_title] should have her back to you."
    "Which lingerie should you have her use for this?"
    menu:
        "The classic black set":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.outfit = SB_advert_one_outfit.get_copy()
            $ the_person.draw_person()
        "The blue nightgown":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.outfit = SB_advert_two_outfit.get_copy()
            $ the_person.draw_person()
        "the pink one piece":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.outfit = SB_advert_three_outfit.get_copy()
            $ the_person.draw_person()
    "Now dressed in her outfit, [the_person.possessive_title] looks to you for direction."
    mc.name "[the_person.title]. You look incredible..."
    "She clears her throat to get your attention."
    mc.name "Right! Why don't you turn around and peek back at me and hold this to the side, right next to your hip."
    $ starbuck.draw_person(position = "back_peek", emotion = "happy")
    "[the_person.possessive_title] turns around and looks back at you. You get a bunch of pictures of her amazing ass. You almost forget to get pictures of the product!"
    mc.name "Perfect! These pictures are perfect, you are going to get a flood of guys in here looking for this!"
    "Once you are done [the_person.possessive_title] turns back to face you."
    $ starbuck.draw_person(position = "stand2", emotion = "happy")
    $ the_person.change_arousal(20)
    "The attention you are giving her is really starting to excite [the_person.possessive_title]. You can see her nipples sticking out proudly in her outfit."
    "The last item for her to model is a dildo. You figure since you are mainly targeting a male audience with this advertisement, a good pose for her would be on her knees, like shes getting ready to put it in her mouth."
    "Which lingerie should you have her use for this?"
    menu:
        "The classic black set":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.outfit = SB_advert_one_outfit.get_copy()
            $ the_person.draw_person()
        "The blue nightgown":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.outfit = SB_advert_two_outfit.get_copy()
            $ the_person.draw_person()
        "the pink one piece":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.outfit = SB_advert_three_outfit.get_copy()
            $ the_person.draw_person()
    "As she changes you stand and gawk at her amazing body."
    the_person.char "Don't worry [the_person.mc_title], we're almost done. What should I do for this one?"
    mc.name "I think you should get down on your knees, you know, like you are getting ready to suck on it."
    the_person.char "Oh! That sounds like fun... sucking on a... a dildo, right!"
    $ starbuck.draw_person(position = "blowjob")
    "[the_person.possessive_title] gets down on her knees. She looks at the dildo longingly. You take multiple pictures of her."
    $ the_person.change_arousal(30)
    the_person.char "Mmm... it looks so tasty..."
    "[the_person.possessive_title] opens her mouth, and slowly starting to run her tongue along the dildo. You see one of her hands slowly drift down between her legs and she begins to touch herself."
    "She has her eyes closed, so you snap a few more pictures of her sucking on the dildo. She suddenly realizes what she is doing and pulls off."
    the_person.char "Right! So, I thought maybe a picture like that... I mean maybe we could include a picture like that free with every purchase... or something?"
    "You can tell she is fumbling with her words, trying to cover up that she lost her awareness and started sucking on the dildo."
    "You are all done with the pictures... maybe you should offer her something else to suck on?"
    menu:
        "Want a real dick?" if mc.current_stamina > 0:
            "[the_person.possessive_title] looks up at you, still on her knees."
            the_person.char "Oh [the_person.mc_title], getting all dressed up has me all turned on. If you'd let me do that, I would really appreciate it."
            mc.name "Go ahead, you look amazing. I can't wait to feel your mouth."
            "You walk up to [the_person.possessive_title]. She unzips your pants and pulls your cock out from your pants."
            "She runs her tongue up and down the sides a few times, then opens her mouth and sucks you into her hot mouth."
            call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True) from _call_fuck_person_SBS70
            if the_person.arousal > 100:
                "[the_person.possessive_title] takes a few minutes to recover from her orgasm. Eventually she gets up."
            else:
                "After you finish, [the_person.possessive_title] takes a second, then gets up."
            $ starbuck.draw_person(position = "stand2", emotion = "happy")
            $ mc.current_stamina += -1
            $ the_person.reset_arousal()
            the_person.char "Mmm... That was nice. It's been a while since I sucked on a hard cock. It was kinda nice!"
            if the_person.get_opinion_score("giving blowjobs") < 1:
                $ the_person.sexy_opinions["giving blowjobs"] = [1, True]
                "[the_person.possessive_title] now likes giving blowjobs!"
            "You are still recovering from your orgasm. You take a look at her phone and start looking at the pictures you got."
            $ the_person.shop_investment_rate = 2.0
            the_person.char "If this advertisement works, we'll have to make more right?"
            mc.name "Definitely. Alright, I'll go ahead and get some advertisements done, and we'll see if we can't get better foot traffic in here."
            "You say goodbye to [the_person.possessive_title] and head out. With pictures like these, you are sure the business here will increase."
        "Want a real dick? \nRequires: Stamina (disabled)" if mc.current_stamina == 0:
            pass
        "Give her some privacy":
            "You decide to give her some time to yourself. You use her phone to forward all the pictures you took to your account."
            mc.name "Okay, those should be good. I'll go ahead and get some advertisements done, and we'll see if we can't get better traffic in here."
            "You say goodbye to [the_person.possessive_title] and head out. With pictures like these, you are sure the business here will increase."
            $ the_person.review_outfit(show_review_message = False)
            $ the_person.shop_investment_rate = 2.0

    python:
        del SB_advert_one_outfit
        del SB_advert_two_outfit
        del SB_advert_three_outfit
        the_person.reset_arousal()
        the_person.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.
        mc.location.show_background()
        renpy.scene("Active")
    return #Toy modeling, ends in blowjob

#SBS80
label starbuck_sex_store_promo_two_label(the_person):
    the_person.char "Oh, business is going pretty good! I have definitely been getting more traffic ever since... you know... helped me with some advertising flyers."
    "[the_person.possessive_title]'s voice trails off for a second before she continues."
    the_person.char "And its been nice, all the attention I've been getting from the guys that come in here."
    the_person.char "But, its only guys coming in! I feel like I'm really missing market share, but I can't figure out a way to get more women in here!"
    "You consider her problem for a bit. Then you come up with an idea."
    mc.name "Have you ever considered doing reviews of the products you carry?"
    "She pauses and looks at you."
    the_person.char "I'm not sure what you mean."
    mc.name "Well, for example, that dildo over there. If I'm a girl, how do I know how well its going to hold up? Is it going to hit all the right places? Is it easy to clean?"
    "[the_person.possessive_title] thinks about what you are saying."
    mc.name "What we could do is, take a video of yourself trying out the product. We post it online, and make sure people know, come get it here!"
    the_person.char "So... you're basically saying, I should take a video of myself... using dildos? And post it online?"
    #Sluttiness Check!
    if the_person.sluttiness > 70 : #We easily pass the sluttiness check.
        $the_person.draw_person(emotion = "happy")
        the_person.char "Oh! That's an amazing idea! I could put QR labels next to the tags too, so people can scan it with their phone and check it out!"
        "[the_person.possessive_title] seems to really like the idea."
        mc.name "Hey, that's a good idea too! Let's do it!"
    elif the_person.sluttiness > 40 :  #Barely passes the sluttiness check.
        the_person.char "Oh... I don't know [the_person.mc_title]. I mean, it sounds like it would work... but videos of me, on the internet? Using sex toys?"
        "You do your best to reassure her."
        mc.name "Absolutely. I mean, when have I steered you wrong? The last idea worked too, didn't it?"
        the_person.char "Hmm... okay. Let's do it!"
    else: #She fails the sluttiness check. Give dialogue to come back when shes sluttier.
        the_person.char "Wow, [the_person.mc_title]. I'm sorry I just... I don't think I could do that. To put myself out there on the internet like that?"
        "[the_person.possessive_title] considers for a bit."
        the_person.char "No, I'm sorry [the_person.mc_title]. It's a great idea, I just don't think I'm ready to do something like that. I'm sorry!"
        "You understand she's just not ready. Maybe at some point in the future she'd be willing to do something like that."
        return
    "[the_person.possessive_title] looks at you for a moment."
    the_person.char "So... You're going to help me... right? I mean, I'm sure I could figure it out eventually, but it would be really nice to have someone help me make the first couple..."
    "You consider her request. It sounds pretty reasonable, plus maybe you'll get to watch her masturbate!"
    mc.name "Sure, I'd be glad to help! Any idea which products you would like to review first?"
    the_person.char "Yeah, I've got a pretty good idea. Meet me in the back in a few minutes while I get everything together!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] walks away. You see her going around and grabbing a few things from around the store. You decide to head to the back room and wait for her there."
    $ SB_advert_four_outfit = Outfit("Lingerie Set Dark Blue Corset")
    $ SB_advert_four_outfit.add_upper(corset.get_copy(),[0.15, 0.2, 0.45, 1])
    #$ SB_advert_four_outfit.add_lower(lace_panties.get_copy(), [0.15, 0.2, 0.45, 1])
    $ SB_advert_four_outfit.add_feet(garter_with_fishnets.get_copy(), [0.15, 0.2, 0.45, 1])
    $ SB_advert_four_outfit.add_feet(heels.get_copy(), colour_black)
    $ the_person.draw_person(position = "stand2")
    "She joins in the backroom carrying a couple of dildos and a set of lingerie."
    the_person.char "Okay, let me just get changed really quick."
    $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
    "Once she finishes stripping, she grabs the lingerie set and puts it on."
    $ the_person.outfit = SB_advert_four_outfit.get_copy()
    $ the_person.draw_person()
    $ the_person.wardrobe.add_outfit(SB_advert_four_outfit)
    $ del SB_advert_four_outfit
    "You check out [the_person.possessive_title] in her outfit. Damn she looks hot!"
    the_person.char "Okay, so here's what I'm thinking..."
    "[the_person.possessive_title] starts going over the details of how she wants to do it. You take mental notes. Soon you are ready to begin."
    "You get the camera recording as [the_person.possessive_title] begins her reviews."
    $ the_person.draw_person(position = "stand4")
    the_person.char "Hello! This is [the_person.name]! Owner of [the_person.name]'s sex shop, and welcome to my review of the Ramboner dildo by..."
    "You check to make sure she is in frame. She talks for a few minutes about about the quality of the toy."
    the_person.char "Okay! Time to try it out!"
    $ the_person.draw_person(position = "missionary")
    "[the_person.possessive_title] lays down on the floor. She begins by stroking herself with the dildo a few times up and down her slit."
    $ the_person.change_arousal(5)
    the_person.char "Mmm, that texturing feels great sliding up and down, let's see how it feels going in..."
    "She slowly takes the head of the dildo and begins pushing it into her pussy."
    the_person.char "Oh! Wow the curve on the tip feels great sliding in..."
    $ the_person.change_arousal(15)
    "[the_person.possessive_title] begins working the dildo in and out of her."
    the_person.char "Yes! And with the flared base, it's easy to hold... so I can control the depth... oh fuck!"
    $ the_person.change_arousal(15)
    "She is working the dildo in and out of herself now at a steady pace. Each time she pulls it out, you can see her juices glistening on the toy."
    the_person.char "The texturing on the outside... it really... stimulates the nerve endings as it... oh god."
    $ the_person.change_arousal(15)
    "[the_person.possessive_title] is now fucking herself earnestly with the dildo. The sights and sounds are starting to turn you on. You absentmindedly begin to stroke yourself through your pants."
    the_person.char "Okay... now seems like a good time to test the curve, and see how well it stimulates the g-spot."
    "She pulls the dildo mostly out, then changes the angle of penetration. She gives herself short, shallow thrusts, focusing on her g-spot."
    the_person.char "YES! Okay this toy stimulates the g-spot... SO GOOD."
    $ the_person.change_arousal(20)
    "[the_person.possessive_title] looks up and notices you stroking yourself. Her mouth goes wide in a moan as her orgasm approaches."
    "She looks directly at you and cries out."
    the_person.char "YES! OH god, fuck me... YES! FUCK ME!!!"
    $ the_person.change_arousal(25)
    $ the_person.draw_person(position = "missionary", emotion = "orgasm")
    "[the_person.possessive_title]'s body begins to spasm as she orgasms. She shoves the toy in deep inside her. Her juices are trickling down beneath her out of her cunt."
    "Her body relaxes after she finishes. She slowly pulls the toy from her sopping wet cunt."
    the_person.char "So... overall... I rate this toy... a solid 9 out of 10... thanks for watching!"
    $ the_person.shop_investment_rate = 3.0
    "You step out from behind the camera. Her sultry eyes look up at you as you walk over to her."
    if (the_person.love > 50):
        the_person.char "Oh [the_person.mc_title]. That toy was so good... but honestly the whole time I was imagining it was you fucking me..."
        "She pushes herself up on her elbows, but makes no motion to stand up."
        the_person.char "Don't get me wrong, toys are great, but I want you! Seeing you touching yourself... looking at me... Please fuck me [the_person.mc_title]!"
    else:
        the_person.char "Damn [the_person.mc_title]. I'm glad you were enjoying the show..."
        "She pushes herself up on her elbows, but makes no motion to stand up."
        the_person.char "Toys are great... but nothing beats a real cock inside me. Would you please fuck me [the_person.mc_title]?"
    menu:
        "Fuck Her" if mc.current_stamina > 0:
            mc.name "[the_person.title], that was so hot! I can't wait to bury myself into your amazing cunt."
            "She smiles at your response."
            the_person.char "Then come get some! I just came, no need to warm me up!"
            "You quickly strip out of your clothes and lay down on top of her."
            if (the_person.love > 50):
                "[the_person.possessive_title] wraps her arms around you and holds you close. You move your face in for a kiss and she greedily accepts your tongue in your mouth."
                "While you make out with her, you use one hand to get yourself lined up with her soaked slit. You slide in easily with no resistance, bottoming out inside her."
            else:
                "[the_person.possessive_title] runs her hands along your sides as you get into position."
                "She grabs your cock with your hand and points it at her soaked slit. With one smooth motion you thrust into her. She's so wet you glide in with no resistance."
            "Wasting no time, you begin thrusting into her. Her pussy feels amazing wrapped around you."
            call fuck_person(the_person, start_position = missionary, start_object = make_floor(), skip_intro = True, girl_in_charge = False) from _call_fuck_person_SBS80
            $ mc.current_stamina += -1
            "[the_person.possessive_title] lays there in a daze. Between the toy and your cock, she had multiple orgasms."
            if (the_person.love > 50):
                "As your start getting dressed again, out of the corner of your eye you see [the_person.possessive_title] begin to shudder."
                "You see a tear roll down one of her eyes."
                the_person.char "Thank you [the_person.mc_title]... It means so much to me, everything you've done for me... and for the shop."
            else:
                "You get up and start getting dressed. [the_person.possessive_title] calls out to you."
                the_person.char "Thank you [the_person.mc_title], for all your help. I wouldn't have made it this far without you."
            mc.name "Thanks [the_person.title]. It has been a pleasure helping you out. Please let me know if you'd like... help... again in the future with your reviews!"
            $ the_person.change_love(5)
            $ the_person.change_happiness(10)
            $ the_person.change_slut_core(3)
            $ the_person.change_slut_temp(5)
            "You go back and take a look at the camera. You accidentally left it recording! It has a recording of you and [the_person.possessive_title] fucking!"
            "You decide you should probably just be honest and tell her."
            mc.name "So... I accidentally forgot to stop the camera... it caught the whole scene of us having sex."
            the_person.char "Oh! Let me see!"
            $ the_person.draw_person(position = "stand2")
            "[the_person.possessive_title] hops up and takes a look at the camera."
            the_person.char "Oh my... this is hot... I didn't think I would like this but... its kinda hot watching yourself on video get fucked..."
            "You raise an eyebrow. Is she starting to like showing off a bit?"
            if the_person.get_opinion_score("public sex") < 1:
                $ the_person.sexy_opinions["public sex"] = [1, True]
                "[the_person.possessive_title] now likes public sex!"
            $ the_person.reset_arousal()
            "You chat with her for a few minutes about the details of setting up a review site, but eventually its time to say goodbye."
            the_person.char "Thanks again for everything [the_person.mc_title]. Don't be a stranger now!"
        "Fuck Her \nRequires: Stamina (disabled)" if mc.current_stamina == 0:
            pass
        "Refuse":  #Lol really? I guess some people may not have the stamina.
            mc.name "Sorry, I've had a long day, and I should probably get to work on editing this video."
            "She seems surprised by your answer."
            the_person.char "Oh... right, I'm sure that's going to be a lot of hard work..."
            "You chat with her for a few minutes about the details of setting up a review site, but eventually its time to say goodbye."
            the_person.char "Thanks for the help [the_person.mc_title], if you find yourself needing anything later... just ask okay?"
            $ the_person.change_love(-5)
            $ the_person.change_happiness(-5)
            $ the_person.change_slut_core(5)
            $ the_person.change_slut_temp(5)

    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.
    $ mc.location.show_background()
    $ renpy.scene("Active")
    return #Masturbation, ends in sex

#SBS90
label starbuck_sex_store_promo_three_label(the_person): #Cunnilingus, ends in rough sex
    the_person.char "Oh, business is great! I'm definitely getting more women in here now."
    "[the_person.possessive_title]'s voice trails off for a second before she continues."
    the_person.char "The interest has been booming now for masturbation tools, but one thing I've noticed as I've had customers come in, as well as my sales..."
    the_person.char "A huge percentage of my sales are to singles. I get almost no couples in here shopping together."
    "You consider her problem for a bit, but it is actually her that comes up with an idea first."
    the_person.char "So, I was thinking, maybe for my next video review you could umm,  you know, help me demonstrate something?"
    "She looks at you hopefully. This is an easy decision."
    mc.name "Absolutely. It's only fair. You've already put yourself out there, I'm ready to do my part."
    "[the_person.possessive_title] gives you a bright, beaming smile."
    the_person.char "Yes! Okay! Give me minute I'll meet you in the back! Get the camera ready!"
    "You make your way to the back. You get the camera setup and ready to go."
    $ SB_advert_five_outfit = Outfit("Lingerie Just Red Panties")
    $ SB_advert_five_outfit.add_lower(panties.get_copy(), colour_red)
    $ the_person.draw_person(position = "stand4")
    "[the_person.possessive_title] enters the room."
    the_person.char "Ok, I figure we can get through a couple things... I have a pair of edible panties, and a nice set of fuzzy handcuffs..."
    "Wow... so at her suggestion, you are about to eat panties off of [the_person.possessive_title]... and then hand cuff her... all on camera."
    "[the_person.possessive_title] starts to strip down."
    $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
    "Once she finishes stripping, she grabs the panties and puts them on."
    $ the_person.outfit = SB_advert_five_outfit.get_copy()
    $ the_person.draw_person()
    $ the_person.wardrobe.add_underwear_set(SB_advert_five_outfit)
    $ del SB_advert_five_outfit
    "[the_person.possessive_title] stands before you almost completely exposed, her incredible body is on full display."
    if starbuck.love > 50:
        the_person.char "Do you think that before we get started, maybe you could just hold me for a little bit?"
        "You step up to her. Your hands go to her waist an she wraps her arms around you."
        $ the_person.draw_person(position = "kissing")
        the_person.char "Mmm... it feels so good when you hold me."
        "She looks up into your eyes. Your bring your face down to hers and begin to kiss. Her lips open submissively to allowed you tongue to invade her mouth."
        "You embrace each other for a while, just enjoying the heat and softness of her skin."
        the_person.char "Okay, are you ready to get this started?"
    else:
        the_person.char "You just gonna watch? Or are you ready to get started?"
    "You walk over and start up the camera. You give her a nod to show her that it's running."
    the_person.char "Hello! This is [the_person.name], from [the_person.name]'s Sex Shop! Here to review another couple of products."
    the_person.char "Today, we are going to review a couple of products meant for couples! So today I've asked a friend to be here to help me review them..."
    "You step into frame next to [the_person.possessive_title]"
    the_person.char "This is [the_person.mc_title], and we are going to review some edible underwear by Skinworks, and some neat fuzzy handcuffs by PowerTrips Inc..."
    "[the_person.possessive_title] gives some of the details on the products."
    the_person.char "Ok, I guess we're ready to get started! Are you ready [the_person.mc_title]?"
    "You nod. [the_person.possessive_title] lays down in the table and spreads her legs, angled in such a way that the camera can get a good view of her barely hidden pussy."
    $ the_person.draw_person(position = "missionary")
    "You get down on your knees between her legs. You kiss and lick up along her leg, working your way up to her pussy."
    "When you reach her mound, you stop and breath deeply in through your nose, savoring the musky scent of her sex."
    "[the_person.possessive_title] runs her hands through your hair, gently urging your face down into her edible panty clad cunt."
    "You push your face into her mound, and begin to nibble at the gummy panties that are between your tongue and [the_person.possessive_title]'s sweet cunt."
    $ the_person.change_arousal(10)#10
    the_person.char "Mmm, how do they taste, [the_person.mc_title]?"
    "You give her a loud MMMmmm of approval."
    "You are starting to make good size holes in the cherry flavored covering. One is close enough to her slit, you are able to snake your tongue through it and along her moist fuckhole."
    $ the_person.change_arousal(10)#20
    the_person.char "Oh! Mmm that felt good. These panties would be good if you had a significant other who... maybe doesn't usually like to go down on you..."
    "You chew the hole a little wider. You can now access her clit easily through the hole. You take the opportunity to roll her clit between your lips for a few seconds before resuming your panty eating."
    $ the_person.change_arousal(15)#35
    the_person.char "Oooohhhhh, he just go through to my clit... Mmmm that feels so good."
    "[the_person.possessive_title] reaches down and tears a piece of her panties off, now giving you almost free reign to eat her pussy."
    the_person.char "Okay, lets see how they taste..."
    "She takes a bite of the panties, chews and swallows. While she does that you push your tongue deep into her cunt."
    $ the_person.change_arousal(15)#50
    the_person.char "Yes! Mmm they actually taste pretty good, I can see why [the_person.mc_title] here is so eager..."
    $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
    $ the_person.draw_animated_removal(strip_choice)
    $ the_person.draw_person(position = "missionary")
    "Her panties now in shreds, [the_person.possessive_title] gathers what is left of them and pulls them off."
    $ the_person.change_arousal(20)#70
    "[the_person.possessive_title]'s juices are beginning to flow freely from her slit. You lap them up before circling your tongue around her clit a few times."
    "After licking at her clit, you move your tongue down to her entrance. You push your tongue up inside her as far as it will go."
    $ the_person.change_arousal(10)#80
    "[the_person.possessive_title] has stopped providing commentary and is now just moaning and encouraging you."
    the_person.char "Oh [the_person.mc_title]! That feels so good..."
    "She starts to rock her hips, grinding herself against your face."
    $ the_person.change_arousal(10)#90
    "[the_person.possessive_title] is bucking her hips wildly as you lick her. Suddenly, she grabs the back of your head and gasps."
    $ the_person.change_arousal(20)#110
    $ the_person.call_dialogue("climax_responses_oral")
    "Her pussy is drooling wet as she climaxes. She paws at the table, trying to find something to hold onto."
    "After a few seconds she lets out a long sigh and all the tension drains out of her body. You slow down a bit and lap up her sweet, creamy juices."
    the_person.char "Oh fuck [the_person.mc_title], your tongue feels so good. Wow!"
    "You slowly push yourself back from her pussy. [the_person.possessive_title]'s juices are dripping down your chin. You lick up as much as you can."
    the_person.char "Ok... wow... so, moving on... you know... to the handcuffs..."
    "You step over and grab the handcuffs. They having linings on them so they are nice and soft, but you can tell that underneath the cloth lining is strong steel. They feel very sturdy."
    the_person.char "That was great for when you want to get your pussy eaten... as my incredibly able assistant just showed, but these, they are good for when you want your man to take control."
    $ the_person.draw_person(position = "sitting")
    "You approach [the_person.possessive_title] with the handcuffs. She sits up and puts her hands behind her back. As you put the handcuffs on her hands, she whispers in your ear."
    the_person.char "[the_person.mc_title] that was amazing. I want you to be rough with me now. Don't worry, I can take it, and I want to show off how sturdy the cuffs are for the camera..."
    "You nod in acknowledgement. While the camera is running, you know that the real reason [the_person.possessive_title] has you here isn't for the video, but because she wants you to dominate her."
    "She could have chosen any other toy, and she could have chosen any other guy, but she chose you. You snap the second hand cuff in place."
    the_person.char "So, these handcuffs are soft enough they don't hurt or dig into the skin, but they are very sturdy. [the_person.mc_title] can do whatever he wants to me now, theres no way I'll be able to break free."
    "You take that as your cue. You grab her shoulders and turn her away from you, then push her down onto the table. Soon, she has her face down and her ass up."
    $ the_person.draw_person(position = "doggy")
    "Her pussy lips are wildly engorged, slick from the juices of her previous orgasm."
    "You rub your dick back and forth across her slit, getting it nice and slick. Then you grab her hips, and in one smooth motion you thrust yourself deep inside her."
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)
    "You thrust yourself deep into her steamy sex. Her moans begin immediately, her arousal still high from her previous orgasm."
    "You hold onto [the_person.possessive_title]'s hips and settle into a steady rhythm, pumping your cock in and out of her tight pussy."
    "You take a hand off of [the_person.possessive_title]'s hips and squeeze her ass cheeks with it. She moans happily in response you give her a hard slap."
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)#40
    "[the_person.possessive_title] struggles a bit against her handcuffs, but she is helpless to defend herself from your spanking."
    "[the_person.possessive_title]'s moaning intensifies rapidly, until finally she takes a sharp breath and tenses up."
    $ the_person.call_dialogue("climax_responses_vaginal")
    $ the_person.change_slut_temp(5)
    $ the_person.change_slut_core(2)
    $ the_person.change_happiness(4)
    "You keep up your pace while [the_person.possessive_title] cums. With each pulse of her pussy around your cock you spank her ass."
    the_person.char "Ah!"
    "You enjoy the way her tight ass jiggles and spank it again."
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)#60
    "You take your hands off of her hips and lean forward to put them on her shoulders. With her hands in cuffs she is powerless to resist when you pull her shoulder back towards you, forcing her to arch her back."
    "With the leverage of your hands on her shoulders, holding her body weight up off the table. Your hips make heavy slapping noises as the slam into her ass with each thrust."
    the_person.char "OHHH! Fuck me [the_person.mc_title]! HOLY FUCK!"
    "[the_person.possessive_title]'s entire body begins to tremble as another orgasm hits her. Her pussy spasms wildly all around you and you can see her hips quaking."
    $ the_person.call_dialogue("climax_responses_vaginal")
    $ the_person.change_slut_temp(5)
    $ the_person.change_slut_core(2)
    $ the_person.change_happiness(4)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)#80
    "[the_person.possessive_title]'s orgasm is milking your cock. It is rapidly pushing you past the point of no return."
    "You can't help but grunt with each thrust as you fuck her roughly. [the_person.possessive_title] is having trouble speaking intelligible words."
    the_person.char "[the_person.mc_title]! Oh cum for me baby... please cum! I want it so bad!"
    $ the_person.change_arousal(20)
    $ mc.change_arousal(25)#105
    "You can't take anymore. You let go of her shoulders and her upper body crashes roughly to the table. You grab her hips and plow deep into her pussy."
    $the_person.call_dialogue("sex_responses_vaginal")
    mc.name "Ah, I'm going to cum!"
    "You bottom out and explode deep inside of [the_person.possessive_title]. The heat of your semen painting her vaginal walls sends her into another orgasm."
    the_person.char "OH! I'M CUMMING AGAIN! YES [the_person.mc_title]!"
    $ the_person.change_slut_temp(5)
    $ the_person.change_slut_core(2)
    $ the_person.change_happiness(4)
    $ the_person.cum_in_vagina()
    $ the_person.draw_person(position = "doggy")
    "You are completely spent. [the_person.possessive_title] is a sweaty, handcuffed mess beneath you. She takes a few seconds to recover."
    the_person.char "So... as you can see... the handcuffs... fuck... they can hold up to... some pretty intense... amazing... mind-blowing... fucking..."
    "You move of the side to exit the frame. You can see in the camera your seed slowly dripping out of [the_person.possessive_title], when you press the stop button."
    mc.name "Wow, that amazing. I'd be surprised if we don't get at least a little bit of traffic from couples out of that!"
    "[the_person.possessive_title] turns her head to look at you. You laugh when you realize you forgot to un-cuff her."
    mc.name "Sorry, I forgot you still had those on."
    "You grab the key and undo the cuffs. She slowly sits up, but is hesitant to stand."
    $ the_person.draw_person(position = "sitting")
    the_person.char "[the_person.mc_title]... its been so long... since I've been fucked like that..."
    if the_person.love > 50:
        the_person.char "I've missed that, having someone take control of me and just fuck my brains out..."
        "While she is normally a very independent woman, you think maybe [the_person.possessive_title] is starting to get a bit of a submissive streak when you are around."
        if the_person.get_opinion_score("being submissive") < 1:
            $ the_person.sexy_opinions["being submissive"] = [1, True]
            "[the_person.possessive_title] now likes being submissive!"
    the_person.char "So... I'm just gonna throw this out there. I have at least 4 other sets of fuzzy cuffs... we could totally try them out anytime you want..."
    "[the_person.possessive_title] slowly stands up. She walks over toward you."
    $ the_person.reset_arousal()
    the_person.char "Except right now... I'm going to need some time to recover from that."
    $ the_person.draw_person(position = "kissing")
    "[the_person.possessive_title] wraps her arms around you. She kisses you twice on the neck, then whispers in your ear."
    the_person.char "I can feel you running down my leg... and I love it..."
    $ the_person.draw_person(position = "walking_away")
    the_person.char "I'm gonna go get cleaned up now... Get to work on that video!"
    $ the_person.shop_investment_rate = 4.0
    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.
    "You grab the camera, and start looking at the footage. The first thing you do is copy it on a thumb drive, for you to enjoy at a later date."
    "You head out to start work on the advertisement video."
    $ mc.location.show_background()
    $ renpy.scene("Active")
    return


#SBS100
label starbuck_sex_store_promo_four_label(the_person): #DP, ends in ???
    the_person.char "Oh, yeah! Its great to see couples coming in now..."
    "[the_person.possessive_title]'s voice trails off for a second before she continues."
    the_person.char "You know, I've been tracking the stock of stuff we have been selling though. It's all very... vanilla? I guess you could say."
    mc.name "I'm not sure I understand what you mean?"
    "[the_person.possessive_title] stutters as she tries to figure out the best way to explain what she means."
    the_person.char "I guess I just mean that, the sales we are getting, its for just generic sex items. Lingerie, condoms, handcuffs... but the more... shall we say, kinky items aren't really selling."
    mc.name "Like what kind of things aren't selling?"
    the_person.char "Well, some of the kinkier items... like whips, ropes, strap-ons... that kind of thing."
    "You consider some of the items she has in mind. The list she's said makes you a little nervous."
    mc.name "Well, I mean, I'm definitely willing to help you make another video showcasing an item or two... did you have anything specific in mind?"
    the_person.char "Well... I'm going to be honest here, you definitely seem like more of a dominant type... why don't we make a video where I play the submissive? See if we can get more business that way?"
    "Wow... she wants you to play the dom! You definitely like where this is going..."
    the_person.char "Tell you what... set up the camera and meet me in back in a few minutes... I've got a couple things in mind I wouldn't mind..."
    mc.name "Sounds great!"
    "You make your way to the back. You get the camera setup and ready to go."
    $ SB_advert_six_outfit = Outfit("Starbuck's Pink Lingerie")
    $ SB_advert_six_outfit.add_upper(corset.get_copy(),colour_pink)
    $ SB_advert_six_outfit.add_feet(garter_with_fishnets.get_copy(),colour_pink)
    $ SB_advert_six_outfit.add_feet(high_heels.get_copy(), colour_pink)
    $ SB_advert_six_outfit.add_accessory(wide_choker.get_copy(),colour_pink)
    $ SB_advert_six_outfit.add_accessory(lipstick.get_copy(), [1.0,0.44,0.43,0.7])

    "[the_person.possessive_title] enters the room. When you see what she is carrying you start to get excited."
    the_person.char "Ok, I figure we can start with the whip... I also have a bottle of premium anal lube, and a strap on for guys designed for double penetration..."
    "Wow... you wonder which hole you are gonna get to fuck while the strap on fucks the other..."
    "[the_person.possessive_title] starts to strip down in front of you."
    $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
    "Once she finishes stripping, she puts on some incredibly sexy pink lingerie."
    $ the_person.outfit = SB_advert_six_outfit.get_copy()
    $ the_person.draw_person()
    $ the_person.wardrobe.add_outfit(SB_advert_six_outfit)
    $ del SB_advert_six_outfit
    mc.name "[the_person.title]... thats... you look amazing."
    "[the_person.possessive_title] gives you a wide smile."
    the_person.char "Thank you! You know I can't give ALL my investors special views like this..."
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title] turns around and wiggles her hips a bit. She peeks back at you and teases."
    the_person.char "But you've done so much for me... I figure this is the least I can do for you!"
    $ the_person.draw_person(position = "stand4")
    the_person.char "Okay! Let's start with the whip, go ahead and get the camera rolling, and I'll do the introduction."
    "You step over to the camera. When [the_person.possessive_title] is in frame you hit the record button."
    the_person.char "Hello! This is [the_person.name], from [the_person.name]'s Sex Shop! Here to review another couple of products."
    the_person.char "Today, we are going to review a couple of products meant for those who are look to get things a little... kinkier in the bedroom..."
    "[the_person.possessive_title] talks about the whip she has in her hand. After explaining tips and tricks to proper usage, she cues you."
    the_person.char "And now, to demonstrate proper usage, I'm going to invite [the_person.mc_title] back to help me demonstrate it..."
    "You move in frame, and she hands you the whip."
    the_person.char "Okay! Now, it is important, anytime you get something like a whip involved, that you are very careful with where you strike the other person."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] bends over a chair nearby."
    the_person.char "While really, you could use it on any fatty part of the body, the obvious place to utilize a whip during sex play is on the ass..."
    "You are partially mesmerized by [the_person.possessive_title]'s ass when she bends over. In her pink lingerie, you can't wait to fuck her... you are startled when she prompts you."
    the_person.char "...[the_person.mc_title]? I said I'm ready now. Show the viewed how to use that thing!"
    "You move behind her, but at an angle so that the camera can still see what is going on."
    "For your first strike, you spank her modestly. You aren't sure how much pain tolerance she has."
    "SMACK"
    the_person.char "OH! As you can see, another important thing when you are using a tool like this is... start slow! As you can see, my partner here is starting easy..."
    "[the_person.possessive_title] wiggles her hips back and forth a couple times."
    the_person.char "Don't worry [the_person.mc_title], you can give it to me harder than that."
    "You swing the whip with a little more force this time."
    "SMACK"
    $ the_person.change_arousal(10)
    the_person.char "AHH! Mmmm, that's nice... Now remember, an important part of spicing up the bedroom is communication! Tell your partner how you like it!"
    "[the_person.possessive_title] wiggles her hips again."
    the_person.char "Okay [the_person.mc_title], that was about a 5 out of 10 for how hard you can spank... I want you give me a 7 this time..."
    "You'd never thought about rating how hard you swing the whip, but it makes total sense after [the_person.possessive_title] says that. It's pretty sexy the way she tells you the way she wants to get spanked..."
    "You put more force into the next one, but not too much."
    "SMACK"
    $ the_person.change_arousal(10)#20
    the_person.char "Fuck! Oh that was good... That was just about perfect... now try and..."
    "SMACK"
    "You catch her off guard as you give her other ass cheek a whipping."
    the_person.char "AHH! Oh that hurt so good... thats it baby, I've been a bad girl... spank me!"
    "SMACK"
    $ the_person.change_arousal(10)#30
    "You give her a couple more spanks with the whip."
    "SMACK"
    "You can see her ass cheeks beginning to turn red. She wiggles her hips as you spank her."
    "SMACK"
    $ the_person.change_arousal(15)#45
    the_person.char "YES! Oh [the_person.mc_title]... okay... I think the viewers get the idea now..."
    "SMACK"
    "You give her one last spank, just for good measure... You can see her pussy is starting to glisten with excitement."
    $ the_person.draw_person(position = "stand2")
    the_person.char "Okay... time to move on. The other thing we have to demonstrate today is... mmm that felt good..."
    "[the_person.possessive_title] takes a second to gather her thoughts."
    the_person.char "We are going to demonstrate proper usage of a special type of strap on. This strap on goes around a man and sits just below the penis..."
    "[the_person.possessive_title] explains the basics of the strap on in her hand. When she gets done talking about it, she gets down on her knees."
    $ the_person.draw_person(position = "blowjob", emotion = "happy")
    the_person.char "Okay, here is how we put it on..."
    "She grabs your dick and gives it a couple strokes. She puts the straps in place and secures the strap on to you. You now have a second, rubber cock, sitting just below your fleshy one."
    "[the_person.possessive_title] gazes intently at your meat. She licks her lips and then runs her tongue along the side of it a couple times before she stands up."
    $ mc.change_arousal(5)
    $ the_person.draw_person(position = "stand4")
    the_person.char "Now, before we get to the good part, it is important, anytime you are getting ready to put anything in your ass, that you get it good a lubed up..."
    "She grabs the bottle of premium anal lube and squirts some in her hand. She lists the pro's of buying the higher quality lubes."
    "[the_person.possessive_title] takes your cock in her hand and started to lube it up. She takes the bottle and squirts some more into her hand, getting you nice and slick."
    $ mc.change_arousal(5)#10
    "She squirts some more in her hand, and you see her reach back and start to lube up her backside."
    the_person.char "Okay, I think we are all set..."
    $ the_person.draw_person(position = "doggy")
    "[the_person.possessive_title] gets down on her hands and knees and sticks her ass up in the air. Her puckered hole glistens from the lube she put on it, and her lips are puffy with arousal."
    the_person.char "[the_person.mc_title]... I want you to go slow when you put your cock in my ass... I'll guide the strap on into my vagina..."
    "Her ass looks supple and firm. You are about to fuck [the_person.possessive_title]'s ass, while a dildo penetrates her pussy. You can't believe how lucky you are to able to do this with her."
    "You get down on your knees behind her. With one hand on her hip and the other on your cock, you line yourself up with tight back passage."
    "[the_person.possessive_title] reaches one hand between her legs and grabs the dildo. She lines it up with her other hole."
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    the_person.char "Oh my god! I'm so full... Its so good [the_person.mc_title]! This thing is amazing..."
    "With your hands on her hips, you slowly start to fuck her."
    call sex_description(the_person, SB_doggy_anal_dildo_dp, make_floor(), 1, private= True, girl_in_charge = False) from _call_sex_description_SBS100
    "[the_person.possessive_title] is in a sex induced daze after you finish. She struggles to make a coherent end to the video."
    the_person.char "So that's... when you use a strap on... holy fuck people just get one."
    "You get up and head over to the camera and stop the recording."
    mc.name "Well... that was incredible. [the_person.title] if that doesn't bring in customers, I don't know what would."
    if the_person.love > 60:
        the_person.char "[the_person.mc_title]... you are amazing. Look... I'm going to be honest here. I couldn't care less about bringing in more business... I just wanted you to fuck me with that thing."
        $ the_person.draw_person(position = "stand2")
        "[the_person.possessive_title] slowly stands up. Her feet are a bit wobbly."
        the_person.char "It has been amazing having you around [the_person.mc_title]. It just feels so right every time we have sex. It almost feels wrong... recording it just to bring in more business..."
        "You decide to interrupt her."
        mc.name "[the_person.possessive_title]. It has been great being your business partner. I know what you are saying, but don't worry. I'd be doing this with you even if we weren't recording it."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        "She smiles at you happily"
        mc.name "But don't worry. If it helps the business grow, theres no reason not to record it. It doesn't make the sex any less meaningful to me. I mean really, you could ask any guy in here to do this stuff..."
        the_person.char "I can't imagine it though... doing this whole venture with anyone else as my partner. Thank you, [the_person.mc_title]."
    else:
        the_person.char "Thanks [the_person.mc_title]. That was amazing... UGH I can barely get up."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        "[the_person.possessive_title] slowly stands up. Her feet are a bit wobbly."
    "[the_person.possessive_title] rubs her ass a bit where you spanked her earlier."
    the_person.char "I remember when... my husband use to use me like that... bending me over, spanking me like the naughty girl that a I am."
    the_person.char "We should do this again. It felt so good when your cock started pushing into my ass..."
    if the_person.get_opinion_score("being submissive") < 2:
        $ the_person.sexy_opinions["being submissive"] = [2, True]
        "[the_person.possessive_title] now loves being submissive!"
    if the_person.get_opinion_score("anal sex") < 1:
        $ the_person.sexy_opinions["anal sex"] = [1, True]
        "[the_person.possessive_title] now likes being anal sex!"
    "You grab the camera, and start looking at the footage."
    mc.name "Okay, you take it easy for a bit, I'm gonna go work on that advertisement video!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] starts to walk away. She is walking a little funny."
    $ the_person.shop_investment_rate = 5.0
    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False)
    "You head out to start work on the advertisement video."

    return

#SBS110
label starbuck_sex_store_promo_five_label(the_person): #Swingset anal, ends in ???
    the_person.char "Oh, yeah! Business is great! It has been amazing having all different types of people coming in here to try out all kinda of new things."
    "[the_person.possessive_title] gives you a big smile."
    the_person.char "I tell you what. I have a product I've been wanting to try out ever since we expanded and got it in..."
    "You like where this conversation is going!"
    the_person.char "If you are willing to try it out with me... I'd be willing to give you an extra that you can take home with you!"
    mc.name "Are we going to do another video of it? For advertising purposes?"
    the_person.char "Of course! I mean, as long as you are okay with it... honestly... I want to try it out either way, but if we're gonna try a new product, might as well take a video anyway, right?"
    "You nod in agreement."
    mc.name "Okay, I'm in. What exactly are we going to test out?"
    the_person.char "Well... I got in a special.. ermm... swing set... with straps that I can get up in, so you can fuck me in while I'm suspended up in the air..."
    mc.name "Wow... do you need help setting it up?"
    the_person.char "Yes, actually. That would be really helpful!"
    "You and [the_person.possessive_title] head to the back room. To the side of the room you can see a box that has the swing in it."
    "You pull it out and start going through the directions. It seems pretty straightforward to set up!"
    $ the_person.draw_person(position = "back_peek")
    "While working on the set up, you look over and see [the_person.possessive_title] working on something with her back to you. You walk up behind her."
    "You run your hands along her hips, admiring their shape and form."
    if the_person.love > 70:
        the_person.char "Mmm... I love it when you run your hands all over me [the_person.mc_title]."
        "You work your hands along her belly and then slowly up to her wonderful tits."
        if the_person.outfit.tits_available():
            "They are so soft and warm in your hands. You give them a good squeeze and then punch lightly at her nipples."
        else:
            "They feel so soft, even through her clothes. You give them a good squeeze, and you can feel her nipples start to poke through the fabric."
        "[the_person.possessive_title] pushes her ass back against you. She starts to grind her hips against your hardening erection."
        $ the_person.change_arousal(20)
        the_person.char "[the_person.mc_title] it is so nice having you close... lets get done with this swing. I want you!"
    else:
        the_person.char "That feels good... Lets focus on the swing though. I need a good fucking!"
    "You get back to work. It isn't long until the whole thing is finished. You stand with [the_person.possessive_title] and admire your handiwork."
    $ the_person.draw_person(position = "stand3")
    the_person.char "Alright. Before we get started, let me get ready. You should probably get naked too!"
    "You start to strip down, but watch intently while [the_person.possessive_title] strips down along side you."
    $ the_person.strip_outfit(position = "stand3")
    "Now that she is naked, [the_person.possessive_title] grabs some of her anal lube of a shelf. You raise an eyebrow as she squirts some onto her hand."
    mc.name "Anal lube? Wow... going all out are we?"
    "[the_person.possessive_title] chuckles as she reaches back and starts to spread the lube around her backside."
    the_person.char "Of course! I mean, it feels so good when you push it into me back there..."
    the_person.char "Besides, I'm sure that the viewers would probably like it better anyway!"
    "[the_person.possessive_title] walks over to you and starts lubing up your cock. It feels great when she gives you a couple of strokes."
    the_person.char "Okay! I'm ready to do this! Go ahead and start up the camera, this is gonna be great!"
    "You step behind the camera. You make sure everything is in frame, then hit record. You give [the_person.possessive_title] a thumbs up."
    the_person.char "Hello! This is [the_person.name], from [the_person.name]'s Sex Shop! Here to review a new product we've just gotten in to the store!"
    the_person.char "Today, I am going to be reviewing the FEMco Sex Swing 3000..."
    "[the_person.possessive_title] starts talking about the swing set. As she talks, she is using hand gestures to illustrate some of the set up methods."
    "Every time she moves her hands back and forth, her amazing tits quiver a bit."
    "After she is done introducing the swing, she sits down in it."
    $ the_person.draw_person(position = "sitting")
    the_person.char "And now to help me demonstrate one of the ways you could use it, the always amazing [the_person.mc_title]!"
    "You step into frame and start to walk up behind her."
    the_person.char "Today, he is going to show us how it could be used for a relaxed sodomy session. I'll be able to relax here in the swing, while my ass is at just the right height for him to fuck it..."
    "As you get close behind her, you put your hands on her hips. She reaches back and grasps your cock, and begins to guide it toward her bottom."
    "When you cock begins poking up against her puckered hole, you can feel a bit of resistance. With your hands firmly on her hips, you pull her ass towards you."
    "[the_person.possessive_title] forces herself to relax her sphincter, and you penetrate her with wonderful pop. With more gentle pressure you are soon deep inside her bowel."
    the_person.char "Mmm... as you can see... I'm able to completely relax with my ass off the back of the swing, so I can just sit and enjoy the sensations."
    "You give her a modest thrust. The swing bounces forward for a second, but gravity soon causes her ass to pendulum back and smack against your hip."
    "The feeling is exquisite. You grab her hips and get ready to fuck [the_person.possessive_title]'s brains out."
    #Call sex scene#
    call sex_description(the_person, SB_anal_swing, SB_make_swing(), 1, private= True, girl_in_charge = False) from _call_sex_description_SBS110

    "Turning off the video camera, you turn to [the_person.possessive_title]."
    $ the_person.shop_investment_rate = 6.0
    mc.name "Wow, that was good. You are so sexy."
    the_person.char "Aww, thanks [the_person.mc_title]. Now, I promised that if you helped me make the video, I'd give you a swing for you to have."
    mc.name "Thanks, but you don't need to do that."
    the_person.char "No no, its okay, I want you to have one... I was thinking... you helped me set up this one, why don't you let me come over and I'll help you set up one?"
    "Hmm, she is offering to come over to your place!"
    mc.name "Well, it would be rude to say no."
    "[the_person.possessive_title] gives you a big hug."
    the_person.char "Great! Let's get it done. It won't take us long!"
    $ the_person.outfit = (the_person.wardrobe.decide_on_outfit(40)).get_copy()

    #TODO move the scene to the player's bedroom. and get dressed
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    $ the_person.draw_person(position = "stand4")
    "You and [the_person.possessive_title] head back to your place. Having already put one together, you and her quick have it all set up."

    the_person.char "Great! Now you have one of your own... you know... for when you have girls over..."
    "She gets a little shy."
    the_person.char "I think that I'm going to leave up the one I have in the back room at the shop, in case you ever want to try it out again..."
    if the_person.love > 70:
        "She looks at you. Her face is a little forlorn, clearly remembering something from her past."
        the_person.char "[the_person.mc_title], getting this shop up and running... and everything you've done for me. You really don't have any idea how much it all means to me. Thank you so much!"
        $the_person.draw_person(position = "kissing")
        "She wraps her arms around you and hugs you close."
        the_person.char "Look... I don't know any other way of saying this, so I'm just gonna say it. I'm falling for you, [the_person.mc_title]. And I know you have a busy job and theres other girls and I'm not saying..."
        "She stutters for a minute."
        the_person.char "I understand that you aren't looking to be tied down to one girl, and I just want you to know that I understand that. I just want to know if you, maybe have feelings for me too..."
        menu:
            "It's mutual.":
                mc.name "Don't worry, [the_person.title]. The feeling is mutual. I love spending time with you."
                $ the_person.draw_person(position = "stand2", emotion = "happy")
                the_person.char "Oh! That is such a relief to hear."
                "You see her digging around in her pocket."
                the_person.char "Here... I want you to have this. It's a key to my apartment. You don't have to come over if you don't want to, but I just want you to know, you're always welcome in my bed."
                mc.name "Thanks [the_person.title]. It will be nice to be able to share a warm bed with a beautiful woman like you once in a while."
                $the_person.draw_person(position = "kissing")
                "She hugs you again and begins kissing you on your neck."
                the_person.char "You make me feel so good, [the_person.mc_title]... come visit me soon okay?"
                $ the_person.shop_owner_relationship_stage = 1.0
            #TODO its not mutual
    $the_person.draw_person(position = "stand2")
    the_person.char "Okay, its time for me to get to the shop. See you soon [the_person.mc_title]!"
    "You walk her to the door and say goodbye. Wow, you are now the proud owner of a sex swing! And with everything going on with [the_person.possessive_title], you brain is swimming a bit."
    $ sex_store.add_object(SB_make_swing())
    $ bedroom.add_object(SB_make_swing())
    return

#SBS120
label starbuck_spend_the_night_label(the_person): #You spend the night at her place. You'll probably get busy
    $ morning_fun_chance = 0
    mc.name "I was thinking I could spend the night here tonight."
    "[the_person.title] looks delighted."
    the_person.char "Oh! That would be great! I'd love the company!"
    $ the_roll = renpy.random.randint(0,100) #Roll for the possible event#
    if the_roll < 10 or mc.current_stamina < 1: #No event, just cuddle up and go to bed.
        mc.name "Thanks. Its been a long day and I'm exhausted."
        "You strip off your work clothes, down to your boxers. You head to [the_person.title]'s bedroom and hop in her bed."
        the_person.char "I'll be in in a minute!"
        "You see [the_person.title] step into the bathroom. In a few minutes she emerges, ready for bed."
        $ the_person.outfit = the_person.wardrobe.get_random_appropriate_underwear(the_person.sluttiness, 10, WardrobePreference(the_person))
        $ the_person.draw_person()
        "She crawls into bed beside you. You cuddle up behind her and enjoy the warmth of her body as you drift off to a restful night's sleep."
        $ morning_fun_chance = 100 #No action tonight? she wakes up hungry
    elif the_roll < 40: #She seduces you
        mc.name "Thanks. I just have a little bit of work stuff to finish up. I brought my laptop, mind if I take over your desk for a few?"
        the_person.char "Help yourself! I'll tell you what, I'm going to hop in the shower."
        "You sit down at the desk and pull out your laptop. You review some of the days research notes and begin emailing instructions for tomorrow."
        "You make note of a couple issues serum production, so write yourself a reminder to talk with an employee tomorrow about it..."
        "You delve into your work emails for a while longer, totally forgetting you are at [the_person.title]'s house. You are vaguely aware when you feel her coming up behind you."
        "Your mind is brought immediately back to the present when you feel the heavenly sensation of [the_person.title]'s warm, soft tit flesh on the back of your neck as she wraps her arms around you from behind."
        mc.name "Mmm, that feels great..."
        "She runs her hands up and down your chest, slowly unbuttoning your shirt. You lean your head back, your neck nestled between her amazing tits."
        "[the_person.title] begins to move her chest up and down slightly, rubbing her breasts along your neck and shoulders."
        the_person.char "Are you about at a stopping point?"
        mc.name "Yes, definitely."
        "You close your eyes and enjoy the sensations. [the_person.title]'s hands move lower down your belly and begins to stroke you through your pants."
        "She expertly begins to unbuckle your belt, and undoes your pants. You sigh when she puts one hand down your underwear and begins to jack you off slowly. She whispers into your ear."
        the_person.char "Come on... lets go to bed."
        $ SB_nude_outfit = Outfit("Nude")
        $ the_person.outfit = SB_nude_outfit.get_copy()
        $ the_person.draw_person(position = "back_peek")
        "She backs away from you and walks into her bedroom. You turn and watch her, seeing she is completely naked."
        "You quickly follow her."
        $ the_person.draw_person(position = "stand4")
        "[the_person.title] stops when she gets to the bed and turns to you."
        the_person.char "Lay down... theres something I want to do..."
        $ the_person.draw_person(position = "standing_doggy")
        "You nod. You take off what is left of your clothes and lay down. You watch [the_person.title] rummage through her nightstand. Her ass wiggles back and forth, right in front of you."
        "*SMACK*"
        "You reach up and give her ass a firm spank. She gives a sigh."
        the_person.char "Ah! Here it is..."
        $ the_person.draw_person(position = "stand4")
        "She stands up and you see that she is holding a bottle of anal lubricant. You feel your dick twitch when you realize what she has in mind."
        "She squirts some of it out onto your cock and works her hand up and down you a few times. Then she squirts a bit more into her hand and then reaches back to her ass."
        "[the_person.title] gives another gasp as you imagine she works a bit of the lube into her tight hole."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.possessive_title] climbs up on top of you. She takes you in her hand and points it towards her back passage."
        the_person.char "Oh god, [the_person.mc_title], its so big! Okay, here we go..."
        "[the_person.possessive_title] goes slow, but steadily slides down, impaling her sphincter on your throbbing erection. She bottoms out and moans loudly."
        #Fuck her#
        call sex_description(the_person, SB_anal_cowgirl, make_bed(), 1, private= True, girl_in_charge = True) from _call_sex_description_SBS120
        if the_person.arousal > 100:
            the_person.char "Oh god, I came so hard..."
            "[the_person.possessive_title] collapses onto the bed next to you, exhausted from her anal cowgirl ride."
        else:
            the_person.char "Mmm, that was so good, thank you [the_person.mc_title]..."
            "[the_person.possessive_title] rolls off you and lays down on the bed next to you."
        $ the_person.reset_arousal()
        "[the_person.title] doesn't bother to get up, she just cuddles up next to you."
        the_person.char "Thanks [the_person.mc_title], I needed that so bad."
        "She stretches her arms out and yawns."
        the_person.char "I'm wore out! Goodnight!"
        "[the_person.title] nuzzles up against you and slowly drifts off to sleep. In your sex induced haze, you quickly drift off to sleep with her."
        $ morning_fun_chance = 20 #She got what she wanted
    elif the_roll < 70 or mc.current_stamina < 3: #You seduce her
        $ the_person.draw_person(position = "kissing")
        "[the_person.possessive_title] wraps her arms around you to give you a hug. You use the opportunity."
        "You grab her ass and pick her up easily. She yelps for a second but quickly wraps her legs around you in an embrace."
        "Your lips meet and you begin to kiss her hungrily. She returns your kiss. You pull her tight against you and begin to grind your needy cock up against her."
        $ the_person.change_arousal(5)
        "She breaks the kiss for a second."
        the_person.char "Oh [the_person.mc_title], I missed you too."
        "[the_person.possessive_title] clings to you and begins to kiss your neck eagerly. You carefully carry her towards her bedroom."
        "When you get to her bed, you roughly throw her down on it."
        $ the_person.draw_person(position = "missionary")
        if the_person.outfit.vagina_available() and the_person.outfit.tits_available():
            "You stop for a second and admire [the_person.title], her body on display in front of you. You guess she walks around the house like this?"
        else:
            "Your mind hazy with lust, you begin to pull [the_person.title]'s clothes off."
            $ the_person.strip_outfit(position = "missionary")
            "Now naked, you stop for a second and admire [the_person.title]'s incredible body."
        "Before you go any further, you decide to make sure that [the_person.title] is wet and ready for you. You pull her over so her legs are hanging off the edge of the bed and get down on your knees in front of her."
        "She spread's her legs instinctively as you begin to kiss along her knee. You trail wet kisses along the inside of her thigh, working your way further up."
        "When you reach her cunt, you waste no time, pushing your tongue between her lips and running it up and down her delicious slit."
        "[the_person.title] moans and begins to run her hands through your hair. When you push your tongue up inside her he gently urges you deeper."
        $ the_person.change_arousal(10)
        "You reach forward with your hands and grasp her tits. You roll her nipples in your fingers for a second causing her moans to grow louder."
        "You lick circles around her clit, then close your mouth over and gently suck on it."
        $ the_person.change_arousal(10)
        the_person.char "Oh! Baby I'm ready, come fuck me!"
        call fuck_person(the_person) from _call_fuck_person_SBS121
        if the_person.arousal > 100:
            the_person.char "Oh god, I came so hard..."
            $ morning_fun_chance = 50 #She finished
        else:
            the_person.char "Mmm, that was so good, thank you [the_person.mc_title]..."
            $ morning_fun_chance = 100 #She didn't finish, so she comes for you in the morning.
        $ the_person.reset_arousal()
        "You lay down on the bed, hopping in the covers."
        "[the_person.title] doesn't bother to get up, she just cuddles up next to you."
        the_person.char "Thanks [the_person.mc_title], I didn't know I needed that until you got here."
        "She stretches her arms out and yawns."
        the_person.char "You wore me out! Goodnight!"
        "[the_person.title] nuzzles up against you and slowly drifts off to sleep. In your sex induced haze, you quickly drift off to sleep with her."

    else: # You both want it, and MC has stamina for a wild ride
        "She gives you a flirty smile."
        the_person.char "I'm kinda sweaty from a long day at the shop, so I was just getting ready to hop in the shower. Why don't you get comfortable? I won't be long."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] turns and walks into her bathroom. She closes the door... mostly... leaving it open a crack. You're sure she left it open on purpose, but you decide for now to let her get started solo."
        $ renpy.scene("Active")
        "You head into her kitchen and notice her coffee pot is on and full. Was she expecting you? You pour yourself a cup and take a few sips."
        "You sit down and enjoy your coffee. It has been about 5 minutes now. The crack in the door is calling you. Should you join her in the shower? Or let her finish?"
        menu:
            "Shower with her.":
                $ SB_nude_outfit = Outfit("Nude")
                $ the_person.outfit = SB_nude_outfit.get_copy()
                #TODO shower background?
                "You decide you've waited long enough and make your way into the bathroom. Inside you smell the scent of lavender body wash and quickly spy [the_person.title]'s soapy body through the hazy steam."
                $ the_person.draw_person(position = "back_peek")
                mc.name "Have room for me in there?"
                the_person.char "Of course! I was hoping you would join me..."
                "You strip down and enter the shower. [the_person.name] gives you a turn under the hot running water."
                the_person.char "Great timing... can you wash my back?"
                "She hands you her loofah and you begin to work circles up and down her back. The soap bubbles make her already smooth skin slick and soft."
                "When her back is all soapy, you reach over her shoulder and hand the loofah back to her. You put your other hand against her hip and slowly pull her back against you."
                "You now wrap your arms around her from behind, and she melts back into you. Your hands roam her body but quickly begin to grope her generous bosom, while she wiggles her ass back against you."
                the_person.char "Mmm, I'm glad we're thinking the same thing. I'm really hungry for you tonight, [the_person.mc_title]!"
                "You whisper into her ear."
                mc.name "Is that so? I don't believe you... Why don't you show me."
                if the_person.obedience > 110:  #She gets on her knees#
                    "[the_person.title] chuckles."
                    the_person.char "Mmm, for you, [the_person.mc_title]? I'll do just about anything..."
                    $ the_person.draw_person(position = "blowjob")
                    "[the_person.possessive_title] turns to you and gets down on her knees. She looks up at you. Her eyes certainly look a bit hungry..."
                    "She puts her hands on her breasts. She leans forward and nestles your cock between her bountiful tits."
                    call fuck_person(the_person, start_position = SB_Titfuck_Kneeling, start_object = make_floor(), skip_intro = True, girl_in_charge = True) from _call_fuck_person_SBS122
                    "You spend a moment recovering while [the_person.title] rinses your cum off her body."


                else:                           #She gets Feisty
                    "[the_person.title] chuckles and pushes her ass back against you."
                    the_person.char "Mmm, I have a better idea..."
                    "[the_person.possessive_title] leans forward a bit, against the shower wall. She reaches back and grabs your hardness, pointing it down towards her slit."
                    the_person.char "Why don't you just push it in... I'm ready for it, I promise..."
                    "You decide to go for it. She has you lined up, so you slowly push yourself forward inside of her."
                    the_person.char "Oh my god..."
                    "[the_person.possessive_title] sighs as you bottom out."
                    "She wiggles her ass back and forth a few times, enjoying the familiar feel of fullness you give her when you fuck her."
                    call sex_description(the_person, SB_doggy_standing, make_wall(), 1, private= True, girl_in_charge = False) from _call_sex_description_SBS123
                    "You spend a moment recovering while [the_person.title] rinses herself off."
                #TODO set outfit to regular nude again. She washed the cum off!
                $ SB_nude_outfit = Outfit("Nude")
                $ the_person.outfit = SB_nude_outfit.get_copy()
                $ the_person.arousal = 50   #A hard setting of arousal... Did this to avoid an entry in the log. Not ideal code#
                $ the_person.draw_person(position = "stand2")
                "You both quickly finish showering. As you hop out, you quickly dry off and [the_person.title] takes your hand."
                the_person.char "Lets go to bed! I'm so charged tonight, I think I can go all night!"
                mc.name "Sounds good. I'm gonna fuck your brains out tonight."
                $ the_person.draw_person(position = "walking_away")
            #"Wait for her.":  #TODO
        "You follow [the_person.title] to her bedroom."
        "Her amazing ass sways back and forth as she walks. Your cock twitches thinking about the night ahead of you."
        "She gets to her bed and immediately opens her nightstand and begins looking for something."
        "She pulls out the strap on dildo you helped her demonstrate for her advertisement and some anal lube and turns to you."
        $ the_person.draw_person(position = "stand4")
        the_person.char "How about we give this another run? Last time we used it, the results were very good..."
        menu:
            "Agree":
                mc.name "Lets do it. I love fucking your tight little ass."
                $ the_person.draw_person(position = "blowjob")
                "[the_person.possessive_title] gets down on her knees in front of you and starts securing the strap on."
                mc.name "Hey... while you're down there..."
                "[the_person.possessive_title] looks up at you and smiles. She sticks out her tongue and slithers it along your aching shaft, teasing you."
                the_person.char "Mmm... you taste so good. But I have other plans for this."
                "She squirts some lube into her hand and then gives you a couple strokes."
                the_person.char "Okay, you're ready, now its my turn!"
                $ the_person.draw_person(position = "doggy")
                "[the_person.title] stands up and hands you the lube, then crawls up on the bed on all fours, presenting her ass to you. She gives her hips a little shake."
                the_person.char "Lube me up, [the_person.mc_title]. Don't be stingy!"
                "You squirt a generous amount of lube onto your fingers. You run your fingers along her ass crack, coating it in a glaze of lube."
                "You take a finger and begin to push it up against her sphincter. You can feel her physically force herself to relax and then your finger eases right in."
                the_person.char "Mmm... that feels good already. I think I'm getting better at this!"
                "You apply some more lube, then slowly push two fingers into her smooth back passage. You feel like she is ready for you."
                "You get into position behind her. She arches her back and presents her ass."
                "[the_person.possessive_title]'s pussy is already dripping with arousal. You line yourself up with her ass, while she reaches down and lines the dildo up with her pussy."
                "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
                the_person.char "Oh my god! I'm so full... Its so good [the_person.mc_title]! Fuck me like you paid for this! Like I'm just a whore!"
                call sex_description(the_person, SB_doggy_anal_dildo_dp, make_bed(), 1, private= True, girl_in_charge = False) from _call_sex_description_SBS124
                "Finished with your anal plundering, you let yourself collapse onto [the_person.title]'s bed."
                "She cuddles up next to you."
                $ the_person.draw_person(position = "missionary", emotion = "happy")

            "Fuck her your way":
                mc.name "Not tonight. I have something different in mind."
                "[the_person.title] looks a little disappointed, but waits to see what you DO have in mind."
                call fuck_person(the_person) from _call_fuck_person_SBS125
                "Finished for the night, you let yourself collapse onto [the_person.title]'s bed."
                "She cuddles up next to you."
                $ the_person.draw_person(position = "missionary", emotion = "happy")

        $ morning_fun_chance = 50 #She finished. Maybe she wants an encore in the morning, maybe not.
        "[the_person.title] nuzzles up against you and slowly drifts off to sleep. In your sex induced haze, you quickly drift off to sleep with her."

    $ the_person.reset_arousal()
    call SB_process_overnight_no_events() from _SB_process_overnight_no_events_SBS129
    #Good morning!
    $ renpy.scene("Active")
    $ the_roll = renpy.random.randint(0,100)
    if the_roll < morning_fun_chance:        #Roll for morning sex is successful
        "[the_person.title]'s naked body against yours makes for a very pleasant night of sleep. A couple times throughout the night you stirred for a bit and gave her a grope, but quickly fell back asleep."
        "Pleasant sensations and the feeling of weight around your torso slowly wakes you up."
        $ the_person.change_arousal(30)
        $ the_person.draw_person(position = "cowgirl")
        "When you awaken, you discover that [the_person.title] is on top of you, with your morning wood already hilted inside her pussy."
        "You moan in appreciation at the wonderful wake up call."
        the_person.char "Mmm... Good morning [the_person.mc_title]... When I woke up this morning you were poking me pretty good... I figured you wouldn't mind if I took it for a quick ride."
        "You murmur your acceptance. Her mesmerizing tits are bouncing up and down right in front of you. You take them both in your palms and give them a good squeeze."
        call sex_description(the_person, cowgirl , make_bed(), 1, private = True, girl_in_charge = True) from _call_sex_description_SBS125
        the_person.char "Mmmff. So good... I wish I could call in sick and we could fuck all day... but I need to get to the shop."
        $ the_person.reset_arousal()
        $ the_person.draw_person(position = "stand3")
        the_person.char "I'm gonna go hop in the shower. Feel free to let yourself out! Thanks for spending the night [the_person.mc_title]!"
        "[the_person.title] slowly gets up and heads to the bathroom. You grab your stuff and head out."
    else:                                    #No morning sex
        "You wake up in the next morning after sleeping soundly the night before. As your stir it wakes up your bedwarmer, [the_person.title]. She yawns and stretches."
        "Slowy, [the_person.title] yawns and sits up at the side of the bed."
        $ the_person.draw_person(position = "sitting")
        the_person.char "Good morning, sleepyhead! Wow, I slept so good last night... you really wore me out!"
        "You chat for a few minutes, enjoying the warmth of her bed, until she gets up."
        $ the_person.draw_person(position = "stand3")
        the_person.char "I'm gonna go hop in the shower. Feel free to let yourself out! Thanks for spending the night [the_person.mc_title]!"
        "[the_person.title]heads to the bathroom. You grab your stuff and head out."
    $ the_person.reset_arousal()
    $ the_person.outfit = (the_person.wardrobe.decide_on_outfit(40)).get_copy()
    $ mc.location.show_background()
    $ renpy.scene("Active")
    return

label starbuck_intro():
    $ the_person = starbuck

    $ the_person.draw_person(emotion = "happy")
    if not SB_STARBUCK_INTRO_COMPLETE:
        "You enter the sex shop. A beautiful woman comes up to you and begins to introduce herself."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        $ SB_STARBUCK_INTRO_COMPLETE = True
        the_person.char "Hello there sir! Welcome to Starbuck's Sex Shop!"

        # uses parts of the in-game introduction sequence tailored to SB
        if the_person.title is None:
            mc.name "Hello."
            $ title_choice = get_random_title(the_person)
            $ formatted_title = the_person.create_formatted_title(title_choice)
            the_person.char "Let me introduce myself, i am [formatted_title]."
            $ the_person.set_title(title_choice)
            $ the_person.set_possessive_title(get_random_possessive_title(the_person))
            "She holds her hand out to shake yours."
            the_person.char "And how may I address you?"
            $ title_tuple = []
            $ title_choice = None
            python:
                for title in get_player_titles(the_person):
                    title_tuple.append([title,title])

            $ title_choice = renpy.display_menu(title_tuple,True,"Choice")
            mc.name "[title_choice], nice to meet you."
            $ the_person.set_mc_title(title_choice)

        the_person.char "We've just opened, so stock is still fairly limited, but feel free to browse and I'm here to answer any questions you might have!"
        "You smile at [the_person.possessive_title] and promise to take a look."
        the_person.char "Sounds great!"
        $ renpy.scene("Active")
        "After [the_person.possessive_title] goes back to the counter, you walk around the shop a bit. Unfortunately, things are pretty bare. There are several shelves with just labels on them."
        "You walk by one labeled as anal toys, but there aren't any on the shelf available for purchase."
        "You walk over to the counter."
        $ the_person.draw_person(position = "stand3", emotion = "happy")
        mc.name "This is pretty interesting, to open a sex shop like this, but the shelves seem pretty empty? Are you going to get more stock soon?"
        $ the_person.draw_person(position = "stand3", emotion = "sad")
        the_person.char "Yes, I'm sorry they are fairly empty, I didn't have much money to invest in the store. I'm hoping I'll be able to attract some customers, and reinvest the money back into the shop..."
        "You can see she is struggling a bit to open up."
        the_person.char "You see, it was always my husband and I's dream to open a shop like this, to help people be more adventurous and have fun in the bedroom..."
        the_person.char "When he died... it was hard. It has been a struggle to make ends meet, but I feel like I'm finally ready to move on with my life, and decided to chase my dreams!"
        "You glance around the shop for a bit. You can tell she is very... optimistic."
        mc.name "That's great that you are moving on... but surely you should get a bit more stock? Have you tried finding any investors?"
        "[the_person.possessive_title] mumbles for a second before answering."
        the_person.char "Well, you would be surprised how hard it is to find investors for a sex shop..."
        "You can tell that she is a hard worker, and is dedicated to making her shop work. Maybe you should consider investing in her shop?"
        mc.name "How much money would you need, say if someone were interested in investing in your shop, to get some basic stock on the shelves?"
        "[the_person.possessive_title] considers for a moment."
        the_person.char "Well, I really want the stock to be good, quality product. I'd say I could probably get everything setup for a basic shop for... say $1000?"
        "That seems pretty reasonable. You decide to consider investing. You should talk to [the_person.title] again if you decide to invest in the shop!"
    elif (the_person.shop_progress_stage) == 0:
        the_person.char "Hello there sir! Welcome back to Starbuck's Sex Shop! Feel free to look around."
        "You smile at [the_person.possessive_title] and promise to take a look."
        the_person.char "Sounds great, [the_person.mc_title]! I'll be here if you have any questions!"
    elif (the_person.shop_progress_stage) == 1:
        the_person.char "Hey there, [the_person.mc_title]! Its good to see you!"
        if the_person.sluttiness > 60:
            "[the_person.possessive_title] smiles playfully."
            the_person.char "I was just thinking about you. Anything I can help you with?"
        else:
            the_person.char "Is there anything I can help you with?"
    elif (the_person.shop_progress_stage) == 2:
        the_person.char "[the_person.mc_title]! I'm so glad to see you! This place is starting to do really well, thanks to you!"
        if the_person.sluttiness > 60:
            "[the_person.possessive_title] smiles playfully."
            the_person.char "I don't think I could ever repay you, is there anything I can help you with?"
        else:
            the_person.char "Is there anything I can help you with?"
    elif (the_person.shop_progress_stage) == 3:
        the_person.char "[the_person.mc_title]! Thanks for checking in! Thing are going amazing here, all thanks to you and your generous investments!"
        if the_person.sluttiness > 60:
            "[the_person.possessive_title] smiles playfully."
            the_person.char "I'll be forever in your debt. Is there anything I can help you with?"
        else:
            the_person.char "Is there anything I can help you with?"
    $ renpy.scene("Active")
    return
####Starbuck Unique Personality####

label starbuck_anal_fetish_masturbate(alert = False):
    $ the_person = starbuck

    if alert == True:
        "You feel your phone vibrate with a notification."
        "You pull it out and take a look. Looks like [the_person.title] is masturbating with her plug!"
    else:
        "You decide to check up on [the_person.title]. You pull out your phone and check up on her."
        "You are mildly surprised to see that she is masturbating with her plug!"
    "Do you want to have some fun with the plug?"
    menu:
        "Leave her to her fun":
            #TODO this section
            return
        "Vibrate the plug":
            "You decide to have a little fun with the plug vibration. You push and the hold the vibration function for a solid three seconds."
            "The app registers a heart rate spike with the vibration. [the_person.possessive_title] knows you are watching the monitor as she masturbates!"
    #WE can assume we decided to vibrate the plug
    "You imagine [the_person.title], somewhere in her shop, pushing th plug in and out of herself."
    "You push and hold the vibrate button again, release it, then pulse again. You make it pulse with vibration every second or two."
    "You watch as her heart rate slowly climbs. It's 100 beats per minute now and still climbing."
    "You pulse the plug a bit faster now. Her heart rate keeps climbing."
    "You can imagine her, bent over, fucking herself with her plug as it vibrates deep inside her needy bowel."
    "After a minute, you see her heart rate peak. You give her 10-15 seconds of strong pulsing vibrations."
    $ the_person.change_happiness(5)
    $ the_person.change_obedience(3)
    "You see the obvious spike on the chart now as her heart rate subsides. The plug registers that it is now back in place and not being used for masturbation."
    "After a few seconds you get a text message from [the_person.possessive_title]."
    #TODO picture of her bent over
    the_person.char "That felt good! You should come visit me soon though... get yourself some of this!"
    "She attached a picture of herself, bent over and showing her ass to you."
    return

label starbuck_anal_fetish_request(alert = False):
    $ the_person = starbuck
    "You feel your phone vibrate with a notification."
    "[the_person.title] sent you a text and a picture!"
    $ the_person.draw_person(position = SB_get_random_ass_position())
    the_person.char "Hey! You need to get over here and fuck this! I'm about to go crazy! I might jump the next guy that walks through my door!"
    "Sounds like she is desperate for a dick in her ass!"

    return

label starbuck_anal_fetish_checkup(alert = False):
    $ the_person = starbuck
    "You decide to check up on [the_person.title]. You pull out your phone and check up on her."
    "You see she has been good. She's had the plug in, just the way she said she would!"
    if the_person.arousal > 40:
        "You can also see her temperature is a little elevated, consistent with what you would expect from someone in a consistent arousal state."
    "You decide to let her know you're thinking about her and her delicious ass."
    "You set the vibration setting to high, then press and hold the vibration button for several seconds. You can see her heart rate spike as her plug quakes inside her ass."
    "You wait for a few seconds, then send her another round of vibrations."
    $ the_person.change_arousal(20)
    "You decide that is enough for now and go back to what you were doing."
    return



label starbuck_greetings(the_person):
    call starbuck_intro from SB_starbuck_intro_1
    return

label starbuck_clothing_accept(the_person):
    if the_person.obedience > 140:
        the_person.char "Oh wow, I bet this will look great on me!"
    else:
        the_person.char "You think this would look good on me? I'll keep that in mind!"
    return

label starbuck_clothing_reject(the_person):
    if the_person.obedience > 140:
        the_person.char "Oh, I wish I could wear this [the_person.mc_title], but even at a sex shop you can go too far..."
    else:
        if the_person.sluttiness > 60:
            the_person.char "Oh my god [the_person.mc_title]... It's hot, but I can't wear this here!"
        else:
            the_person.char "Oh my god [the_person.mc_title], an outfit like that should only be worn in private!"
    return

label starbuck_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "Sorry [the_person.mc_title], I should really get myself dressed properly again! Just a second!"
    else:
        if the_person.sluttiness > 50:
            the_person.char "I love the way you're looking at me, but I should wear something else before another customer comes in."
        else:
            the_person.char "Oh my god, I shouldn't be dressed like this at the shop! Just give me a moment."
    return

label starbuck_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "I wish I could let you, but I don't think I should be taking that off yet."
    elif the_person.obedience < 70:
        the_person.char "Sorry [the_person.mc_title], but I love being a tease. I'm going to leave that on for a bit."
    else:
        the_person.char "I can't take that off right now [the_person.mc_title]!"
    return

label starbuck_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            "[the_person.possessive_title] gives you a wink."
            the_person.char "I was thinking the same thing!"
        else:
            the_person.char "You want to do that with me, [the_person.mc_title]? You're lucky I'm just as perverted."
    else:
        the_person.char "Hmmm, sounds good! Let's do it!"
    return

label starbuck_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh god [the_person.mc_title], I don't think I could do this for anyone else..."
        the_person.char "But I just can't say no to you."
    else:
        if the_person.obedience > 130:
            the_person.char "If that's what my best customer needs me to do..."
        else:
            the_person.char "I'm not sure I should be letting a customer... sample the goods this way..."
            "She seems conflicted for a second."
            the_person.char "Okay, just promise you won't tell anyone!"
    return

label starbuck_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Not yet, I need to get warmed up first. Let's start out with something a little more tame."
    else:
        the_person.char "I... we can't do that [the_person.mc_title]. You're one of my customers, after all!"
    return

label starbuck_sex_angry_reject(the_person):
    if the_person.sluttiness < 20:
        the_person.char "What the fuck! Do you think I'm just some whore who puts out for anyone who asks?"
        the_person.char "Ugh! Get away from me, I don't even want to talk to you after that."
    else:
        the_person.char "What the fuck do you think you're doing, even I won't do that!"
        the_person.char "Get the fuck away from me, I don't even want to talk to you after that!"
    return

label starbuck_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "What's up [the_person.mc_title]? Do you need any help testing the merchandise?"
        else:
            the_person.char "What're you thinking about? You look like you're up to something."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Do you have something in mind? I wouldn't mind fooling around some..."
        elif the_person.sluttiness > 10:
            the_person.char "Oh, do you see something you like?"
        else:
            the_person.char "I... what do you mean [the_person.mc_title]?"
    return

label starbuck_seduction_accept_crowded(the_person):
    if the_person.sluttiness < 20:
        "[the_person.possessive_title] grabs your arm and smiles."
        the_person.char "That sounds great. Let's head to the backroom and get started... let's at least find someplace quiet."

    elif the_person.sluttiness < 50:
        the_person.char "I... I mean, we shouldn't do anything like that without at least going to the back room... right?"

    else:
        the_person.char "Oh god, that sounds so hot. Let's get to it!"
    return

label starbuck_seduction_accept_alone(the_person):
    if the_person.sluttiness < 20:
        the_person.char "Well, there's nobody around to stop us..."
    elif the_person.sluttiness < 50:
        the_person.char "Mmm, that's a fun idea. Come on, let's get to it!"
    else:
        the_person.char "Oh [the_person.mc_title], I can't wait!"
    return

label starbuck_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        "[the_person.possessive_title] blushes and looks away from you awkwardly."
        the_person.char "I, uh... Sorry [the_person.mc_title], I just don't feel that way about you."

    elif the_person.sluttiness < 50:
        the_person.char "Oh, it's tempting, but I'm just not feeling like it right now. Maybe some other time?"
        "[the_person.possessive_title] smiles and gives you a wink."

    else:
        "[the_person.possessive_title] looks at you and frowns"
        the_person.char "It's so, so tempting, but I've had a rough day and just don't feel up to it right now [the_person.mc_title]. Hold onto that thought though."
    return

label starbuck_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "I hope you are ready to back that flirting up with some action!"
        else:
            the_person.char "Thank you for the compliment, sir."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, I like what I'm seeing too."
            "[the_person.possessive_title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person.char "Hey, maybe if you buy something first."
            "[the_person.possessive_title] gives you a wink and smiles."
    return

label starbuck_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Mmm, that feels great. I love it when you blow a big load all over my face."
            "[the_person.possessive_title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person.char "Mmm, thanks! I hope you enjoyed it as much as I did!"
            "[the_person.possessive_title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Ah... I love a nice, hot load on my face. Don't you think I look hot like this?"
            "[the_person.char] runs a finger through a puddle of your cum and then licks it clean, winking at you while she does."
        else:
            the_person.char "Fuck me, you really pumped it out, didn't you?"
            "[the_person.possessive_title] runs a finger along her cheek, wiping away some of your semen."
    return

label starbuck_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Oh god, you taste so good. Thank you for the treat [the_person.mc_title]."
        else:
            the_person.char "Mmm, thank you sir. Feel free to browse while I clean myself up!"
    else:
        if the_person.sluttiness > 80:
            the_person.char "Mmm, your cum tastes so great [the_person.mc_title], are you sure there isn't any more of it for me?"
            "[the_person.possessive_title] licks her lips and sighs happily."
        else:
            "[the_person.possessive_title] licks her lips and smiles at you."
            the_person.char "Mmm, that was nice."
    return

label starbuck_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "One sec, I want to take something off."
        else:
            the_person.char "Ah, I'm wearing way too much right now. One sec!"

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "Why do I bother wearing all this?"
        else:
            the_person.char "Wait, I want to get a little more naked for you."

    else:
        if the_person.arousal < 50:
            the_person.char "Give me a second, I'm going to strip something off just. For. You."
        else:
            the_person.char "Ugh let me get this off. I want to feel your skin pressed up against me!"
    return

label starbuck_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "I wish I could talk more, but I have other customers. Can we talk later [the_person.mc_title]?"
    else:
        the_person.char "Hey, I'd love to chat but I have a million things to get done around the store right now. Maybe later?"
    return

label starbuck_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "Ugh, jesus you two. Get a room or something, nobody wants to see this."
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.possessive_title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        the_person.char "Could you two at least keep it down? This is fucking ridiculous."
        $ the_person.change_happiness(-1)
        "[the_person.possessive_title] tries to avert her gaze and ignore you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person.char "You're certainly feeling bold today [the_sex_person.name]. At least it looks like you're having a good time..."
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.possessive_title] watches for a moment, then turns away  while you and [the_sex_person.name] keep [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Oh wow that's hot. I should sell tickets to this!"
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.possessive_title] watches you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Come on [the_person.mc_title], [the_sex_person.name] is going to fall asleep at this rate! You're going to have to give her a little more than that."
        "[the_person.possessive_title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."
    return

label starbuck_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "I can handle it [the_person.mc_title]. Let's show [the_watcher.name] how it's done!"
        $ the_person.change_arousal(1)
        "[the_person.possessive_title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Don't listen to [the_watcher.name]. This is a sex shop, surely they expect to see something like this when they walk in?"

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        the_person.char "I don't usually demonstrate the goods like this, [the_watcher.name]. You understand, right?"
        "[the_person.possessive_title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Oh [the_person.mc_title], [the_watcher.name] is watching you fuck my brains out!"
        $ the_person.change_arousal(2)
        "[the_person.possessive_title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "Fuck [the_person.mc_title], maybe we should have gone to the back room?"
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.possessive_title] seems uncomfortable with [the_watcher.name] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "Ah, now this is a party! Maybe when he's done you can tap in and take a turn [the_watcher.name]!"
        the_person.char "Orgy day at Starbuck's Sex Shop... that's actually a pretty good idea!"
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.possessive_title] seems more comfortable [the_position.verb]ing you with [the_watcher.name] around."

    return
init python:
    def starbuck_titles(person):
        valid_titles = [reserved_titles(person)]
        valid_titles.append("Cara")
        return valid_titles
    def starbuck_possessive_titles(person):
        valid_possessive_titles = [relaxed_titles(person)]
        if person.sluttiness > 60:
            valid_possessive_titles.append("Your slutty business partner")
        if person.sluttiness > 100 and person.sex_skills["Anal"] >= 4:
            valid_possessive_titles.append("Your buttslut")
        if SB_check_fetish(person, cum_external_role) or SB_check_fetish(person, cum_internal_role):
            valid_possessive_titles.append("Your cum guzzler")
            valid_possessive_titles.append("Your cum catcher")
        return valid_possessive_titles
    def starbuck_player_titles(person):
        valid_player_titles = [reserved_player_titles(person)]
        if starbuck.shop_progress_stage > 1:
            valid_player_titles.append("Business Partner")
        return valid_player_titles
