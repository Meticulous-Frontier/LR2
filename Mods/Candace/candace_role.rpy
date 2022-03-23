#Candace, AKA Candi. Office bimbo. First met via Ophelia's story line. Can eventually corrupt, hire, and seduce her as revenge. Has default bimbo personality
# After hiring her, get discount on supplies purchased based on her sluttiness (she offers to seduce suppliers)
#Later, can develop anti bimbo serum to restore her. Transforms into Candace. Still slutty, but incredibly smart.
#Uses smarts to further seduce suppliers for a bigger discount
#TODO figure out max discounts. Probably 10-20%? Late game, supply discount is mostly flavor players are probably already profitable. Make available earlier via policy? "Logistics Coordinator?"
#Enjoys supply work, skirts, showing her ass.
init 2 python:
    #Requirement functions
    def candace_meet_at_office_store_requirement(person):
        if person.location == office_store and mc.business.is_work_day():
            return True
        return False

    def candace_get_to_know_requirement(person):
        if person.location == office_store:
            if not candace_get_has_quit_job():
                if not candace_can_talk():
                    return "Already talked today"
                return True
        return False

    def candace_convince_to_quit_requirement(person):
        if candace_get_can_convince_to_quit() and ophelia_get_will_help_candace():
            if mc.business.get_employee_count() >= mc.business.max_employee_count:
                return "At employee limit"
            if not candace_get_has_quit_job():
                return True
        return False

    def candace_goes_clothes_shopping_requirement(person):
        if candace.employed_since == -1 or candace.event_triggers_dict["clothes_shopping"] != 0:
            return False
        if candace.days_employed > 7:  #She's been working at least a week.
            if mc.business.has_funds(500) and candace.location == candace.work:
                return True
        return False

    def candace_overhear_supply_order_requirement(person):
        if day > candace.employed_since + 14:
            if time_of_day > 1:
                if person.sluttiness > 40:
                    if person.is_at_work():
                        return True
        return False

    def candace_supply_order_discount_requirement():
        if time_of_day == 1:
            if mc.is_at_work() and mc.business.is_open_for_business():
                return True
        return False

    def candace_topless_at_mall_requirement(the_person):
        if the_person.location in [mall, gym, home_store, clothing_store, office_store, mall_salon]:
            if the_person.love >= 40:
                return True
        return False

    def candace_midnight_wakeup_requirement():
        if mc.business.research_tier >= 3 and candace_starbuck_are_friends() and candace.love >= 60:
            if time_of_day == 4:
                if renpy.random.randint(0,100) < 15: #Average 7 days
                    return True
        return False

    def candace_begin_cure_research_requirement(the_person):
        if the_person.is_at_work():
            return True
        return False

    def candace_anti_bimbo_serum_requirement():
        if mc.business.is_open_for_business() and mc.is_at_work():
            # lock for at least 2 weeks
            if day >= candace_get_living_with_stephanie_day() + 14:
                return True
        return False

    def candace_cure_bimbo_requirement():
        if mc.business.is_open_for_business() and mc.is_at_work():
            if mc.business.is_trait_researched(anti_bimbo_serum_trait):
                return True
        return False

    def candace_meet_doctor_candace_requirement():
        if mc.business.is_open_for_business() and mc.is_at_work():
            if time_of_day == 2:
                if day >= candace_get_cure_day() + 7:
                    return True
        return False

    #Candace Actions (define actions in init)
    candace_meet_at_office_store = Action("Meet Candi", candace_meet_at_office_store_requirement, "candace_meet_at_office_store_label")
    candace_get_to_know = Action("Get to know her {image=gui/heart/Time_Advance.png}", candace_get_to_know_requirement, "candace_get_to_know_label", menu_tooltip = "Find out more about Candi")
    candace_convince_to_quit = Action("Convince her to quit", candace_convince_to_quit_requirement, "candace_convince_to_quit_label", menu_tooltip = "Quit her current job and join your company.")
    candace_goes_clothes_shopping = Action("Clothes shopping", candace_goes_clothes_shopping_requirement, "candace_goes_clothes_shopping_label")
    candace_overhear_supply_order = Action("Overhear supply call", candace_overhear_supply_order_requirement, "candace_overhear_supply_order_label")
    candace_supply_order_discount = Action("Candi reports success", candace_supply_order_discount_requirement, "candace_supply_order_discount_label")
    candace_topless_at_mall = Action("Candi going topless", candace_topless_at_mall_requirement, "candace_topless_at_mall_label")
    candace_midnight_wakeup = Action("Candi gets arrested", candace_midnight_wakeup_requirement, "candace_midnight_wakeup_label")
    candace_begin_cure_research = Action("Candi moves", candace_begin_cure_research_requirement, "candace_begin_cure_research_label")
    candace_anti_bimbo_serum = Action("Head Researcher makes a plan", candace_anti_bimbo_serum_requirement, "candace_anti_bimbo_serum_label")
    candace_cure_bimbo = Action("Candi gets cured", candace_cure_bimbo_requirement, "candace_cure_bimbo_label")
    candace_meet_doctor_candace = Action("Meet Doctor Candace", candace_meet_doctor_candace_requirement, "candace_meet_doctor_candace_label")

    def candace_mod_initialization():
        #TODO candance wardrobe and base outfit
        candace_base_outfit = Outfit("Candace's base accessories")
        the_eyeshadow = light_eye_shadow.get_copy()
        the_eyeshadow.colour = [.15, .15, .15, 0.95]
        candace_base_outfit.add_accessory(the_eyeshadow)

        candace_wardrobe = Wardrobe("Candace's Wardrobe")

        # her boyfriend only allows her to wear this 'company wardrobe'
        outfit = Outfit("Pink Lace Top And Leggings")
        outfit.add_upper(strappy_bra.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_upper(lace_crop_top.get_copy(),[.87, .44, .63, .95])
        outfit.add_lower(strappy_panties.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_lower(leggings.get_copy(),[.87, .44, .63, .95])
        outfit.add_feet(thigh_highs.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_feet(high_heels.get_copy(),[.87, .44, .63, .95])
        outfit.add_accessory(lipstick.get_copy(),[.41, .16, .38, 0.5])
        outfit.add_accessory(heavy_eye_shadow.get_copy(),[.87, .44, .63, .6])
        candace_wardrobe.add_outfit(outfit)

        # init candace role
        candace_role = Role(role_name ="It\'s Complicated", actions =[candace_get_to_know, candace_convince_to_quit], hidden = True)
        candace_job = Job("Assistant", candace_role, purgatory, work_times = [1, 2])

        global candace
        candace = make_person(name = "Candace", last_name = "Hooper", age = 29, body_type = "standard_body", face_style = "Face_12", tits = "F", height = 0.94, hair_colour = ["black",[0.09,0.07,0.09,1]], hair_style = curly_bun, skin="black",\
            eyes = "light blue", personality = candace_personality, name_color = "#dda0dd", dial_color = "#dda0dd", starting_wardrobe = candace_wardrobe, \
            stat_array = [3,1,5], skill_array = [2,1,2,1,5], sex_array = [2,3,4,1], start_sluttiness = 35, start_obedience = -40, start_happiness = 76, start_love = 0, \
            title = "Candi", possessive_title = "Your acquaintance",mc_title = mc.name, relationship = "Girlfriend", SO_name = ophelia_get_ex_name(), kids = 0, base_outfit = candace_base_outfit,
            force_random = True, forced_opinions = [
                ["supply work", 2, True],        # she loves HR work
                ["skirts", 1, False],        #And Skirts
                ["the colour pink", 2, False], #She loves pink
                ["the colour yellow", 1, False],
                ["the colour purple", -2, False],
                ["the colour green", -2, False],
                ["pants", -2, False],        #She hates pants!
                ["high heels", 2, False]
            ], forced_sexy_opinions = [
                ["being submissive", 1, False], # likes when others have their way with her
                ["giving handjobs", -2, False], # prefers to use other body parts...
                ["skimpy outfits", 1, False],
                ["showing her tits", 2, False],
                ["not wearing underwear", 2, False],
                ["cheating on men", 1, False]
            ])

        candace.generate_home()
        candace.add_job(candace_job, job_known = True)
        candace.set_schedule(office_store, the_times = [3], the_days = [0, 1, 2, 3, 4]) #Buying office supplies for her employer.
        candace.home.add_person(candace)
        candace.event_triggers_dict["met_at_store"] = 0
        candace.event_triggers_dict["day_met"] = -1 #Might eventually change the code where candi gets INIT other than when you meet her, so leave this -1 for now
        candace.event_triggers_dict["learned_about_unhappy"] = 0
        candace.event_triggers_dict["learned_about_bf_control"] = 0
        candace.event_triggers_dict["learned_about_previous_work"] = 0
        candace.event_triggers_dict["learned_about_uniform"] = 0
        candace.event_triggers_dict["learned_about_pay"] = 0
        candace.event_triggers_dict["relationship_doubt_score"] = 0  #Everytime you plant a seed of doubt, increment this.
        candace.event_triggers_dict["quit_job"] = 0
        candace.event_triggers_dict["last_talk_day"] = 0
        candace.event_triggers_dict["clothes_shopping"] = 0
        candace.event_triggers_dict["supply_discount_active"] = False
        candace.event_triggers_dict["is_bimbo"] = True

        candace.add_unique_on_room_enter_event(candace_meet_at_office_store)
        return

    def create_debug_candace(): #Use this function to make a version of Candace for debug purposes.
        if "candace" in globals():
            renpy.say(None, "Candace already exists! Overwriting")

        candace_base_outfit = Outfit("Candace's base accessories")
        the_eyeshadow = light_eye_shadow.get_copy()
        the_eyeshadow.colour = [.15, .15, .15, 0.95]
        candace_base_outfit.add_accessory(the_eyeshadow)

        candace_wardrobe = Wardrobe("Candace's Wardrobe") # This name will allow the rebuild_wardrobe function to generate a new one

        # her boyfriend only allows her to wear this 'company wardrobe'
        outfit = Outfit("Pink Lace Top And Leggings")
        outfit.add_upper(strappy_bra.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_upper(lace_crop_top.get_copy(),[.87, .44, .63, .95])
        outfit.add_lower(strappy_panties.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_lower(leggings.get_copy(),[.87, .44, .63, .95])
        outfit.add_feet(thigh_highs.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_feet(high_heels.get_copy(),[.87, .44, .63, .95])
        outfit.add_accessory(lipstick.get_copy(),[.41, .16, .38, 0.5])
        outfit.add_accessory(heavy_eye_shadow.get_copy(),[.87, .44, .63, .6])
        candace_wardrobe.add_outfit(outfit)

        # init candace role
        candace_role = Role(role_name ="It\'s Complicated", actions =[candace_get_to_know, candace_convince_to_quit], hidden = True)
        candace_job = Job("Assistant", candace_role, purgatory, work_times = [1, 2])

        global candace
        candace = make_person(name = "Candace", last_name = "Hooper", age = 29, body_type = "thin_body", face_style = "Face_3", tits = "F", height = 0.94, hair_colour = ["black",[0.09,0.07,0.09,1]], hair_style = curly_bun, skin="black",\
            eyes = "light blue", personality = candace_personality, name_color = "#d62cff", dial_color = "#d62cff", starting_wardrobe = candace_wardrobe, job = candace_job, \
            stat_array = [3,1,5], skill_array = [2,1,2,1,5], sex_array = [2,3,4,1], start_sluttiness = 35, start_obedience = -40, start_happiness = 76, start_love = 0, \
            title = "Candi", possessive_title = "Your acquaintance",mc_title = mc.name, relationship = "Girlfriend", SO_name = ophelia_get_ex_name(), kids = 0, base_outfit = candace_base_outfit,
            force_random = True, forced_opinions = [
                ["supply work", 2, True],        # she loves supply work
                ["skirts", 1, False],        #And Skirts
                ["the colour pink", 2, False], #She loves pink
                ["the colour yellow", 1, False],
                ["the colour purple", -2, False],
                ["the colour green", -2, False],
                ["pants", -2, False],        #She hates pants!
                ["high heels", 2, False]
            ], forced_sexy_opinions = [
                ["being submissive", 1, False], # likes when others have their way with her
                ["giving handjobs", -2, False], # prefers to use other body parts...
                ["skimpy outfits", 1, False],
                ["showing her tits", 2, False],
                ["not wearing underwear", 2, False],
                ["cheating on men", 1, False]
            ])

        candace.generate_home()
        candace.set_schedule(office_store, the_times = [3], the_days = [0, 1, 2, 3, 4]) #Buying office supplies for her employer.
        candace.home.add_person(candace)
        candace.event_triggers_dict["met_at_store"] = 0
        candace.event_triggers_dict["day_met"] = day #Might eventually change the code where candi gets INIT other than when you meet her, so leave this -1 for now
        candace.event_triggers_dict["learned_about_unhappy"] = 0
        candace.event_triggers_dict["learned_about_bf_control"] = 0
        candace.event_triggers_dict["learned_about_previous_work"] = 0
        candace.event_triggers_dict["learned_about_uniform"] = 0
        candace.event_triggers_dict["learned_about_pay"] = 0
        candace.event_triggers_dict["relationship_doubt_score"] = 0  #Everytime you plant a seed of doubt, increment this.
        candace.event_triggers_dict["quit_job"] = 0
        candace.event_triggers_dict["last_talk_day"] = 0
        candace.event_triggers_dict["clothes_shopping"] = 0
        candace.event_triggers_dict["supply_discount_active"] = False
        candace.event_triggers_dict["is_bimbo"] = True

        candace.add_unique_on_room_enter_event(candace_meet_at_office_store)

        return


    def create_debug_genius_candace():  #Use this function to make a version of genius Candace for debug purposes.
        if "candace" in globals():
            renpy.say(None, "Candace already exists! Overwriting")

        candace_base_outfit = Outfit("Candace's base accessories")
        the_eyeshadow = light_eye_shadow.get_copy()
        the_eyeshadow.colour = [.15, .15, .15, 0.95]
        candace_base_outfit.add_accessory(the_eyeshadow)

        candace_wardrobe = Wardrobe("Candace's Wardrobe") # This name will allow the rebuild_wardrobe function to generate a new one

        # her boyfriend only allows her to wear this 'company wardrobe'
        outfit = Outfit("Pink Lace Top And Leggings")
        outfit.add_upper(strappy_bra.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_upper(lace_crop_top.get_copy(),[.87, .44, .63, .95])
        outfit.add_lower(strappy_panties.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_lower(leggings.get_copy(),[.87, .44, .63, .95])
        outfit.add_feet(thigh_highs.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_feet(high_heels.get_copy(),[.87, .44, .63, .95])
        outfit.add_accessory(lipstick.get_copy(),[.41, .16, .38, 0.5])
        outfit.add_accessory(heavy_eye_shadow.get_copy(),[.87, .44, .63, .6])
        candace_wardrobe.add_outfit(outfit)

        # init candace role
        candace_role = Role(role_name ="It\'s Complicated", actions =[candace_get_to_know, candace_convince_to_quit], hidden = True)
        candace_job = Job("Assistant", candace_role, purgatory, work_times = [1, 2])

        global candace
        candace = make_person(name = "Candace", last_name = "Hooper", age = 29, body_type = "thin_body", face_style = "Face_3", tits = "F", height = 0.94, hair_colour = ["black",[0.09,0.07,0.09,1]], hair_style = curly_bun, skin="black",\
            eyes = "light blue", personality = genius_personality, name_color = "#d62cff", dial_color = "#d62cff", starting_wardrobe = candace_wardrobe, job = candace_job, \
            stat_array = [3,1,5], skill_array = [2,1,2,1,5], sex_array = [2,3,4,1], start_sluttiness = 35, start_obedience = -40, start_happiness = 76, start_love = 0, \
            title = "Candi", possessive_title = "Your acquaintance",mc_title = mc.name, relationship = "Single", kids = 0, base_outfit = candace_base_outfit,
            force_random = True, forced_opinions = [
                ["supply work", 2, True],        # she loves supply work
                ["skirts", 1, False],        #And Skirts
                ["the colour pink", 2, False], #She loves pink
                ["the colour yellow", 1, False],
                ["the colour purple", -2, False],
                ["the colour green", -2, False],
                ["pants", -2, False],        #She hates pants!
                ["high heels", 2, False]
            ], forced_sexy_opinions = [
                ["being submissive", 1, False], # likes when others have their way with her
                ["giving handjobs", -2, False], # prefers to use other body parts...
                ["skimpy outfits", 1, False],
                ["showing her tits", 2, False],
                ["not wearing underwear", 2, False],
                ["cheating on men", 1, False]
            ])

        candace.generate_home()
        #candace.set_schedule(candace.home, the_times = [1,2])
        #candace.set_schedule(office_store, the_times = [3], the_days = [0, 1, 2, 3, 4]) #Buying office supplies for her employer.
        candace.home.add_person(candace)
        candace.event_triggers_dict["met_at_store"] = 1
        candace.event_triggers_dict["day_met"] = day #Might eventually change the code where candi gets INIT other than when you meet her, so leave this -1 for now
        candace.event_triggers_dict["learned_about_unhappy"] = 1
        candace.event_triggers_dict["learned_about_bf_control"] = 1
        candace.event_triggers_dict["learned_about_previous_work"] = 1
        candace.event_triggers_dict["learned_about_uniform"] = 1
        candace.event_triggers_dict["learned_about_pay"] = 1
        candace.event_triggers_dict["relationship_doubt_score"] = 8  #Everytime you plant a seed of doubt, increment this.
        candace.event_triggers_dict["quit_job"] = 1
        candace.event_triggers_dict["last_talk_day"] = day
        candace.event_triggers_dict["clothes_shopping"] = 1
        candace.event_triggers_dict["supply_discount_active"] = True
        candace.event_triggers_dict["is_bimbo"] = False

        candace.add_unique_on_room_enter_event(candace_meet_at_office_store)
        mc.business.add_employee_supply(candace, False)

        return

label candace_meet_at_office_store_label(the_person):
    "As you browse some office furniture for your business, out of the corner of your eye you spot a vaguely familiar figure."
    $ the_person.draw_person()
    "Hmm... isn't that the bimbo that [salon_manager.title]'s ex is dating?"
    mc.name "Hey there... [the_person.title], right?"
    "She looks at you. She seems to recognize you."
    the_person "Ah! You must be the new guy. I'm here to pick up the umm... supplies... that we talked about on the phone."
    "Or not."
    mc.name "Sorry, you must have me confused with someone else. We met the other night, at a restaurant."
    "She squints at you for several seconds."
    the_person "Wait... you're the host? Right? I had a great time that night, at your restaurant!"
    mc.name "Actually, I was there as a customer. Just like you."
    the_person "Oh! I see. Sorry! I don't know what my problem is lately, I feel like I'm just so easily confused by things. I used to have a great memory!"
    "Sure you did..."
    mc.name "I understand. Anyway, are you meeting someone here?"
    the_person "Oh yes! I buy a lot of office supplies for my boyfriend's business here. I have an arrangement where they give me, well, a pretty good discount..."
    mc.name "Oh! That must be nice. I run a business myself, and a discount in supplies would be a wonderful thing to have."
    the_person "Oh yeah! It's easy! Do you want to know my secret?"
    mc.name "Certainly."
    "She comes close to you and whispers in your ear."
    the_person "When I pick up the supplies, I go to the backroom with the guy and suck his dick!"
    $ mc.change_locked_clarity(10)
    "You probably should have known that was coming."
    mc.name "Interesting. And your boyfriend... he is okay with this?"
    the_person "Oh yes! He says as long as they don't fuck me it's fine."
    "Hmm, so he isn't a cuck. He is just fine with using his bimbo girlfriend to further his business..."
    "?????""Ms. [the_person.name]? I have your order ready for you in the back now."
    the_person "Oh! How exciting!"
    the_person "Nice to meet you again mister. I've got some work to do!"
    $ the_person.draw_person(position = "walking_away")
    "You watch as [the_person.title] walks to the back room to pick up her supplies."
    "There is something that just doesn't seem right here. You aren't sure what it is exactly, but you feel like you should really get to know [the_person.title] better."
    "If nothing else, maybe you could convince her to have a little fun sometime..."
    $ the_person.event_triggers_dict["met_at_store"] = 1
    # make sure candace is in unique character list (prevent MC hire button)
    if candace not in unique_character_list:
        $ unique_character_list.append(candace)
    return "Advance Time"

label candace_get_to_know_label(the_person):
    if the_person.happiness > 80: #Cap her happiness until we set her free.
        $ the_person.happiness = 80
    if candace_get_learned_about_unhappy():  #We have already learned she is unhappy, so learn more about why.
        "You consider what to talk to her about."
        menu:
            "Her Boyfriend":
                call candace_talk_about_bf_control(the_person) from _candace_chit_chat_choice_BF1
            "Her Previous Job":
                call candace_talk_about_previous_work(the_person) from _candace_chit_chat_choice_work1
            "Her Pay":
                call candace_talk_about_pay(the_person) from _candace_chit_chat_choice_pay1
            "Her Clothes":
                call candace_talk_about_uniforms(the_person) from _candace_chit_chat_choice_uniform1
        "You consider trying to push more on the subject, when you are interrupted."
        "?????""Ms. [the_person.name]? I have your order ready for you in the back now."
        the_person "Yay! See you around [the_person.mc_title]!"
        $ the_person.draw_person(position = "walking_away")
        "You watch as [the_person.title] walks back to the storeroom."
        if candace_get_ready_to_quit():
            if candace_get_can_convince_to_quit():
                if ophelia_get_will_help_candace():
                    "You already talked to [salon_manager.title]. Next time you see [the_person.title], you should put the pressure on and see if you can convince her to quit and come work for you."
                elif the_person.love < 20:
                    "You can tell that [the_person.title] is wavering, but you sense hesitation. The conditions aren't quite right to get her to convince her to split with her boyfriend."
                    "Maybe if you got closer with her? If she had more affection for you, she might be more willing to break up with her asshole boyfriend."
                else:
                    "You feel like with one more push, you could probably get [the_person.title] to quit. But what will happen when you do?"
                    "You consider if for a few moments. You should probably ask for help. This guy sounds like a narcissist, and he could be trouble if you aren't careful."
                    "[salon_manager.title] used to date him... and she seems pretty knowledgeable about this kind of stuff. Maybe you should ask her for some help?"
                    $ salon_manager.event_triggers_dict["talk_about_candace"] = 1
            else:
                "You feel like you've just about convinced her that she could quit, but you need to learn more about her."
        else:
            "So far, she still seems pretty resolute on not quitting. Just keep chipping away, and you'll be able to convince her eventually!"
    else:
        mc.name "How are you doing today, [the_person.title]?"
        the_person "Oh... I'm doing okay I guess."
        mc.name "You guess?"
        the_person "Yeah... I guess, I just don't understand my boyfriend sometimes."
        mc.name "Guys can be confusing sometimes."
        the_person "I know! It's like, he's okay with me blowing the supply guys here for discounts on his work supplies."
        the_person "Then last night, I ordered a pizza and invited him over, and when he got there I was blowing the pizza guy to save some money on the tip..."
        $ mc.change_locked_clarity(10)
        "Does she ever stop sucking cock?"
        the_person "When he walked in, he got all pissed off! Like, why is it okay to do it to save money on one thing, but not something else?"
        mc.name "That does seem inconsistent."
        "She sighs."
        the_person "I know! The worst part is, he spanked me, which he knows I love, but then didn't do anything else!"
        $ mc.change_locked_clarity(10)
        the_person "I have needs! You can't just spank a girl and then not fuck her rough! It's just not right."
        mc.name "Exactly what I was thinking."
        the_person "I don't know what it is, I just feel like, something isn't right, you know? Like, I'm just in the wrong place."
        "Hmmm... very interesting."
        mc.name "You know... you don't have to work where you are now."
        the_person "Yeah... I guess... but then my boyfriend would dump me!"
        mc.name "I'm sure he would understand..."
        the_person "No no no, he already told me as much. He said, \'don't you think about quitting, or I'll dump you! and no one wants to date a dumb bimbo like you but me!\'"
        "Jesus, this guy sounds like a major narcissist. The more you learn about him, the more happy you are that [salon_manager.title] got away from him, even if involuntarily."
        the_person "And if he dumps me, who's going to fuck me every night? No, I think I'd better just stay where I'm at for now."
        $ mc.change_locked_clarity(10)
        $ the_person.event_triggers_dict["learned_about_unhappy"] = 1
        "?????""Ms. [the_person.name]? I have your order ready for you in the back now."
        the_person "Oh! Finally! Some action! See you around [the_person.mc_title]."
        $ the_person.draw_person(position = "walking_away")
        "You watch as [the_person.title] rushes to the back of the store. There is absolutely something not right with what is going on."
        "She may not be the brightest, but [the_person.title] doesn't deserve to be treated this way. You think about it for a while, but make up your mind."
        "It is going to take some convincing. You might have to plant a few seeds of doubt here and there, but surely you can get her to quit her job and dump this guy."
        "Maybe you could convince her to work for you? She seems to have quite the knack for maintaining office supplies... maybe she would have a similar skill for medical and chemical supplies?"

    $ candace.event_triggers_dict["last_talk_day"] = day # prevent talk spamming (at least two days need to pass before you can plant the next seed)
    call advance_time from _call_advance_time_candace_get_to_know_label
    return

label candace_talk_about_bf_control(the_person):
    if candace_get_learned_about_bf_control():
        mc.name "How are things going with the boyfriend? Any better?"
        the_person "No! God no. Last night, I made him dinner. I was in the kitchen, wearing only an apron, hoping he would do something while I was cooking..."
        the_person "When I was almost done, I looked over, and he was asleep on the couch!"
        mc.name "Did you wake him up?"
        the_person "I umm... he doesn't let me wake him up... says his rest is very important..."
        mc.name "Aren't your needs important too?"
        the_person "Yeah... I guess? I don't know! I just don't like it when he gets mad at me."
        menu:
            "I would help meet your needs" if candace_get_mc_is_sexually_skilled():
                $ candace_increase_doubt()
                mc.name "You know, at my job, I always reward my employees, with a multitude of different types of rewards, or bonuses."
                mc.name "You work so hard, you deserve to have someone who meets your needs."
                the_person "Ha, it's hard to imagine having a man who could actually meet my needs."
                mc.name "Who says it has to be just one man? You have wonderfully free spirit, you should be free to share that spirit with anyone you want."
                $ mc.change_locked_clarity(5)
                if candace_get_ready_to_quit():
                    the_person "You know... I think you are right. But it's scary, you know? To leave what you know for something new."
                else:
                    the_person "You might be right... but I don't think I'm ready. It's scary, you know? To leave what you know."
            "I would help meet your needs\n{color=#ff0000}{size=18}Requires: high sex skills{/size}{/color} (disabled)" if not candace_get_mc_is_sexually_skilled():
                pass
            "Sorry to hear that":
                mc.name "I'm sorry to hear about your problems."
                the_person "That's okay. I'm sure it's just me, he was probably just tired after a long day at work... right?"

    else:
        mc.name "So, how are things going with your boyfriend?"
        the_person "Oh, as good as it can be, I guess."
        mc.name "I'm not sure. Is there something in particular that is bothering you?"
        the_person "Well, I don't mean to complain, but, it just feels like everyday there are more and more rules!"
        mc.name "He gives you... rules?"
        the_person "I mean, at first it was okay, and kinda made sense. No fucking other guys, stop spending all your pay-check at the strip club."
        the_person "But it feels like everyday he's adding some kind of new rule! I can hardly keep track of them all!"
        the_person "No going to the bar without him. No talking with the other men at his business. Leave my location setting shared with him on my phone."
        "It really does seem to be what you feared it might be. Her boyfriend is an overbearing psychopath."
        mc.name "[the_person.title]... that doesn't sounds like a healthy relationship."
        the_person "That's what I thought at first, but then he told me I'm not allowed to watch daytime talk shows anymore... I don't remember why I thought it was weird to be honest."
        $ candace.event_triggers_dict["learned_about_bf_control"] = 1
        $ candace_increase_doubt()
        "Yeah, you definitely need to help her get out of this."
        mc.name "You know, I've had a few girlfriends throughout the years. Part of the relationship is being open with each other, and trusting each other."
        the_person "Oh, don't worry! I trust him completely!"
        mc.name "But do you feel that he trusts you too?"
        the_person "Of course! I just feel bad. No one ever taught me relationships are supposed to have all these rules! Thankfully he is really patient with me though."
        "Hmm... you aren't sure that this approach is going to convince her."
        mc.name "So how long have you two been together?"
        if day < 180:
            the_person "Oh, we've been together now for a little over six months! Pretty crazy to think about!"
        elif day < 365:
            the_person "Oh we've been together for just over a year now! Pretty crazy to think about!"
        else:
            $ rel_length = str((day / 365) + 1)
            the_person "Oh, we've been together for a little over [rel_length] now! Pretty crazy to think about!"
            $ del rel_length
        "Wait a minute... you do the math in your head. You were there when [the_person.title]'s boyfriend broke up with with [salon_manager.title]. That means he had been cheating on her!"
        "Not just a narcissist, but a cheater as well. Yet another reason you really need to get her out of this situation."
    return

label candace_talk_about_previous_work(the_person):
    if candace_get_learned_about_previous_work():
        mc.name "Hey, remember what you told me about your previous job?"
        the_person "Yeah! I really liked that place. I wish I still worked there."
        mc.name "I did some research on that place. Guess what? It did research and production on small run pharmaceuticals, just like the business I run now!"
        the_person "Small run... what now?"
        mc.name "Drugs, basically. Like pills."
        the_person "Oh! Yeah I remember that! Checking boxes, taking notes, talking to people."
        $ candace_increase_doubt()
        mc.name "Yeah, my business does the same thing? You know, if you quit, I would totally hire you to work for me."
        if candace_get_ready_to_quit():
            the_person "That sounds amazing. Are you sure? I mean, I feel like there's something wrong with me sometimes. Are you sure you would take me?"
        else:
            the_person "That sounds too good to be true... so it must be! My boyfriend keeps telling me he's the only one who would put up with me. Are you sure you would take me?"
        mc.name "You would be great, I would love have someone like you on board."
    else:
        mc.name "I've heard you mention your previous job a couple of times. What did you do before?"
        the_person "Oh... well, to be honest, I don't actually remember much about it. It was at a place over on the east side of town, near the old car factory."
        the_person "I remember taking these vials of stuff... liquids I think! Mixing things together, shaking them up, taking a bunch of notes."
        mc.name "You were a researcher?"
        the_person "Yeah, a scientist or something like that! I don't remember how I did it, to be honest. Now it sounds so dull, but I remember really enjoying it at the time."
        mc.name "Do you know the name of the place? It sounds like somewhere I'd like to visit sometime."
        the_person "Oh... no actually I don't, but I remember the company logo! It was a neat science beaker with 4 hearts all around it."
        "Hmm. On the east side of town? You should look it up and see if you can find out more about it."
        $ candace.event_triggers_dict["learned_about_previous_work"] = 1
        #TODO new mandatory event where you look up the old business
    return

label candace_talk_about_uniforms(the_person):
    if candace_get_learned_about_uniform():
        mc.name "Any luck talking to your boyfriend about relaxing your dress code some?"
        the_person "No... no I haven't..."
        mc.name "Haven't talked to him?"
        the_person "No, I've tried to talk to him, but he shut it down and just said it was non negotiable."
        if candace_get_employees_have_lax_uniforms():
            mc.name "You know, the girls at my company have a much more... relaxed... dress code."
            the_person "Oh? Those girls sure are lucky!"
            mc.name "Yup! I have multiple uniforms available to choose from, from conservative business suites, to topless with a set of yoga pants."
            the_person "You... you let girls go topless? That sounds... SO COMFY!!!"
            $ mc.change_locked_clarity(10)
            $ candace_increase_doubt()
            mc.name "It is! You would like it there. You know if you quit, I would hire you to work there, right?"
            if candace_get_ready_to_quit():
                the_person "I bet I would like it there! Maybe it's about time to make a change in my life."
            else:
                the_person "I think you might be right, but I don't think I'm ready. It's scary, you know? To leave what you know."
            mc.name "You would fit in wonderfully at my company."
    else:
        mc.name "I can't help but notice, every time I see you here, you have the same outfit on."
        the_person "Oh god, don't get me started. I fucking hate pants!"
        #TODO learn she hates pants
        mc.name "Ah, then why do you wear them?"
        the_person "I just got off work. My boyfriend made uniforms for everyone at work to wear pants."
        the_person "I used to wear skirts. It was great! Such easy access... and if you don't wear panties it's so easy to just, sit on someone's lap or face or whatever."
        $ mc.change_locked_clarity(20)
        mc.name "That does sound handy. Why did your boyfriend change the dress code?"
        the_person "Ah, it was my fault really. One time I was wearing this short skirt and no panties, and I was bending over to get something out from under my desk I had dropped..."
        the_person "Suddenly I felt someone's hands on my ass, feeling me up. I thought it was my boyfriend! I asked him for a quickie and soon he was fucking me."
        the_person "Imagine my surprise when my boyfriend comes around the corner! I looked back and realized it wasn't him!"
        mc.name "He didn't care for that?"
        the_person "No, he fired the guy right then and there. Then he told me I'm not allowed to wear skirts to work anymore!"
        $ candace.event_triggers_dict["learned_about_uniform"] = 1
        mc.name "That sounds awfully restrictive. Don't you think you should be able to wear what you want to work?"
        the_person "Oh, I mean, it would be nice, but I kind of understand. It keeps accidents like getting fucked by random guys from happening!"
        "She says the last bit of that sentence with as much resolve as she can muster, but you can tell from the tone her voice, she wishes it would happen once in a while anyway..."
        mc.name "You should talk to your boyfriend about it. Maybe he would let you wear a skirt if you promise to make it a certain length? Or to wear panties?"
        the_person "Hmm... that's not a bad idea! I'll have to try that sometime!"
        $ candace_increase_doubt()
    return

label candace_talk_about_pay(the_person):
    if candace_get_learned_about_pay():
        mc.name "You know, the girls who work for me, make about as much money as you do per week in a day working for me."
        the_person "Aww, you pay so well! You must really take care of your employees."
        mc.name "I'm always on the lookout for talented employees. I think you would make a good employee. You interested? I promise you'll make a lot more than you are now!"
        $ candace_increase_doubt()
        if candace_get_ready_to_quit():
            the_person "You know, I can't believe I'm saying this, but I've been seriously considering it!"
        else:
            the_person "Oh, I'm okay, I don't need the money. But I suppose it would be nice to have."
    else:
        mc.name "So, as a business owner, with several employees of my own, I have a question for you."
        the_person "Sure! Go ahead."
        mc.name "How much does your job pay, to have talent like yours?"
        the_person "Oh! I work on commission! I keep half of the money I save the company on office supplies!"
        mc.name "Ah... but what about your base rate?"
        the_person "Base rate?"
        mc.name "Yeah, like, how much do you get paid per hour, or per day? Or do you have a salary?"
        the_person "Oh, no, it's commission only! My boyfriend says working on commission will help keep me motivated to work hard!"
        mc.name "I see... and how much commission do you usually make?"
        the_person "Oh, well, I average about $20, but sometimes when I let the stock boy play with my ass I can make as much as $25!"
        mc.name "Per day?"
        the_person "Oh no, not that much. Per week!"
        mc.name "I see... and how much do you work?"
        the_person "Oh, I'm out there pretty much 9am to 5pm on weekdays..."
        "That is criminally low pay. Yet another reason you really need to get her out of this situation."
        mc.name "You know, I'm pretty sure literally ANY job would pay you more."
        the_person "Yeah, but you know the economy these days. It would be hard for someone like me to find work!"
        mc.name "Yeah, but you should probably really talk to your boyfriend about paying you more. It might be illegal how little you are making."
        the_person "Ah, I suppose, but I'm okay with it. My boyfriend puts the money back into the business anyway!"
        mc.name "But how do you afford, say, rent?"
        the_person "Oh! That's easy! I have another little agreement with my landlord. Instead of rent..."
        mc.name "That's okay. I think I get the picture."
        $ candace.event_triggers_dict["learned_about_pay"] = 1
    return

label candace_convince_to_quit_label(the_person):
    $ scene_manager = Scene() # make sure we have a clean scene manager
    $ scene_manager.add_actor(the_person)
    $ ex_name = ophelia_get_ex_name()
    "Alright. This is it. It's now or never."
    mc.name "[the_person.title]... can I talk to you about something? Something important?"
    the_person "Oh, of course! What is it?"
    mc.name "This isn't easy to say, but, I want you to quit your job and come work for me."
    the_person "Ha, I know, I know, you keep saying that, but..."
    mc.name "I'll pay you $40 a day. Effective immediately."
    the_person "Oh! That's more than I make in a week! But I don't know..."
    mc.name "I know you used to work at a pharmaceuticals company. You told me you used to love that place! You could work at one again!"
    the_person "[the_person.mc_title], I really do have fond memories... from what I can remember... but I don't think I can do that kind of work again..."
    mc.name "You don't have to do research. My company is constantly sourcing chemicals and reagents for different products. It wouldn't be any different than what you are doing now, helping keep supplies up!"
    the_person "I just don't know. God, is it getting hot in here?"
    mc.name "Probably. Are you overheating? Wouldn't it be nicer if you could go back to wearing skirts again?"
    the_person "It really would be, to feel the breeze between my legs again."
    mc.name "Just do it. Just say yes, it will be worth it, I promise."
    $ scene_manager.update_actor(the_person, emotion = "sad")
    the_person "I want to... I really do..."
    mc.name "Then why don't you?"
    the_person "I'm... I'm so scared! [ex_name]... I think he knows I've been thinking about leaving! Last night he told me if I quit, he's going to expose that I've been trading sexual favors for discounts..."
    the_person "He says it's illegal! That I'll go to jail for being a prostitute!"
    mc.name "Don't worry, I know someone who can help. I have a friend who has dealt with a similar situation... let's say she can handle herself."
    mc.name "She can help you. Take a leap of faith. You can trust me."
    "She thinks about it for a bit."
    "?????""Ms. [the_person.name]? I have your order ready for you in the back now."
    "She looks over at the clerk. She seems to make up her mind."
    the_person "Actually... I'm really sorry. I can't take the delivery tonight."
    "?????""Oh? Okay Ms. [the_person.name]. Have a good night!"
    the_person "I think I will."
    $ scene_manager.update_actor(the_person, emotion = "happy")
    the_person "Alright mister. I'm going to trust you. What do we do?"
    mc.name "Let's go to my friend's. She'll help us get set up."
    the_person "Lead the way!"
    "Thankfully, the office supply store is right next to the mall, so it is a quick walk over to the salon."
    $ mc.change_location(mall_salon)
    $ mc.location.show_background()
    "As you walk into the salon, you notice that [salon_manager.title] is working with a customer."
    mc.name "Okay, she's over there, but she's with a customer right now. While we wait for her, why don't we do the paperwork for your new employment?"
    the_person "Okay... let's do it!"
    "There is a small table to the side of the room. You sit down and start to go through it with [the_person.title]."
    $ scene_manager.update_actor(the_person, position = "sitting")

    $ mc.business.add_employee_supply(the_person)
    $ town_relationships.update_relationship(salon_manager, the_person, "Friend")

    "You complete the necessary paperwork and hire [the_person.title], assigning her to the supply department."
    "As you finish up, you notice [salon_manager.possessive_title] is walking over to the table."
    $ scene_manager.add_actor(salon_manager, position = "sitting", display_transform = character_left_flipped)
    salon_manager "Hello! I'm [salon_manager.name]. I don't think we've been properly introduced."
    the_person "Hi! You can call me [the_person.name]."
    salon_manager "You know, I used to date [ex_name] too!"
    the_person "Right... used to... kind of weird to think about, this is all happening so fast!"
    salon_manager "Don't worry. First thing's first! Do you have your phone handy? Let's take a picture together!"
    the_person "Okay! I love selfies."
    "[the_person.title] and [salon_manager.possessive_title] lean together and take a picture."
    salon_manager "There we go! That will be a great picture to send with your break up text..."
    "Oh boy. Things are about to get juicy."
    salon_manager "Let me see your phone now. Okay here we go."
    salon_manager "Guess who I met today, [ex_name]! Turns out we having something in common!.."
    "You spend the next hour or so getting [the_person.title] all set up. [salon_manager.title] really does think of everything."
    $ the_person.relationship = "Single"
    $ the_person.SO_name = None
    $ the_person.remove_role(affair_role)   # people can get her to this role before she quits
    $ the_person.change_happiness(30)
    "She's got new passwords on everything from bank accounts, to social media. A locksmith is already en route to change her locks, and she's blocked her ex from her phone completely."
    "After a while, you notice they seem to be done, and now they are just trading stories and gossip. They actually seem to be getting along okay."
    "You stand up and stretch."
    mc.name "Well... I don't know about you two, but I'm pretty worn out. Take care. And [the_person.title], I'll see you at the office!"
    the_person "Sure thing boss! Oh! Should I call you boss now? Oh that sounds nice!"
    menu:
        "Boss\n{color=#00ff00}{size=18}+20 Obedience{/size}{/color}":
            $ the_person.set_mc_title("Boss")
            $ the_person.change_obedience(20)
        "[mc.name]\n{color=#00FF00}{size=18}+20 Happiness{/size}{/color}":
            $ the_person.set_mc_title(mc.name)
            $ the_person.change_happiness(20)
    the_person "Whatever you say [the_person.mc_title]!"
    "Well, you now have your very own office bimbo. While before you were just looking to get her out of a bad situation, you are now considering some of the possibilities open to you..."
    $ the_person.set_possessive_title("Your Office Bimbo")
    mc.name "Alright, well have a good night."
    salon_manager "Goodnight!"
    the_person "Bye!"
    $ candace.event_triggers_dict["quit_job"] = 1
    # she has quit her job, give her a new wardrobe
    $ rebuild_wardrobe(candace, force = True)
    $ candace.add_unique_on_talk_event(candace_goes_clothes_shopping)
    $ candace.add_unique_on_room_enter_event(candace_overhear_supply_order)
    call advance_time from _call_advance_time_candace_convince_to_quit_label
    return

label candace_overhear_supply_order_label(the_person):
    "You step into the office and look around. You see your employees hard at work. Close to you, you hear [the_person.title], on the phone with a supplier."
    "You can't help but overhear the conversation. As you look closer, you realize she is doing a video call."
    $ scene_manager = Scene()  #Clean Scene
    $ scene_manager.add_actor(the_person, position = "sitting")
    the_person "Yes sir that's right. We need more of this stuff! Looks like it's called up... cal... calcium... phos... oh balls"
    "????" "I'm not sure I understand what you need. Do you have a label you can show me?"
    the_person "Oh! Certainly... I'd be glad to show you anything you want... let me see here."
    "She goes through a draw in her desk and pulls out an empty vial. She tries holding it up to the camera."
    if the_person.outfit.tits_available():
        "????" "It's too close... can you back it up a little bit?... Yeah a bit farther..."
        "With her tits out, she pulls the vial back until it is resting in her cleavage."
        $ mc.change_locked_clarity(20)
        "????" "Now it's having a hard time focusing... can you move the camera closer?"
        "She takes the cam and brings up, point blank to her tits, with the little vial nestled between them."
    else:
        "????" "I can't make out the label, there's too many colors in the background..."
        the_person "Oh! I know how to fix that."
        "You are hardly surprised when you see [the_person.title] start to take her top off."
        $ scene_manager.strip_to_tits(person = the_person)
        the_person "How about now?"
        $ mc.change_locked_clarity(10)
        "????" "It's too close... can you back it up a little bit?... Yeah a bit farther..."
        "With her tits out, she pulls the vial back until it is resting in her cleavage."
        "????" "Now it's having a hard time focusing... can you move the camera closer?"
        $ mc.change_locked_clarity(20)
        "She takes the cam and brings up, point blank to her tits, with the little vial nestled between them."
    the_person "Are you getting a good look sir? Of the label, of course!"
    "????" "Yeah, I see it now. Calcium phosphide. You've been most helpful! I can get you a discount on those if you'd like, as thanks for your big... help"
    "[the_person.title] chuckles. You notice her nipples are getting a little stiffer... she seems to really be enjoying this..."
    the_person "No need! Maybe I could give you my number though... and you could show me your thanks later in... another way..."
    "She trades numbers with the supplier. Wait did she just turn down a discount? You watch as she says goodbye, making sure to lick her lips and wink before ending the call."
    "You decide to talk to her about it. You don't want to stifle her... creativity... but if she's getting discounts just for doing what she would already be doing, there's nothing wrong with that, right?"
    "You walk up to her desk. She smiles at you when she sees you approach."
    the_person "Hello [the_person.mc_title]! Anything I can do for you today?"
    "You get ready to speak... but you notice her posture subtly change as she finishes that sentence. Did she just push her chest out a bit? You shake it off."
    mc.name "Yes, sorry I couldn't help but overheard your conversation with that supplier."
    the_person "Yes... sorry I just couldn't help but have a little fun with the guy..."
    mc.name "That's perfectly fine, I didn't mind that at all."
    the_person "Oh? That's good!"
    mc.name "Yeah, I'm just curious. Why did you turn down the discount? If they are offering to discount the product..."
    the_person "Oh, that. Well, I've had several suppliers start to offer discounts the last few days. I would say yes but... I was concerned they might get the wrong idea about... why I am showing them my body..."
    the_person "I've gotten dick pics from three different suppliers in the last few days... it's been great! I want them to feel like they owe me!"
    mc.name "I'm sure that if you accepted their offer of a discount, they would still send you dick pics."
    "She thinks about what you said for a bit."
    the_person "I don't know... are you sure?"
    mc.name "I'll tell you what, try it on your next call and see what happens. If it doesn't go the way you want, you don't have to accept it anymore."
    the_person "Oh! That's a good idea! I mean yeah I miss out on one... but I suppose it's worth it to try!"
    "You are glad you get her to agree. You decide to let her get back to work."
    mc.name "Let me know how it goes."
    the_person "Yes sir!"
    $ scene_manager.clear_scene()
    $ mc.business.add_mandatory_crisis(candace_supply_order_discount)
    return


label candace_supply_order_discount_label():
    $ the_person = candace
    $ scene_manager = Scene()  #Clean Scene
    $ scene_manager.add_actor(the_person)
    "As you arrive at work, [the_person.title] is wandering around, apparently looking for you."
    the_person "Ah! [the_person.mc_title]! I need to talk to you!"
    mc.name "Yes?"
    the_person "I tried what you said, and it worked! Our supplier for... for... fuck what was the chemical name..."
    "She stops talking for a second as she thinks."
    the_person "Ahh fuck it who cares. Whatever it was, they gave me a 10\% discount, and he even sent me a video later last night of him jacking off on a picture of my tits I sent him!"
    $ mc.change_locked_clarity(5)
    "That was... a lot of details."
    the_person "So... I kept going, and got almost all of our suppliers to give me some kind of discount! And it hasn't affected my umm... success rate... with sexting afterwards at all!"
    "You consider the implication. Maybe you could have her negotiate new standard rates with all your suppliers? Negotiating might be a but tough for someone like her though..."
    "Fuck it, you decide to just let her get whatever discounts she happens to get and take the extra money without pushing your luck."
    mc.name "That's great. Thank you for your hard work."
    the_person "Yes sir!"
    $ candace.event_triggers_dict["supply_discount_active"] = True
    $ scene_manager.clear_scene()
    "You now receive a 10\% discount on all supply orders."

    $ candace.add_unique_on_room_enter_event(candace_topless_at_mall)
    return

label candace_topless_at_mall_label(the_person):
    $ scene_manager = Scene()
    python:
        if police_chief.title is None:  # haven't met, set title
            police_chief.set_possessive_title("the police chief")
            police_chief.set_mc_title("Mr." + mc.last_name)
            police_chief.set_title("Officer " + police_chief.last_name)
            police_chief.wear_uniform()

    "As you walk around the mall, you notice a commotion. A small group of mostly men have gathered around someone, you walk over to see what is going on."
    "When you walk over, you find [the_person.possessive_title], and it immediately becomes clear why there is a crowd gathering around..."
    if mc.business.topless_is_legal():  #Right now it is always illegal
        pass
    else:
        $ scene_manager.add_actor(the_person)
        $ scene_manager.strip_to_tits(person = the_person, delay = 0)
        $ scene_manager.update_actor(the_person)
        "[the_person.title] is walking around the PUBLIC mall topless. Something that you are pretty sure is illegal."
        mc.name "[the_person.title], what are you doing?"
        the_person "Oh hey [the_person.mc_title]! Not much, I was just going for a little walk."
        "?????" "Alright everyone, what seems to be the issue here? Let's move along now, okay?"
        "You look over. It's a police officer!"
        $ scene_manager.add_actor(police_chief, display_transform = character_left_flipped)
        police_chief "Come on now, let's all just go back to our shopping."
        "Suddenly, she sees [the_person.title]."
        police_chief "Move along now... holy shit!"
        $ scene_manager.update_actor(police_chief, emotion = "angry")
        police_chief "Excuse me Ma'am? You can't just walk around the mall with your titties out!"
        $ scene_manager.update_actor(the_person, emotion = "sad")
        the_person "I... I can't? Really? Why not?"
        police_chief "Ma'am... That's ILLEGAL! That is called public indecency!"
        the_person "But... everyone always loves it when I get my tits out..."
        police_chief "Sure, in the privacy of your own home you can do whatever, but this is a public place!"
        police_chief "I'm gonna have to run you in, now put your hands behind you back."
        "You decide to intervene."
        mc.name "I'm sorry officer, I know this looks bad, but I know her. I'll buy her a shirt really quick and get her covered up."
        mc.name "I'm sure she won't do it again!"
        "[police_chief.possessive_title] looks at you, then back at [the_person.title], then shakes her head."
        police_chief "I mean, there are worse crimes that could be committed here... Okay, just make it quick."
        "You quickly grab [the_person.possessive_title]'s hand and lead her into the clothing store."
        $ scene_manager.remove_actor(police_chief)
        $ mc.change_location(clothing_store)
        $ mc.location.show_background()
        "You grab the first t-shirt you find and have her put it on."
        $ the_person.outfit.add_upper(tanktop.get_copy(), [1.0, 1.0, 1.0, 1.0])
        the_person "This shirt is boring!"
        mc.name "[the_person.title], I know. But you can't be doing that, okay?"
        the_person "I still don't understand what I was doing wrong!"
        mc.name "There are laws in place! As nice as it would be, you can just walked around in public, topless."
        mc.name "If you want to do that at work, that is fine, but you have to wear a shirt to the mall!"
        "[the_person.possessive_title] pouts."
        the_person "Okay. I'm sorry [the_person.mc_title], I didn't mean to cause you trouble."
        "You walk with [the_person.title] to the check out counter. You have the cashier ring up the shirt."
        $ mc.business.change_funds(-20)
        "After you check out, suddenly [the_person.possessive_title] turns to you and hugs you."
        $ scene_manager.update_actor(the_person, position = "kissing")
        the_person "Thank you. You've always been so nice to me..."
        "You put your hands on her back and hold her for a few seconds."
        "You start to wonder if she is going to be okay. Whatever happened that turned her into a bimbo, she seems to be barely functional."
        mc.name "You stay out of trouble, okay?"
        $ scene_manager.update_actor(the_person, emotion = "happy", position = "stand3")
        "[the_person.title] lets go of you and gives you a big smile."
        the_person "Okay!"
        mc.name "I'll see you at work."
        the_person "Yes Sir!"
    $ the_person.change_love(5, 60)
    $ scene_manager.clear_scene()
    $ mc.business.add_mandatory_crisis(candace_midnight_wakeup)
    return

label candace_midnight_wakeup_label():
    python:
        if police_chief.title is None:  # haven't met, set title
            police_chief.set_possessive_title("the police chief")
            police_chief.set_mc_title("Mr." + mc.last_name)
            police_chief.set_title("Officer " + police_chief.last_name)

        # make sure she is in the police station wearing her uniform
        police_chief.change_location(police_station)
        police_chief.wear_uniform()

    "Your phone goes off in the middle of the night, waking you up. You look over at it."
    "You have no idea who it is, so you silence it and roll over. Seconds later, it's going off again. You groggily sit up and answer your phone."
    mc.name "Hello?"
    "?????" "Hi. Is this [mc.name]?"
    mc.name "Yes..."
    "?????" "This is [police_chief.title] with the police department. We have a [the_person.name] [the_person.last_name] here who asked us to call you."
    "Candace? Who do you know named Candace?"
    mc.name "I'm sorry I'm not sure who that is..."
    police_chief "She also goes by Candi."
    "Oh shit! What is [the_person.name] doing at the police department?"
    mc.name "Oh! Is she okay?"
    police_chief "She's fine. She got swept up last night in a prostitution sting. Apparently she was going around a strip club last night offering services..."
    $ mc.change_locked_clarity(10)
    police_chief "But it turns out she was doing it for free. We got multiple witnesses so we are gonna let her go."
    police_chief "We were just gonna send her off, but I didn't feel good about her walking home alone this time of night so I asked if she could call anyone and she gave me your name and number."
    "That sounds exactly like something [the_person.name] would do."
    mc.name "Okay... I'll be there in 20 minutes."
    "You hang up the phone and take a minute. [the_person.name], you REALLY need to be more careful. Who knows what kind of guy you could have wound up with? You wonder if it isn't time to do something more drastic with her."
    "You get up and quickly get yourself dressed. You leave a quick note on the counter in case anyone notices you are gone in the middle of the night and head out. It's a fairly short walk to the police station."
    #Change to police station
    $ police_station.show_background()
    "As you walk in, you walk up to the front desk. There's a good looking girl behind the desk. She smiles when she greets you."
    "?????" "Hello. Can I help you?"
    mc.name "Yeah. I'm here to pick up Candace."
    "?????" "Ahh. Sure thing. First though, the chief wants to talk to you in her office, privately..."
    mc.name "Okay..."
    "?????" "Her office is right down the hall there."
    "The kind officer points you the way to go. You head down the hall, take a breath and knock."
    police_chief "It's open."
    "You let yourself in."
    police_chief "Close the door, please."
    "You close the door behind you. Behind the desk is an official looking officer. She greets you with a scowl."
    $ police_chief.draw_person(position = "sitting", emotion = "angry")
    police_chief "So you must be here to pick up that crazy bitch, Candace."
    mc.name "Yeah, something like that..."
    police_chief "We need to chat. I got a call from my deputy a few hours ago at home, saying I needed to get here right away. They said they had arrested someone they didn't know what to do with."
    "Oh boy, this is going to be interesting..."
    police_chief "So I come in, and they got her in solitary lockup. I asked why, and apparently she was in a cell with a few other women and when a deputy walked by she would beg to suck his dick."
    police_chief "When he said no and walked away, he could hear her making passes at the other girls in the cell."
    police_chief "So I get here, bring her to my office and wouldn't you know it, it's the woman that was walking around topless at the mall the other day!"
    police_chief "I start asking her questions, you know. Where are you from, where's your family, that sort of thing."
    police_chief "She says she doesn't know, so I ask about friends and she says she just has a couple..."
    police_chief "We talk for a bit longer... And it's pretty clear from her conversation... This lady has no business being out in public. She is so far gone. Do you have any idea what is going on with her?"
    "You take a moment to consider how to answer this. You are going to need to proceed carefully."
    mc.name "Well, when I met Candace, she was in a bad relationship. The guy she was with was taking advantage of her."
    mc.name "I did some work on her background, and although I'm not sure where, I think she may have been involved in some sort of pharmaceutical experiment that made her like that."
    mc.name "I helped her get out of the relationship and set her up with a job at my business, trying to help her get independent again."
    police_chief "Hmm. I see. That's unfortunate, but she doesn't seem to understand that she can't just wander around downtown hitting on everything with a pulse. She's gonna wind up getting kidnapped... Or worse."
    mc.name "I agree. To be honest, I didn't realize she had been doing that."
    "The chief ponders for a few moments."
    police_chief "Look... I can't force you to do this... But it is something you might consider. It's clear to me that Candace can't really take care of herself."
    police_chief "We can't find any records pertaining to family in the area either."
    police_chief "If you put in a motion with the local courts filing for her power of conservatorship on the grounds that she is unable to function independently, I'd be willing to sign that in support."
    police_chief "With that, you could have her sent somewhere better designed to take care of folks like her. It'd be for her own good."
    mc.name "That seems... extreme? Maybe she would be willing to move in with a friend or something?"
    police_chief "Yeah... Maybe... Look, you don't HAVE to do anything. But for her sake, you should consider doing SOMETHING."
    police_chief "Otherwise, if she winds up back in here, I won't be able to just let her go, I'll have to get her committed somewhere."
    mc.name "I understand ma'am."
    police_chief "Alright. Well, good luck. I'll call down to lockup and have them bring her up."
    $ clear_scene()
    "You excuse yourself from the police chief's office. As you are walking back to the entrance, you start thinking about what you could do for [the_person.name]. Maybe she could move in with someone?"
    "She has been pretty close with [starbuck.name] recently. Maybe she would be willing to have a roommate?"
    "Maybe you could even have her move in with you? It might be a little cramped, but you think if you explain things to Mom and [lily.name] they would understand."
    "You think a little more. What about the bimboism itself? Maybe there is some way it could be reversed? You've made some incredible strides recently with the serums at your business, but you've never considered trying to undo their effects."
    "Is such a thing possible? Maybe you could talk to [mc.business.head_researcher.name] about it?"
    $ the_person.draw_person()
    "As you stand at the entrance, lost in thought, an officer brings [the_person.name] out."
    if the_person.love > 20:
        the_person "Hey boss! Sorry to have them call you. They kept asking me who would come and get me and you were the only one I could think of!"
    elif the_person.love < 20:
        the_person "Oh, hey boss... I'm sorry to drag you out here in the middle of the night like this..."
    else:
        the_person "Hey [the_person.mc_title]. Sorry about this..."
    mc.name "It's okay. Let's just get you home. We can talk about this when we get there."
    "The officer says you are free to go, so you step out into the night with her."

    $ downtown.show_background()
    "As you walk towards her house, you sigh when she tries to lead you into a back alley."
    the_person "It's been a frustrating night... I just thought, like, maybe we could..."
    $ mc.change_locked_clarity(10)
    mc.name "Let's get back to your place first, okay?"
    the_person "Aww, okay."
    "It's pretty clear you that if you don't do anything, [the_person.name] is going to get herself into real trouble. Is this really something you want to get yourself involved in though?"
    "You get to her apartment, and soon she is walking through the front door... Which was completely unlocked..."
    #candi home background
    $ mc.change_location(the_person.home)
    $ mc.location.show_background()
    the_person "Finally! Let's have some fun!"
    mc.name "Wait... We need to talk first."
    the_person "God damnit why does everyone just want to talk? Just like... Let's get naked and then like... Let our bodies do the talking?"
    $ mc.change_locked_clarity(15)
    mc.name "This is important."
    "It's time to make a decision. What are you going to do?"
    menu:
        "Move in with you \n{color=#ff0000}{size=18}Corruption path \n Not yet written{/size}{/color} (disabled) ":
            pass
        "Move in with \n{color=#ff0000}{size=18}FWB path \n Not yet written{/size}{/color} (disabled)":
            pass
        "Research a cure":
            call candace_love_path_intro_label from _set_candace_to_love_path
        "Do nothing \n{color=#ff0000}{size=18}Abandon path \n Not yet written{/size}{/color} (disabled)":
            pass

    python:
        clear_scene()
    return

label candace_love_path_intro_label():
    $ the_person = candace
    $ the_person.draw_person()
    "You've made up your mind. While the current [the_person.title] certainly has her charms, the drug she was given is ruining her life."
    "You care about her too much to let that happen. You have to do what you can to research it and see if you can reverse the effects."
    mc.name "[the_person.title]... Tomorrow we are going to talk to [mc.business.head_researcher.name]. I want to see if we can try and reverse the experiment that made you like this."
    the_person "Made me... Like this? I don't understand... Don't you like me?"
    mc.name "Of course I do. But the changes that it caused, you're a danger to yourself. How long have you been going out and wandering around, looking for a fuck?"
    the_person"I... err... I mean... Sometimes I just get the urge..."
    mc.name "And you can't control it?"
    the_person "I mean... Why should I? It's just for fun!"
    mc.name "I get that, but you can't just wander the streets. I got you out of your previous relationship because I care about you and and couldn't stand to see you getting taken advantage of like that."
    mc.name "If you keep doing this, someone even worse is going to come along and who knows what will happen."
    $ the_person.draw_person(emotion = "sad")
    the_person "I... I..."
    "A small tear is coming down her eye."
    the_person "I don't want to be... Like... A burden..."
    "You step closer to her, pulling her into a hug."
    the_person "If that is what you think... I trust you boss."
    "You feel relieved. You could have gone through court to file to be her conservator, but it sounds like it won't come to that. You hold her close for a while. Soon, you feel a little movement."
    "[the_person.title]'s hand makes it way from your back to your front, as she begins stroking your crotch."
    the_person "Is it... Is it time now?"
    $ mc.change_locked_clarity(20)
    "She truly is insatiable."
    if mc.energy < 50:
        "You are exhausted from a long day, but you dig deep, knowing there's no way you could leave her without giving [the_person.title] a decent dicking."
        $ mc.change_energy(50)
    "[the_person.title] gives a little yelp as you pick her up."
    mc.name "Yes, it's time now."
    $ the_person.draw_person(position = "against_wall", emotion = "happy")
    the_person "Yay! I've been waiting for this all night!"
    "[the_person.title] wraps her legs around you, grinding against you, as you carry her over to her kitchen counter."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(15)
    if not the_person.vagina_available():
        "You pull off everything between you and her cunt."
        $ the_person.strip_to_vagina(prefer_half_off = True, visible_enough = True, position = "missionary")
    "[the_person.title] reaches down and starts to play with herself as you start to get undressed. She starts to moan as you pull your cock out."
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(30)
    the_person "Just put it in me, I'm ready for it... Whoa!"
    $ the_person.draw_person(position = "missionary")
    "You grab legs and push them up over her head. You waste no time, lining yourself up with her slit, you push yourself into her."
    the_person "Oh! Fucking... Finally!"
    "[the_person.title] grabs her own legs, holding them back for you as best she can. It's time to give her pounding she's been looking for!"
    call fuck_person(the_person, start_position = piledriver, start_object = make_counter(), private = True, skip_intro = True, skip_condom = True) from _call_candace_love_fuck_01
    "You look at the clock on [the_person.possessive_title]'s microwave. It's almost 2am. You are exhausted."
    mc.name "Hey... It's really late... Can I crash here tonight?"
    "[the_person.title]'s face gets disturbingly excited."
    the_person "Oh. My. God. A slumber party! Let's do it!"
    $ the_person.draw_person(position = "walking_away")
    "She starts to lead you into her bedroom."
    mc.name "[the_person.title] I just need to get some sleep..."
    the_person "Don't worry, you'll wake up and be all like, I've never slept better!'"
    "She modulates her voice lower when she imitates you. Oh god what are you getting yourself in to..."
    $ the_person.change_to_bedroom()
    "In her bedroom, you lay down on her bed, pulling blankets up over yourself. Her bed smells flowery."
    the_person "Okay, let me just get into some jammies..."
    $ the_person.draw_person(position = "walking_away")
    "You try to stay awake for her, but your eyes are getting so heavy."
    "You are starting to feel yourself drift off when you hear the bedroom door close as [the_person.title] comes back."
    python:
        the_outfit = Outfit("Candi's Pink Nightgown")
        the_outfit.add_upper(nightgown_dress.get_copy(), [1.0, .71, .75, .65])
        the_person.apply_outfit(the_outfit)
        del the_outfit
    $ the_person.draw_person(position = "stand4")
    "She is wearing a sheer pink nightgown, and absolutely nothing else. Normally a sight like that would be enough to get your blood boiling, but right now you are just too tired."
    $ mc.change_locked_clarity(5)
    "Silently, [the_person.title] climbs into bed next to you. You turn on your side and cuddle up with her, spooning her from behind."
    $ the_person.draw_person(position = "walking_away")
    "Still naked, your cock is now up against [the_person.possessive_title]'s rear. She wiggles back and forth a couple times until it nestles in between her cheeks."
    "She grabs your hand and brings it around her front, placing it on her chest. She sighs, then turns her head."
    the_person "Goodnight boss. Thanks for spending the night... I've... Like... always wanted to try sleeping like this..."
    mc.name "Goodnight..."
    the_person "Hopefully in the morning my nightgown will be covered in cum..."
    "You know you should probably be alarmed by that statement... But you are too tired to care at this point."
    $ mc.change_locked_clarity(5)
    mc.name "Yeah... Me too..."
    "You drift off to sleep."
    "You are exhausted, but begin to dream sexy dreams about [the_person.title], the bomb shell bimbo you are cuddled up with. At one point, you are dreaming that she has climbed on top of you and is riding your cock aggressively."
    "However, the feelings are so intense, you aren't sure... Could this be real?"
    $ the_person.draw_person(position = "cowgirl")
    the_person "That's it boss... It's okay I'm like, just letting you work that boner off..."
    $ mc.change_locked_clarity(50)
    "You reach up and grab her tits. This definitely feels real. And you are really close to finishing."
    mc.name "I'm... I'm!"
    "You try to warn her. She quickly pops off and starts to jack you off. You cum, blowing your load all over her nightgown covered belly."
    $ the_person.cum_on_stomach()
    $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
    $ the_person.draw_person(position = "cowgirl") # paint cum
    "When you finish, [the_person.title] starts to lick her fingers. She seems happy as she lays back in bed next to you. Sleep rapidly overtakes you."
    $ mc.change_locked_clarity(20)
    "You sleep for a while longer. You aren't surprised though when you feel warm, wet sensations enveloping your cock again."
    "The delicious suction and the sound of [the_person.possessive_title]'s lips smacking give you all the information you need. [the_person.title] is sucking you off."
    $ the_person.draw_person(position = "blowjob")
    "You crack your eyes open and see Candi, working diligently to get you off with her mouth. You aren't sure how long she has been doing this, but it's definitely working."
    $ mc.change_locked_clarity(50)
    "You reach down and run your hand through her hair, helping keep it out of her way. She looks up at you an makes eye contact... And then maintains is as she starts to give you long, slow strokes with her mouth."
    mc.name "God... I thought I was empty last time... Get ready here it cums again!"
    $ mc.change_locked_clarity(50)
    "She takes you out of her mouth and strokes you with her hands. She points you down at her chest as you begin to fire off your load."
    $ the_person.cum_on_tits()
    $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
    $ the_person.draw_person(position = "blowjob")
    "She keeps eye contact and doesn't say a word as you drop your load all over her chest. It immediately starts soaking into her nightgown. You can see the stains from earlier still on her belly."
    "You aren't sure what happens after that, because you pass out again. Your last thought as you fall back asleep, is that [the_person.title] must think a slumber party means getting as much cum as possible on her nightgown."
    $ the_person.next_day_outfit = the_person.outfit # stay in current outfit next day
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_candace_love_path_intro # move time forward without morning events
    "You open your eyes. Sunlight? Next to you, the bed is empty. Crap, what time is it? You get up and reach for your phone."
    "The battery is dead. Is that coffee you smell? [the_person.title] must hear you stirring, she soon appears in the door to her bedroom."
    $ the_person.draw_person(position = "stand4")
    "She is still wearing the same nightgown. Evidence of your long, sex filled night apparent."
    $ mc.change_locked_clarity(20)
    the_person "Good morning sleepyhead!"
    mc.name "Hey... Is that coffee?"
    the_person "Yup! I have some eggs and toast ready too!"
    mc.name "Wow, you didn't have to do that."
    "She looks at you, a bit puzzled."
    the_person "I don't? My last boyfriend always told me to, like, always have breakfast ready whenever he gets up!"
    "That's right, her last boyfriend was a controlling asshole. You forget that sometimes."
    "You shake your head."
    mc.name "That sounds great, but you don't HAVE to do that. I appreciate it though!"
    "You start to get up. As you push the blankets down, you remember that you are completely naked."
    mc.name "Are my clothes still out there?"
    the_person "Oh... Well... Maybe I shouldn't have done this but... Like... I threw your stuff in the washer..."
    "You grimace. You doubt she has anything extra you can wear."
    the_person "It's okay though! They'll be clean before it's time to go to work."
    mc.name "Ah, okay. What time is it?"
    the_person "It's about 7."
    "That should work out okay. Eat some breakfast, and you can head in to work with [the_person.title] and go straight to [mc.business.head_researcher.title]."
    "A timer goes off in the other room."
    the_person "Oh! I gotta get back to the kitchen!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns and leaves the room. As she turns, you notice her nightgown has cum stains on the ass too... When did that happen? Did she make you cum while you were completely asleep too?"
    $ mc.change_locked_clarity(30)
    "You slowly get up, your feet a little unsteady. You work your way out of the bedroom."
    $ kitchen.show_background()
    "In the kitchen, there is a small table with two chairs. You walk over and sit down at one."
    $ the_person.draw_person(position = "back_peek")
    the_person "It's almost ready. Sorry I, like, only know how to make scrambled eggs..."
    mc.name "It's quite alright. Listen... I just want to make sure you know this... You didn't have to make me cum so much last night either..."
    the_person "Oh, I know. I just... Wanted to. I haven't had someone stay over since... Well, as far as I can remember anyway! I thought that like, if you had a good time, maybe you'd stay over again sometime..."
    "She turns and sets down two plates of eggs and toast, then turns back and starts pouring a couple cups of coffee."
    mc.name "Your old boyfriend, he never stayed over here?"
    "She turns around with two cups, then sits down across from you."
    $ the_person.draw_person(position = "sitting")
    the_person "No, he used to make me come to his place, he never really came here... He didn't let me umm... Do stuff... In the night either. Said he needed his sleep."
    mc.name "I umm... It might be good to ask next time... I didn't mind it, but I'm definitely pretty tired today."
    the_person "I'm sorry! I just... I could feel it, you know, get hard? And I couldn't help myself!"
    mc.name "It's okay, really. I could have said no, and it... Well it's pretty amazing, to wake up to a woman like you pleasuring me."
    the_person "Yay! That's why you should stay over again!"
    $ mc.change_locked_clarity(50)
    "You take a bite of the eggs. It's actually pretty good. The coffee is hot and helps wake you up."
    mc.name "Listen... Today we are going to go talk with [mc.business.head_researcher.title]. I promise we'll definitely do this again sometime, but for now, I want you to work with her, okay? I want to find out if we can reverse the effects of the lab experiment."
    "She picks at her breakfast."
    the_person "There are times... You know? Like where I feel like I almost... Remember. Like, I remember being so excited. Like I was on the verge of something! But there was a deadline... Our funding was gonna get cut..."
    $ the_person.draw_person(position = "sitting", emotion = "angry")
    "She furrows her brow."
    the_person "I just... Ugh! I can't remember! I can't remember anything..."
    mc.name "It's okay. Thank you for breakfast. It's very good."
    $ the_person.draw_person(position = "sitting", emotion = "happy")
    the_person "Like, totally!"
    "It's amazing how quickly her personality changes back to her normal, bubbly self."
    "You finish your breakfast and sit sipping your coffee. Candi finishes up as well. She stands up and grabs your plates."
    $ the_person.draw_person(position = "stand2")
    "She takes them over to the her sink and begins to wash them. As you watch, she bends over, scrubbing them clean..."
    $ the_person.draw_person(position = "standing_doggy")
    "God, her ass is great. Even after cumming over and over last night, you feel blood flowing to your dick as you watch her bent over."
    $ mc.change_locked_clarity(30)
    "Still completely naked, you know there is no way you can hide it from her. Maybe you should take charge, and give her a good fuck before you both head in to work."

    "You get up from the table and start to walk over to [the_person.possessive_title]. She doesn't seem to react... Surely she heard you get up?"
    "Then you notice. She is starting to wiggle her ass back and forth. God she really is a sex hungry minx."
    $ mc.change_locked_clarity(50)
    "You grip her hips with your hands, and then push your fully erect cock against her ass."
    the_person "Oh, thank God, I was, like, REALLY hoping to get one more before work..."
    # pull up nightgown
    $ the_person.draw_animated_removal(the_person.outfit.get_lower_top_layer(), position = "standing_doggy", half_off_instead = True)

    "You slowly lift up her nightgown, exposing her rear. You position the head of your cock against her entrance and then start to rub it up and down her slit. When you pull back for a second, your tip is slick with her arousal."
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(30)
    the_person "Stop teasing... I'm ready. I'm always ready!"
    mc.name "I know, but someone has to teach you patience."
    the_person "I'm patient! I can totally be patient, I'm the most... Ohhh!!!"
    "You cut her off mid sentence as you thrust yourself all the way into her. You don't give her time to recover, as you start to roughly fuck her."
    call fuck_person(the_person, start_position = SB_doggy_standing, private = True, skip_intro = True, skip_condom = True) from _call_candace_love_fuck_02

    # You decide to just wait and see what happens. You continue to enjoy the view of Candi's ass as she scrubs your plates clean, then sets them on a drying rack. She turns around and immediately notices your erection.
    # "Oh, thank God, I was, like, REALLY hoping to get one more in before work..."
    # She starts to walk over to you. You give her a simple ultimatum.
    # "We can do it one more time... But this time I finish inside you. Your choice of what hole."
    # She gives you a smile. "Mmm... Decisions... Decisions..."
    "As you are both recovering, you hear a buzzer go off."
    the_person "Oh! The dryer is done! I guess it's about time to head into the office..."
    "[the_person.title] disappears for a moment then comes back, holding your clothes."
    $ the_person.draw_person(position = "stand4")
    "You spend a few minutes getting dressed and freshening up a bit in the restroom. When you emerge, you see [the_person.possessive_title] also getting ready for the day."
    $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
    $ the_person.apply_planned_outfit()
    mc.name "I'm going to head in a little early. I'll page you down to my office when I've had a chance to talk to [mc.business.head_researcher.title]."
    the_person "Okay! See you later!"
    "You step out of [the_person.title]'s apartment. You should make it a priority to talk to your head researcher."
    $ mc.business.head_researcher.add_unique_on_talk_event(candace_begin_cure_research)
    if not perk_system.has_ability_perk("Lustful Youth"):
        "You feel like making [the_person.possessive_title] cum over and over has woken something inside you."
        "You feel like no matter what happens or how your day is going, you will always have the energy to make the ones you love cum."
        $ lustful_youth_perk_unlock()
        "You have gained the perk 'Lustful Youth'!"
    return

label candace_begin_cure_research_label(the_person):
    $ scene_manager = Scene()
    mc.name "I need to talk to you about something. Can come with me to my office?"
    "Your head researcher looks up from her work and nods."
    the_person "Sure, I'll be right there."
    "She follows you to your office. You close the door in the way in, and you both have a seat."
    $ ceo_office.show_background()
    $ scene_manager.add_actor(the_person, position = "sitting")
    mc.name "I need to talk to you about [candace.name]. Before she came here, she worked at another pharmaceutical company similar to this one."
    #[If you have already researched the bimbo serum]
    if mc.business.is_trait_researched(permanent_bimbo):
        mc.name "I think she may have been involved in a trial in something similar to our bimbo serum."
    else:
        mc.name "I think she may have been involved in some sort of trial on a drug that affected her mental capacities."
    the_person "I actually thought something similar. I didn't know that she came from a competitor, but her personality exhibits all of the traits that we've seen from the serum, both physical and mental."
    mc.name "Unfortunately, it has inhibited her ability to function independently. Do you think there is any way of reversing the serum effects? Or even just partially?"
    the_person "Wow... That's a difficult question. Up until now, just about all of our work has been on making the serums MORE effective, not nullifying them."
    mc.name "I understand that this is a difficult question... But unfortunately [candace.name] is no longer able to manage. I can't sit idly by and watch her life get ruined, if there is something we can do to help her."
    "Your head researcher ponders the issue for a bit."
    the_person "Can you give me some time to study her? With a few tests... Maybe I could figure something out."
    mc.name "That is fine. I actually need to find her a place to stay for a bit..."
    "You explain to [the_person.name] what happened with [candace.name] getting arrested and your conversation with the police chief."
    if the_person == stephanie:
        the_person "Wow... Tell you what. Why don't you have her move in with me for a bit? I can work on it on the side, and between me and [ashley.name] we should be able to keep an eye on her..."
    else:
        the_person "Wow. Well, I live alone, why don't you have her move in with me for a bit? I could put her in my guest room."
    mc.name "[the_person.name], you're amazing. Let me call her in and we'll talk to her."
    "You call [candace.name] and ask her to come to your office. In a minute there's a knock on your door."
    mc.name "Come in."
    $ scene_manager.add_actor(candace, display_transform = character_left_flipped)
    candace "You need something?"
    mc.name "Have a seat."
    "[candace.name] walks in and sits down next to [the_person.name]."
    $ scene_manager.update_actor(candace, display_transform = character_center_flipped, position = "sitting")
    mc.name "Remember how we talked about having [the_person.name] examining you and doing some research?"
    "She looks at you with a puzzled look."
    candace "I... I remember we had a slumber party..."
    "You can tell that she is struggling to remember."
    mc.name "You got arrested, remember?"
    candace "Right! And I told the nice police officer I was hiding drugs 'somewhere special' and so he had to do a strip search and..."
    $ mc.change_locked_clarity(10)
    mc.name "[candace.name], we said we would talk with [the_person.name] about helping you control some of your... urges... Among other things."
    candace "If you say so boss!"
    mc.name "Okay. Well, in order to keep things from impacting the business too much, [the_person.name] would like you to stay with her for a while. It will make it easier for her to run tests on you as necessary."
    candace "You mean... You want me to move in? With [the_person.name]?"
    mc.name "Don't worry, it would only be temporary. A couple weeks at most."
    mc.name "Think of it, like a slumber party."
    candace "Oh! A slumber party! That will be like, so much fun!"
    "[the_person.name] gives you a wink, seeing that [candace.name] is going along with the plan."
    the_person "I'll come over after work today and help you pack a few things."
    mc.name "Good. Let me know if either of you need anything."
    "With that, you dismiss the meeting. Hopefully [the_person.name] will be able to find some way to reverse the effects of the serum that made [candace.name] this way."
    $ candace.event_triggers_dict["living_with_stephanie"] = day
    $ candace.set_schedule(the_location = the_person.home, the_times = [0,4])
    $ mc.business.add_mandatory_crisis(candace_anti_bimbo_serum)
    $ scene_manager.clear_scene()
    $ mc.location.show_background()
    $ jump_game_loop() # jump out of dialog and return to office
    return

label candace_anti_bimbo_serum_label():
    $ the_person = mc.business.head_researcher
    $ mc.start_text_convo(the_person)
    the_person "Hey! Meet me in your office ASAP!"
    mc.name "On my way!"
    $ mc.end_text_convo()
    $ the_person.draw_person(position = "sitting")
    $ ceo_office.show_background()
    "You quickly head to your office and find [the_person.possessive_title] sitting behind your desk with her feet up."
    the_person "Guess what? I'm a fucking genius."
    mc.name "Oh? Do you have something to report from your research with Candi?"
    the_person "Something like that. You see, at first, I was racking my brain, trying to come up with some crazy chemical compound that could go back and undo a complex drug with multiple binding points and effects."
    the_person "But then I realized, I was doing it all wrong."
    mc.name "Oh?"
    the_person "Yeah! You don't need to UN-do all the previous serums effects, I just needed to create new compounds that counter the undesirable side effects."
    the_person "Specifically for [candace.name], the effect that makes her a total dumbass, the loss of her intelligence."
    mc.name "And you were successful in creating something to do that?"
    the_person "Well... Kind of. I have a pretty good idea of how to do that, but I'm going to need help researching it. I added my idea to the serum trait database."
    if not mc.business.is_trait_researched(permanent_bimbo):
        the_person "Also, we really should research the bimbo serum that we have the preliminary results for first. It would give us a better understanding before we attempt this path."
    the_person "If you want us to look into it more, the research team will get to work on it. It is something that could be very useful, in general."
    the_person "If someone were to accidentally ingest the bimbo serum or something, this could at least counteract the effect on their mental state and personality."
    mc.name "That sounds very useful. Let me think about it and I'll swing by research later if I decide to have the research department focus on it."
    if the_person.sluttiness > 60:
        the_person "Okay... In the mean time, [candace.name] can feel free to keep staying with me. We've, umm, had a lot of fun, living together the last few weeks!"
        "You remember the night you spent with her. You are certain they've been having lots of fun together."
        $ mc.change_locked_clarity(5)
        mc.name "Sounds good, I appreciate it."
        $ town_relationships.update_relationship(the_person, candace, "Best Friend")
    else:
        the_person "Okay... Well, don't delay it, okay? Living with her has been... Stressful."
        the_person "She keeps 'accidentally' walking in on me when I'm showering and sometimes when I wake up in the morning she's in my bed next to me!"
        mc.name "It won't be too much longer. I appreciate it."
        the_person "Okay... She's driving me crazy, okay!"
        $ town_relationships.update_relationship(the_person, candace, "Rival")
    "[the_person.title] leaves your office"
    $ clear_scene()
    if mc.business.is_trait_researched(permanent_bimbo):
        "You now have a new serum trait available to research."
    else:
        "As soon as you research permanent bimbofication, you will have a new serum trait available for research."
    "It has the powerful effect of reversing the bimbo serum's personality change and intelligence penalty!"

    $ unlock_anti_bimbo_serum()
    $ mc.business.add_mandatory_crisis(candace_cure_bimbo)
    return

label candace_cure_bimbo_label():
    $ scene_manager = Scene()
    $ the_person = mc.business.head_researcher
    "You have now finished researching the anti bimbo serum trait. You text your lead researcher."
    mc.name "Hey, can you make me a single dose anti bimbo serum for [candace.name]?"
    the_person "Already done. I figured you would want that."
    mc.name "Thanks, bring it to my office. I'll have her meet us there."
    $ ceo_office.show_background()
    "You walk to your office and sit down. You call [candace.name] and have her come. You admit that you are very nervous about what is about to happen."
    "Will [candace.name] suddenly remember everything that's happened?"
    "Will she hold you responsible for all the times you fucked her in her current state?"
    "There are so many possibilities, it's impossible to know what is about to happen."
    $ scene_manager.add_actor(the_person)
    $ scene_manager.add_actor(candace, display_transform = character_center_flipped)
    "Both girls walk into your office at about the same time."
    candace "Yeah boss?"
    mc.name "Why don't you both sit down."
    $ scene_manager.update_actor(the_person, position = "sitting")
    $ scene_manager.update_actor(candace, position = "sitting")
    mc.name "I have some good news [candace.name]. [the_person.name] has designed a serum to help you get back to your old self. It won't be a complete reversal, but it should help a lot with some of the issues you've been having with your memory and impulse control"
    candace "Okay boss. If that's what you want, I'd be happy to try it."
    mc.name "Thank you for trusting me. It means a lot. [the_person.name]?"
    the_person "Okay... Do you mind if I take notes? This will be our first human trial..."
    candace "Sure."
    "[the_person.name] hands [candace.name] the vial."
    the_person "Here you go. I made it a little salty, the way you said you like it. I couldn't recreate the other properties you asked for reliably..."
    candace "Oh! Well thanks for trying."
    "Without further ado, she pops the cap and downs it. She hands the vial back to [the_person.title] and you wait."
    "[candace.name] closes her eyes and begins to breath deeply. So far she doesn't seem to be having any major negative reactions, but you are starting to get concerned."
    "It's only been a minute or two, but it feels like an eternity. Finally she opens her eyes and looks at you."
    "Her pupils narrow and you can see her focus on you with a startling level of concentration."
    $ candace.personality = genius_personality
    $ candace.event_triggers_dict["is_bimbo"] = False
    $ candace.event_triggers_dict["cure_day"] = day
    $ candace.int = 9       #Scary smart
    candace "[candace.mc_title]... This is incredible!"
    mc.name "Candi, are you okay?"
    candace "Candi? Yes that's what I went by... But you can call me Candace."
    $ candace.set_title("Candace")
    "You feel a sense of relief, but also a bit of fear. Is this the same person still? Or is she someone completely different now?"
    mc.name "How are you feeling [candace.title]? Do you know where you are? What has been happening recently?"
    "She turns to [the_person.name]."
    candace "Yes. Yes I remember... Everything."
    the_person "Anything you can tell us? About what originally happened to you? Or how you got here?"
    $ scene_manager.update_actor(candace, emotion = "sad")
    "Her brow furrows as she starts to recall."
    candace "I was the lead researcher, at another company, but we had just received word that our government funding was going to get cut if we couldn't get results."
    "She clears her throat and continues."
    candace "I was desperate, but also overconfident. I wanted to rush human trials, but my boss said no. So I decided to take it myself."
    the_person "What were you trying to make?"
    candace "It seems so silly now. It was a drug designed for espionage. To reduce someone to their basest desires and to be completely open to suggestion and to be truthful."
    candace "The implications of the drug in the hands of the intelligence agency were immense."
    candace "But it was supposed to be temporary. In animal testing, the drug worked it's way out of the body within 24 hours."
    candace "Something went wrong with mine... The effects... Appear to have been permanent?"
    $ scene_manager.update_actor(candace, emotion = "angry")
    "She shakes her head. Her fists clench as she remembers the next events."
    $ renpy.say(candace.char, "The lab shut down... I had no where to work, no money... And my libido had sky rocketed... I didn't know what to do. Then I met " + ophelia_get_ex_name() + "...")
    candace "I was out in front of this strip club... Trying to find someone to take me home that night, when I ran into him. He could tell I was in a bad spot... And totally took advantage of it."
    candace "Soon I was his 'personal secretary', but he wasn't even paying me anything. I was doing all sorts of errands for him, trading sexual favors for discounts, among other things."
    $ scene_manager.update_actor(candace, emotion = "happy")
    "[candace.title] turns to you, her expression softening."
    candace "But then, I met you... At that restaurant. You convinced me to quit, and to leave that controlling asshole... And gave me a job..."
    mc.name "I'm glad I was able to help..."
    candace "You did more than just help. You brought stability back to my life, gave me hope... You even bailed me out of jail! I owe you a great debt Mr. [mc.last_name]."
    mc.name "Please, just [candace.mc_title]. I'm sorry about the times I also took advantage of your mental state."
    candace "What? I don't remember you doing anything like that."
    mc.name "We've been intimate. A lot actually."
    candace "Yes. And I'd like for that to continue. You weren't taking advantage, you were giving me exactly what I wanted."
    $ mc.change_locked_clarity(10)
    "She says that now... but a lot has happened to her. You still feel a bit uneasy about how much you fucked her while she was in her previous mental state."
    mc.name "I see. What about your work? Would you like to move over to the research department? We are doing amazing things here."
    candace "No, no. Not right now anyway. I need some time away from all that. I think for now I'd like to continue where I am now. It is actually quite enjoyable."
    candace "Actually, I think I know of a few suppliers I might be able to secure better contracts with, if I use a little persuasion anyway."
    mc.name "You don't need to keep using your body to secure discounts from suppliers if you don't want to."
    "She looks at you a bit puzzled."
    candace "Why wouldn't I want to? [candace.mc_title], a woman's body is an incredible tool to wield as they choose. If I want to be the best I can be, why would I deny myself the use of that tool?"
    "[candace.title] gives you a wink."
    candace "Plus, it's really really fun to be a tease."
    $ mc.change_locked_clarity(10)
    "Oh god, what have you done? You realize any man who tries to negotiate unfavorable contract terms with this woman is absolutely fucked."
    "It is clear that even though she has her intelligence back, [candace.title] still has her previous opinions and her sexuality."
    "You look over and see [the_person.title] scribbling down notes at an incredible pace."
    the_person "Wow... This is just absolutely amazing. Candi... Err... [candace.title]... Tonight after work, I suppose I'll help you pack up so you can move back to your place then?"
    candace "Yes I would like that. You've been very nice, letting me stay with you, but I think I would like my personal space back."
    candace "Really, the work that has been done to help me... I don't think I will ever be able to repay you."
    the_person "Well, when [the_person.mc_title] came to me and asked me to do it... I knew I couldn't say no. I'm so relieved that it has all worked out."
    candace "Ah, so you were the architect of the whole thing [candace.mc_title]? I suppose I shouldn't be surprised."
    mc.name "Well... That night at the police station. The chief talked to me before I bailed you out. He wanted me to apply to be your conservator."
    mc.name "I knew I needed to do everything I could to get the effects reversed..."
    candace "Wow... I didn't realize things had gone that far. I'm going to have to think about that for a bit."
    candace "Now, unless there's more to discuss, I think I have some new supply contracts to negotiate."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    $ scene_manager.update_actor(candace, position = "walking_away")
    "The girls turn and leave you in your office. The progress made with [candace.title] has been incredible, for sure."
    $ scene_manager.clear_scene()
    "It feels like a happy ending for her, but at the same time you feel certain that this is really just the beginning of the story of you and your genius office girl."
    $ candace.event_triggers_dict["sex_record_snapshot"] = candace.sex_record.copy() #This should take a snapshot of our sex record with candace so we can compare it later
    $ candace.set_schedule(the_location = candace.home, the_times = [0,4])
    $ mc.business.add_mandatory_crisis(candace_meet_doctor_candace)
    return

label candace_meet_doctor_candace_label():
    python:
        the_person = candace

    "It's been about a week since you cured [the_person.title] of her bimboism..."
    "Well, mostly anyway. Since that time, talking with her is like talking to an entirely different person... But also the same."
    "She still smells the same, she still twirls her hair around her finger the same way, she still smiles at you the same way."
    "Yet, every time she opens her mouth and speaks, she is completely different."
    "A few days ago you walked by the break room while able trivia show was on, and [the_person.title] was spitting answers out before the host even finished with the question."
    "When she looks you in the eye and speaks, her words carry weight. You don't blow off her suggestions as if they are nonsense anymore."
    if candace_get_sex_record_difference_tier() == 0:
        "The changes have made you wary, especially of having sex with her. She still seems willing, but it just feels wrong."
        "You can't bring yourself to lay your hands on her. And in a business like yours that could be a problem in the long term. You decide to address it."
    elif candace_get_sex_record_difference_tier() == 1:
        "The changes have made you wary about how you relate with her, especially sexually. You've gotten touchy feely with her... But so far you haven't gone further."
        "The tension is starting to get to you. You decide to address it."
    elif candace_get_sex_record_difference_tier() == 2:
        "You've tested the waters with her since then. She seems to be just as receptive to your sexual advances as before."
        "Something about her resurgent intelligence has you wary though. You decide to talk to her about it."
    elif candace_get_sex_record_difference_tier() >= 3:
        "Since the change, somehow she has gotten even sexier. Whenever an opportunity arises, you can't seem to keep your hands off of her. And she seems to enjoy it too."
        if candace_get_sex_record_difference_tier() >= 4:
            "Even now, you can't help but day dream a bit about dumping your seed inside her yet again."
            "Something about her resurgent intelligence leaves you wary though. You decide to talk to her about it."
    $ ceo_office.show_background()
    "You head to your office. You sit down at your desk and call down to [the_person.title] and ask her to come to your office. Soon she is at your door, stepping inside."
    $ the_person.draw_person()
    the_person "Good day [the_person.mc_title]."
    mc.name "Thank you for coming, [the_person.title]. Would you please close the door?"
    the_person "Certainly."
    "[the_person.title] closes the door and walks over to your desk, taking a seat."
    $ the_person.draw_person(position = "sitting")
    mc.name "I'm sorry for interrupting your day, but I wanted to talk to you about something."
    the_person "Ah yes, I calculated you would want to have this talk today."
    mc.name "Right. So obviously it would be good if we can get some things... Out in the open."
    the_person "Certainly sir. Do you mind if I go first?"
    "Oh boy. You aren't sure you are ready for this, but you are hopeful this will be a positive conversation."
    mc.name "Honestly, I'm not sure how to put this in to words. If you know how, by all means."
    the_person "Yes sir. So I've spent a lot of the last week, recounting the events I went through in the last few months, replaying them in my head, considering the outcomes and variables."
    the_person "The outcome that occurred... Where my intelligence was restored... The odds of something like that happening are less than .01 percent."
    mc.name "I mean, I'm sure it is rare that you chance upon a guy in the same industry..."
    the_person "Yes, that is certainly rare, sir. But it goes beyond that."
    the_person "To find someone that would take the time that you did, to recognize that I was in an abusive relationship, to do what it took to get me out, to get me a job, to help me make friends."
    the_person "When that same person COULD have taken a different route... Taken advantage, taken control."
    mc.name "I... I could never have done something like that..."
    the_person "I know. For you to have the morals to do that."
    the_person "But beyond that, to be in this industry, to be in a position to actually help, and to make the pushes necessary to formulate the cure, and to give it to me."
    "[the_person.title] looks you right in the eye and delivers her judgement."
    the_person "It could have only been you. You saved me. And for that, I owe you everything."
    $ the_person.change_love(100, 100)
    mc.name "Don't be ridiculous, you don't owe me anything..."
    the_person "I know you feel that way. But it goes beyond that too. You have your flaws, sure. Every man has a vice. But you mean everything to me."
    if the_person.is_girlfriend():
        the_person "I know I've changed a lot, and you may not love me anymore, but I love you. I'm completely yours if you still want me."
    else:
        the_person "I know I've changed a lot, and I'm willing to be patient if you want me to. But I love you. I'm completely yours if you want me."
    "Wow, you hadn't anticipated this."
    mc.name "You mean... You aren't angry? For the times I was weak... Even though I should have known better... and took advantage of you?"
    "[the_person.title] begins to laugh."
    the_person "Took advantage... Of me? I... Did not estimate that you might be fearing reprisal. You really are too good to be true, aren't you?"
    "[the_person.title] stands up. You worry she is about turn and leave... But instead... She starts getting naked?"
    $ the_person.outfit.remove_random_upper()
    $ the_person.outfit.remove_random_lower()
    $ the_person.draw_person(position = "stand2")
    mc.name "That's... You don't have to do that..."
    $ mc.change_locked_clarity(20)
    the_person "I know. But I want to. Sir, I threw myself at you so many times, you never took advantage of me. Your restraint in everything has been incredible."
    the_person "No straight man could have resisted being exposed to the amount of sex appeal I was displaying without succumbing."
    "She continues to disrobe. You are mesmerized by the beautiful woman in front of you."
    $ the_person.outfit.remove_random_upper()
    $ the_person.outfit.remove_random_lower()
    $ the_person.draw_person(position = "stand2")
    the_person "Besides, even if my brains were scrambled, I still wanted it. And I enjoyed it. A LOT. But I know some part of you still doesn't believe me."
    $ mc.change_locked_clarity(50)
    the_person "So now, I'm going to show you. Actions speak louder than words."
    "She motions to you."
    the_person "Would you please get naked for me? I want to show you how much I loved it, and how much I STILL love your cock."
    the_person "I want you to just sit back, let me get on top of you, and fuck you."
    the_person "I want to have intercourse, and then I want to feel you orgasm, and deposit your semen inside me."
    "Wow... A scientific way of putting it, but also very effective. You pull your cock out while [the_person.title] finishes stripping."
    $ the_person.strip_outfit()
    "Her eyes are on you as she walks around the desk. You glance at your unlocked office door..."
    the_person "Don't worry, we won't get interrupted during this..."
    mc.name "Have you been monitoring my office traffic?"
    the_person "No. But I did put up your out to lunch sign and locked the door on my way in without you noticing..."
    $ mc.change_locked_clarity(30)
    $ the_person.draw_person(position = "cowgirl")
    "[the_person.title] gets up on top of you. Her eyes are making direct contact with yours as she takes your cock in one hand and starts to run you up and down her slit."
    "Her natural lubrication soon has you wet and ready for penetration."
    "She leans forward and closes her eyes. Your lips make contact and you begin to kiss. At the same time, she lifts her hips slightly, lines you up with her cunt, and slowly sinks down onto you."
    $ mc.change_locked_clarity(50)
    "Her tongue dances with yours as the first fledgling thrusts are made of her hips onto yours. Her kisses punctuated with moans."
    the_person "Mmm... You feel so good. I swear, every time we fuck is better than the last..."
    $ the_person.change_arousal(30)
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _meet_dr_candace_fuck_01
    "When you finish, she just stays on top of you for a bit. You can feel your seed dribble out of her for a bit, but she doesn't seem to care about the mess. She just holds on to you."
    the_person "Thank you. I needed that."
    mc.name "Yes. I admit I was being apprehensive, but that certainly, ermmm, eased my mind."
    the_person "It certainly is a very relaxing activity. When I was working on my thesis, I was calling up the poor guy I was seeing at the time all the time trying to de-stress."
    mc.name "Thesis? You mean... You have a doctorate?"
    the_person "Yes."
    mc.name "So... I should be calling you doctor [the_person.last_name]?"
    the_person "Ahh, let me just stop you right there. I would prefer things between us, and the girls here at the office, to remain more... Informal."
    "She sits back a bit and smiles."
    the_person "I'd prefer other titles. Candace is good, but what would be even better would be if you just called me... Your girlfriend..."
    mc.name "I might take issue with you getting busy with your landlord if we're gonna do this."
    "She chuckles before responding."
    the_person "You goof. With a cock as good as yours, I won't need anything else..."
    "After a moment she adds on to that."
    the_person "I would like to keep helping [starbuck.name] at the shop though... She's become a good friend."
    if the_person.is_girlfriend():
        "Well, it seems that [the_person.title] still has feelings for you and wants to continue being your girlfriend."
    else:
        "Well, in quite the reversal of roles, Candace has asked you out officially. Do you want to accept?"
        menu:
            "Accept":
                if not the_person.is_girlfriend():
                    $ the_person.add_role(girlfriend_role)
                mc.name "So, what is your degree in, anyway?"
                the_person "I received my doctorate for molecular biology and genetics... Though I'm not sure why that is relevant."
                mc.name "Oh, I just wanted to know for when I have to introduce you to people as 'my girlfriend Dr. [the_person.last_name]."
                $ the_person.change_happiness(15)
                $ the_person.change_love(5)
                the_person "Ahh! I suppose that would be okay... The first part anyway."
                "She leans back a bit and gets kinda dreamy eyed."
                the_person "You know, I truly had no idea if you were going to accept or not."
                mc.name "Yeah. I was on the fence myself, but then you rode me cowgirl while I was in my office chair."
                mc.name "I realized if we were dating I could call you in here anytime during the work day and do it again..."
                the_person "... You know I would do that even if we weren't dating, right?"
                "You give her a wink. You decide to get busy one more time before you move on for the day..."
                mc.name "Yeah but now I don't have to use the company punishment manual to do this either."
                $ mc.change_locked_clarity(20)
                "She gives a little yelp as you suddenly scoot your chair from your desk. You stand up, picking her up as you go, then turn her over and bend her over you desk."
                $ the_person.draw_person(position = "standing_doggy")
                mc.name "You've been one naughty doctor."
                the_person "Oh lord I like where this is going."
                mc.name "Getting yourself arrested? The cops thought you were a prostitute!"
                "With your harsh, but playful words you bring your hand down and smack her ass. It wobbles enticingly."
                $ the_person.change_arousal(10)
                $ mc.change_locked_clarity(20)
                the_person "Oh! I'm sorry boss!"
                mc.name "Going out and looking for some stranger to meet your needs... When I was here all along!"
                "You give her ass another spank."
                $ the_person.change_arousal(15)
                $ mc.change_locked_clarity(20)
                the_person "Ahh! I'm sorry, I won't do it again!"
                "A red handprint starts to appear on her rear, where you spanked her. You lighten you touch a bit and gently rub her ass, soothing it."
                mc.name "I know. Because you don't need to anymore. When you get those cravings, and it's just too much to bear, come and find me. I'll meet your needs, anytime, anywhere."
                the_person "Oh... That's amazing..."
                "She starts to wiggle her hips and giggle a little."
                the_person "Excuse me, boss? I think I'm feeling those 'needs' again!"
                $ mc.change_locked_clarity(50)
                "Her playful tone makes it obvious she is playing dumb a little, whereas just a few weeks ago, she would have said something similar to that, but being completely serious."
                "You let your fingers run their way down the inside of her cheeks, dipping them gently in her pussy. She's still soaking wet from when you fucked earlier."
                $ the_person.change_arousal(10)
                "[the_person.title] turns her head back to look at you. Are those puppy dog eyes?"
                the_person "Please, I need you again sir. Please!"
                "God damn no wonder she is so good at negotiating supply contracts, she knows just how to ask."
                "Your cock is rock hard and ready to seal the deal. It's time to fuck [the_person.title] properly now that you have everything out in the open."
                $ mc.change_locked_clarity(50)
                "Your grab her hips and move in close. She reaches between her legs and holds the tip of your erection, guiding you inside of her."
                "You easily bottom out inside of her in one smooth stroke. She groans at the sensations of being filled again."
                the_person "Okay... I'm done being cute. You can rough me up now!"
                "You reach up and grab her hair."
                mc.name "I think I'll do that."
                "Pulling her head back, you start to thrust yourself inside of her at a rapid pace. It's time to give it to her good!"
                call fuck_person(the_person,start_position = SB_doggy_standing, skip_intro = True, girl_in_charge = False, position_locked = True, skip_condom = True) from _fuck_doctor_candace_again_02
                "When you finish with her, [the_person.title] is sprawled out across your desk. Your light colored cum on her dark skin is a beautiful contrast."
                "You get yourself cleaned up a bit and looking presentable while she is still recovering."
                the_person "Oh fuck [the_person.mc_title]... Your dick is amazing..."
                "Her breathing is finally starting to slow down a bit."
                the_person "Are we, umm... We doing my place or yours tonight?"
                mc.name "Honestly, I'm not sure if I'll be able to tonight, but I'll let you know."
                the_person "Mmm... Okay... You go ahead... I think I would just like to bask a little..."
                "You consider for a moment getting a nice couch for your office..."
                "But then whenever you call a girl in they'd probably assume you were getting ready to make a cheap porno movie. Better not."
                mc.name "Rest up, I'm going to get back to work."
                "You leave your office. You feel great about how things have progressed with [the_person.possessive_title]."
            "Reject (disabled)":
                pass
    $ clear_scene()
    return

#Character variable wrappers
init 3 python:
    def candace_get_day_met():
        return candace.event_triggers_dict.get("day_met", -1)

    def candace_get_met_at_store():
        return candace.event_triggers_dict.get("met_at_store", 0)

    def candace_get_learned_about_unhappy():
        return candace.event_triggers_dict.get("learned_about_unhappy", 0)

    def candace_get_learned_about_bf_control():
        return candace.event_triggers_dict.get("learned_about_bf_control", 0)

    def candace_get_learned_about_previous_work():
        return candace.event_triggers_dict.get("learned_about_previous_work", 0)

    def candace_get_learned_about_uniform():
        return candace.event_triggers_dict.get("learned_about_uniform", 0)

    def candace_get_learned_about_pay():
        return candace.event_triggers_dict.get("learned_about_pay", 0)

    def candace_get_employees_have_lax_uniforms():
        return reduced_coverage_uniform_policy.is_active()

    def candace_get_mc_is_sexually_skilled():
        if (mc.sex_skills["Foreplay"] + mc.sex_skills["Oral"] + mc.sex_skills["Vaginal"] + mc.sex_skills["Anal"]) > 16 : #Average of 4 or better across sex skills.
            return True
        return False

    def candace_get_ready_to_quit():
        if candace.event_triggers_dict.get("relationship_doubt_score", 0) >= 5:
            return True
        return False

    def candace_get_can_convince_to_quit():
        if candace_get_ready_to_quit():
            if candace_get_learned_about_pay() and candace_get_learned_about_previous_work() and candace_get_learned_about_uniform() and candace_get_learned_about_bf_control():
                if candace_get_employees_have_lax_uniforms() or candace_get_mc_is_sexually_skilled():
                    return True
        return False

    def candace_get_has_quit_job():
        if "candace" in globals():
            return candace.event_triggers_dict.get("quit_job", 0) != 0
        return False

    def candace_can_talk():
        if "candace" in globals():
            return candace.event_triggers_dict.get("last_talk_day", 0) < day
        return False

    def candace_increase_doubt():
        score = candace.event_triggers_dict.get("relationship_doubt_score", 0)
        candace.event_triggers_dict["relationship_doubt_score"] = score + 1
        return

    def candace_get_has_gone_clothes_shopping():
        if "candace" in globals():
            return candace.event_triggers_dict.get("clothes_shopping", 0) != 0
        return False

    def candace_update_action_lists():  #This function is designed to try and bring action lists up to date, from update to update, so we don't have to start a new game every time.
        if candace_get_has_quit_job():
            if not candace_get_has_gone_clothes_shopping():
                candace.add_unique_on_talk_event(candace_goes_clothes_shopping)
        return

    def candace_is_giving_supply_discount():
        if candace.is_employee():
            if candace.event_triggers_dict.get("supply_discount_active", False) == True:
                return True
        return False

    def candace_calculate_discount():
        disc_mult = 1.0
        if "candace" in globals():
            if candace.is_employee():
                if candace_is_giving_supply_discount():
                    if candace_is_bimbo():
                        disc_mult = 0.90
                    else:
                        disc_mult = 0.80
        if mc.business.IT_project_is_active(supply_storage_project):
            disc_mult -= 0.05
        return disc_mult


    def candace_is_bimbo():
        if "candace" in globals():
            return candace.event_triggers_dict.get("is_bimbo", False)
        return False

    def candace_starbuck_are_friends():
        if "candace" in globals():
            return candace.event_triggers_dict.get("friends_with_starbuck", False)

    def candace_get_cure_day():
        if "candace" in globals():
            return candace.event_triggers_dict.get("cure_day", 9999)
        return 9999

    def candace_get_living_with_stephanie_day():
        if "candace" in globals():
            return candace.event_triggers_dict.get("living_with_stephanie", 9999)
        return 9999

    def candace_get_sex_record_difference_tier(): #Use this to determine what dialogue to run after curing her bimboism. Made a function because messy
        old_dict = candace.event_triggers_dict.get("sex_record_snapshot", None)
        if old_dict == None:
            return 0
        if old_dict["Vaginal Sex"] < candace.sex_record["Vaginal Sex"] or old_dict["Anal Sex"] < candace.sex_record["Anal Sex"]: #You fucked her at least once
            if old_dict["Vaginal Sex"] + old_dict["Anal Sex"] + 2 <= candace.sex_record["Vaginal Sex"] + candace.sex_record["Anal Sex"]: #Sex at least twice
                if old_dict["Vaginal Creampies"] + old_dict["Anal Creampies"] + 2 <= candace.sex_record["Vaginal Creampies"] + candace.sex_record["Anal Creampies"]:
                    return 4
                else:
                    return 3
            else:
                return 2
        if old_dict["Handjobs"] < candace.sex_record["Handjobs"] or old_dict["Blowjobs"] < candace.sex_record["Cunnilingus"] or old_dict["Cunnilingus"] < candace.sex_record["Blowjobs"]or old_dict["Fingered"] < candace.sex_record["Fingered"]:
            return 1
        return 0
