#Attempt at writing an alternate scene for nora to be introduced in the game if the player uses the bimbo serum.
init 5 python:
    add_label_hijack("normal_start", "alternate_nora_intro_mod_core")
    add_label_hijack("after_load", "alternate_nora_intro_mod_core")

label alternate_nora_intro_mod_core(stack):
    python:
        alternate_nora_intro_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

init 2 python:
    def alternate_nora_intro_requirement():
        if mc.business.research_tier >= 2:
            if university.visible:  # make sure crisis is run and removed
                return True
            if mc.business.is_open_for_business():
                if mc.location != mc.business.r_div:
                    if renpy.random.randint(0,100) < 30:
                        return True
        return False

    def alternate_nora_intro_mod_initialization():
        alternate_nora_intro_action = Action("Nora contacts you", alternate_nora_intro_requirement, "alternate_nora_intro_label")
        mc.business.add_mandatory_crisis(alternate_nora_intro_action)
        return

label alternate_nora_intro_label():
    if university.visible == True:   #TODO find a better condition for when to nope tf out of this label
        return
    $ the_person = mc.business.head_researcher
    $ scene_manager = Scene()
    $ mc.start_text_convo(the_person)
    if the_person == stephanie:
        the_person "[the_person.mc_title]! Get down to the lab! You won't believe who is down here."
    else:
        the_person "Hey, I have someone down here in the lab looking for you specifically. Can you please come down?"
    mc.name "I'm on my way right now!"
    $ mc.end_text_convo()
    "You quickly make your way down to the lab."
    $ mc.change_location(rd_division)
    $ mc.location.show_background()
    "When you get there, lo and behold, its your former professor, [nora.title]!"
    $ scene_manager.add_actor(nora, display_transform = character_center_flipped)
    $ scene_manager.add_actor(the_person)
    mc.name "Wow, [nora.title]? What a surprise!"
    nora "I know! I am rather surprised to see you here as well."
    nora "Some of the groups in my research circle posted some inquiries about a serum sample they had acquired that had some incredible properties!"
    nora "When they tracked the manufacture of the chemical to this town, they messaged me and said I should go check the lab out."
    if the_person == stephanie:
        nora "So when I get here, out in the parking lot, who do I see walking in? My old student [the_person.name]!"
        the_person "When I saw her, and she told me what she was doing here, I had to get a hold of you!"
    else:
        nora "So when I get to the front office and I ask who runs the place, what do they tell me? My old student!"
    mc.name "It is certainly good to see you. Yes, we are making some incredible strides here, especially recently."
    "You catch up with [nora.title] for a bit, but soon it is obvious she is here on more than just a friendly visit."
    nora "So. Out at the university, we are overwhelmed with the amount of research that needs to be done, and we are looking to outsource some of it."
    "She pulls out a folder and holds it out to you."
    nora "If you can manufacture and research information on the trait I provide you I can pay a bounty of $2000. I may also be able to provide another trait for you to study."
    nora "Do you find this acceptable?"
    "You think the offer over. It's a good amount of money for the amount of work, as long as you have someone to test these serums on."
    mc.name "I can make that work."
    nora "Glad to hear it! When you finish, I'll be over at the university in my lab. You remember how to get there, don't you?"
    mc.name "I do, yes."
    nora "Great! I look forward to hearing from you, and working with you more in the future."
    if the_person == stephanie:
        nora "And [the_person.name], it is so good to see you. We should catch up sometime, okay?"
        the_person "Sounds great!"
    $ scene_manager.clear_scene()
    "[nora.title] leaves and you make your way to your office to look over the folder she gave you."
    $ mc.change_location(office)
    $ mc.location.show_background()
    "The notes contain creation instructions for an unknown serum. She is looking for you to manufacture and test it."
    "You should bring it up to at least mastery level 2 before you go back to [nora.title]."

    #The magic sauce. Try to replicate all the variables here that are set in vanilla nora encounters.
    $ mc.business.event_triggers_dict["intro_nora"] = False

    $ the_trait = get_random_from_list(list_of_nora_traits)
    $ the_trait.researched = True
    $ mc.business.event_triggers_dict["nora_trait_researched"] = the_trait  #We can probably skip this
    $ list_of_traits.append(the_trait)
    $ del the_trait

    $ nora.set_schedule(university, days=[0, 1, 2, 3, 4], times =[1,2,3])
    $ nora.set_schedule(university, days=[5], times =[1,2])

    $ add_nora_university_research_actions()

    $ mc.business.event_triggers_dict["nora_cash_research_trait"] = mc.business.event_triggers_dict.get("nora_trait_researched")
    $ mc.business.event_triggers_dict["nora_trait_researched"] = None

    $ add_nora_research_cash_action(nora)

    return
