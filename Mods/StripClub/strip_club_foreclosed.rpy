## Stripclub storyline Mod by Corrado
#  You find the stripclub foreclosed.
#   foreclosed_stage = 1 Talk with Starbuck
#   foreclosed_stage = 2 Think about buying
#   foreclosed_stage = 3 Buy the club
#   foreclosed_stage = 4 Stripclub: bought - select old strippers
#   foreclosed_stage = 5 Stripclub: foreclosed finished
#   foreclosed_stage = -1 Stripclub new other owner

init 2 python:
    def init_strip_club_mod(action_mod):
        mc.business.event_triggers_dict["foreclosed_stage"] = 0
        mc.business.event_triggers_dict["foreclosed_last_action_day"] = 0
        mc.business.event_triggers_dict["old_strip_club_owner"] = None
        mc.business.event_triggers_dict["old_strip_club_name"] = None
        mc.business.event_triggers_dict["strip_club_decision_day"] = 0
        mc.business.event_triggers_dict["strip_club_has_bdsm_room"] = False
        return

    def get_strip_club_foreclosed_stage():
        return mc.business.event_triggers_dict.get("foreclosed_stage", 0)

    def set_strip_club_foreclosed_stage(value):
        mc.business.event_triggers_dict["foreclosed_last_action_day"] = day
        mc.business.event_triggers_dict["foreclosed_stage"] = value
        return

    def strip_club_is_closed():
        return __builtin__.len(stripclub_strippers) == 0 or (get_strip_club_foreclosed_stage() > 0 and get_strip_club_foreclosed_stage() < 5)

    def get_strip_club_foreclosed_last_action_day():
        return mc.business.event_triggers_dict.get("foreclosed_last_action_day", 0)

    def strip_club_foreclosed_event_requirement():
        if get_strip_club_foreclosed_stage() != 0:
            return False
        if sarah.event_triggers_dict.get("epic_tits_progress", 0) == 1: # don't start while Sarah epic tits event in progress
            return False
        if mc.business.funds > 60000:
            if time_of_day > 2:
                if cousin.event_triggers_dict.get("seen_cousin_stripping", False) == True and cousin.event_triggers_dict.get("blackmail_level", -1) >= 2:
                    return True
        return False

    def cousin_talk_about_strip_club_requirement(person):
        if not person.location() in [cousin_bedroom]:
            return True
        return False

    def starbuck_talk_about_strip_club_requirement(person):
        if get_strip_club_foreclosed_stage() == 1:
            if day > get_strip_club_foreclosed_last_action_day() + 2:
                return True
        return False

    def strip_club_foreclosed_change_stripper_schedules():
        for person in stripclub_strippers:
            if person.is_employee():
                person.set_schedule([0, 4], person.home)
            else:
                person.set_schedule([1,2,3], None)
                person.set_schedule([0, 4], person.home)
        return

    def add_cousin_talk_about_strip_club_action():
        cousin_talk_about_strip_club_action = Action("Cousin talk about strip club", cousin_talk_about_strip_club_requirement, "cousin_talk_about_strip_club_label")
        cousin.add_unique_on_room_enter_event(cousin_talk_about_strip_club_action)
        return

    def add_starbuck_talk_about_strip_club_action():
        starbuck_talk_about_strip_club_action = Action("Starbuck talk about strip club", starbuck_talk_about_strip_club_requirement, "starbuck_talk_about_strip_club_label")
        starbuck.add_unique_on_room_enter_event(starbuck_talk_about_strip_club_action)

    strip_club_foreclosed_mod_action = ActionMod("Strip Club Story Line", strip_club_foreclosed_event_requirement, "club_foreclosed_event_label",
        menu_tooltip = "At a certain point the strip club is closed and you get the chance to buy it.", category = "Misc", 
        initialization = init_strip_club_mod, is_mandatory_crisis = True, crisis_weight = 5)


label club_foreclosed_event_label():
    python:
        mc.business.event_triggers_dict["old_strip_club_owner"] = strip_club_owner
        mc.business.event_triggers_dict["foreclosed_day"] = day
        mc.business.event_triggers_dict["old_strip_club_name"] = strip_club.formalName
        strip_club_owner = "Foreclosed"
        strip_club.name = "Foreclosed"
        strip_club.formalName = "Foreclosed"
        strip_club.remove_action(strip_club_show_action)
        strip_club.background_image = Image(get_file_handle("Club_Outside_Background.jpg")) # Till the club doesn't open back again this should be the background
        strip_club_foreclosed_change_stripper_schedules()
        add_cousin_talk_about_strip_club_action()
    
    "While reading a newspaper you find out that your favorite Strip Club is no longer in business."
    "Perhaps you should talk to your cousin Gabrielle about it, when your aunt cannot overhear your conversation."
    return

label cousin_talk_about_strip_club_label(the_person):
    $ the_person.draw_person(emotion = "sad")
    the_person.char "Oh, [mc.name]... Just the last person I wanted to see right now!"
    mc.name "Hello, [the_person.title]... What's with the long face?"
    the_person.char "I think I just lost my job, the Club has been foreclosed and nobody knows if and when it would be open again..."
    mc.name "Any idea about what happened?"
    the_person.char "For sure I don't know, but I heard some rumours about a lot of unpaid taxes..."
    mc.name "The business was in that much trouble?"
    $ name_string = mc.business.event_triggers_dict.get("old_strip_club_owner", "that cheap fuck")
    the_person.char "Actually the business was running very well, but looks like [name_string], the boss there, just disappeared a few days ago with all the Club's money..."
    the_person.char "That fucking asshole didn't even pay me nor the other girls for our last week."
    "She looks at you and suddenly shifts her demeanor."    
    $ the_person.draw_person(emotion = "happy", position = "stand2")
    the_person.char "Oh, speaking about money, can you lend me 300 bucks?"
    the_person.char "I could do a special performance just for you, you know..."
    menu:
        "Accept":
            mc.name "Ok, follow me..."
            "You and [the_person.title] walks to the nearest hotel."
            $ amount = 300
            $ the_person.change_stats(happiness = 10, obedience = -3, love = 2)
            call club_foreclosed_strip_label(the_person) from _call_cousin_talk_about_strip_club_label_1
        "Refuse":
            mc.name "Actually I wanted to relax and have some fun tonight, but spending time with you and your poisoned tongue isn't exactly my idea of 'fun'..."
            mc.name "Bye, [the_person.title]... See you next time !"
            $ the_person.change_stats(happiness = -5, obedience = 2, love = -2)
            $ the_person.draw_person(position = "walking_away")
            "Hit and sunk by your behavior, [the_person.title] leaves you alone."
        "Mock":
            mc.name "Can you explain WHY I need to spend $300 on you stripping when there's plenty of other girls around willing to do far more for less money?"
            the_person.char "So you are a pervert, and stingy too ? Ok [mc.name], just for you I'll do it for $200..."
            $ the_person.change_stats(happiness = -3, obedience = 1, love = -1)
            menu:
                "Accept":
                    mc.name "Perhaps I should say no..."
                    the_person.char "Come on, take me to a nice hotel and I'll show you a good time."
                    mc.name "Alright, lets go."
                    "You and [the_person.title] walks to the nearest hotel."
                    $ amount = 200
                    $ the_person.change_stats(happiness = 5, obedience = -1, love = 1)
                    call club_foreclosed_strip_label(the_person) from _call_cousin_talk_about_strip_club_label_2
                "Refuse":
                    mc.name "Actually I wanted to relax and have some fun tonight, but spending time with you and your poisoned tongue isn't exactly my idea of 'fun'..."
                    mc.name "Bye, [the_person.title]... See you next time !"
                    $ the_person.change_stats(happiness = -5, obedience = 2, love = -2)
                    $ the_person.draw_person(position = "walking_away")
                    "Taken aback by your behavior, [the_person.title] turns around and sulks away, leaving you alone."

    $ set_strip_club_foreclosed_stage(1)
    $ add_starbuck_talk_about_strip_club_action()
    $ clear_scene()
    return

label club_foreclosed_strip_label(the_person):
    $ mc.change_location(downtown_hotel)
    $ mc.location.show_background()
    mc.name "Ok, here's your money, now lets get this show started."
    $ mc.business.change_funds(-amount)
    "[the_person.possessive_title] quickly disappears into the bathroom to change her clothes."
    $ the_person.apply_outfit(stripclub_wardrobe.pick_random_outfit())
    $ the_person.draw_person(emotion = "default", position = "stand4")
    the_person.char "You're in luck I really need the money, otherwise I would never do this for you."
    menu:
        "Give up":
            "On second though, you decide to stop her."
            mc.name "Enough! I know how desperate for money you are, [the_person.title]."
            $ the_person.draw_person(emotion = "sad", position = "stand4")
            "She think she just lost her opportunity to gain some cash and looks disheartened..."
            mc.name "Despite your usual attitude, I'll let you keep the money I gave you and I'll add $100 more...because if you believe it or not, but family matters to me."
            $ mc.business.change_funds(-100)
            "When you give her another $100, you can see the puzzled look on her face, she can't believe what's happening..."
            $ the_person.draw_person(emotion = "happy", position = "stand4")
            the_person.char "Really? I never got cash this easily!"
            the_person.char "Ok, you're a pervert, but I admit you're a generous pervert!"
            $ the_person.change_stats(happiness = 5, obedience = -1, love = 2)
            $ clear_scene()
            "It looks like [the_person.title] is her usual obnoxious self again... a moment later she's back in the bathroom changing her clothes."
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(emotion = "happy", position = "stand4")
            "When she's back, she moves right up to you."
            $ the_person.draw_person(emotion = "happy", position = "kissing")
            the_person.char "I still don't like you, but I think you deserve at least a kiss!"
            "She leans forward and gives you a soft kiss on your lips."
            if the_person.has_taboo("kiss"):
                $ the_person.break_taboo("kiss")
                $ the_person.change_arousal(15)
            else:
                $ the_person.change_arousal(10)
            $ the_person.draw_person(position = "walking_away")
            "Happily [the_person.title] turns around leaving the room, closing the door behind her."
            $ clear_scene()

        "Let's start":
            mc.name "Enough chit chat [the_person.title], less talking and more stripping!"
            $ the_person.draw_person(position = "back_peek")
            "[the_person.title] turns on some sexy music on her phone and looks at you unsure about how far she should let the show go."
            if the_person.effective_sluttiness() < 30:
                "[the_person.title] stop moving and start to look at the floor."
                the_person.char "Do you really want me to strip for you ?"
                $ the_person.draw_person(emotion = "sad", position = "stand4")
                the_person.char "I need the money and I would do it for anybody else, but you're my cousin, we're related..."
                the_person.char "I'm sorry [the_person.title], I can't do it..."
                mc.name "What if I give you $100 more than what we agreed?"
                $ the_person.draw_person(emotion = "default", position = "stand4")
                $ mc.business.change_funds(-100)
                $ the_person.add_situational_slut("desperate", 20, "She is desperate for cash.")

            "You hand over the cash and [the_person.title] stares at you for a moment, sighs and slowly start to dance for you."
            if the_person.effective_sluttiness("underwear_nudity") <= 20: # She only wants to show her underwear.
                if the_person.outfit.wearing_bra(): # If she's wearing a bra strip down to it.
                    while the_person.outfit.bra_covered():
                        $ the_item = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
                        $ the_person.draw_animated_removal(the_item)
                        "[the_person.possessive_title] takes off her [the_item.display_name]."
                else: #She's not wearing a bra and doesn't want you to see her tits.
                    "[the_person.title] seems nervous and plays with her shirt."
                    mc.name "What's wrong?"
                    the_person.char "I don't have a bra on... I can't take this off."
                    mc.name "Come on, you know the deal."
                    $ the_person.change_stats(happiness = -5, obedience = 2)

                if the_person.outfit.wearing_panties(): # If she's wearing a panties strip down to it.
                    while the_person.outfit.panties_covered():
                        $ the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
                        $ the_person.draw_animated_removal(the_item)
                        "[the_person.possessive_title] now takes off the [the_item.display_name]."
                else: #She's not wearing panties and doesn't want you to see her pussy.
                    the_person.char "I'm not wearing any panties right now. That means I can't take this off."
                    mc.name "Come on, that's not what the deal is."
                    the_person.char "Sad you don't get to see my tight, wet pussy [the_person.mc_title]?"
                    "She laughs and shakes her head."
                    the_person.char "Deal with it. Go cry to mommy if it matters that much to you."

                $ the_person.draw_person(position = "back_peek")

                if the_person.outfit.wearing_panties() and the_person.outfit.wearing_bra():
                    "Once [the_person.possessive_title] has stripped down to her underwear, she turns around to let you look at her ass."
                else:
                    "Once [the_person.possessive_title] has stripped down as far as she's willing, she turns around to let you look at her ass."
                the_person.char "Are you happy now ? I bet you're about to cream your fucking pants looking at this."
                "You take a second to enjoy the view."
                mc.name "Alright, that'll do."
                the_person.char "Finally... Pervert!"
                $ clear_scene()
                "A moment later she's back in the bathroom changing her clothes again."
                $ the_person.update_outfit_taboos()
                $ the_person.apply_planned_outfit()
                $ the_person.change_slut_temp(10)
                $ the_person.draw_person(emotion = "happy", position = "stand4")
                the_person.char "Thank you for the money, see you!"
                $ the_person.draw_person(position = "walking_away")
                "Happily [the_person.title] leaves the room and closes the door behind her."
            elif the_person.effective_sluttiness("bare_tits") <= 40: # She'll show tits and panties.
                while not the_person.outfit.tits_visible(): # If she's wearing a top strip it down.
                    $ the_item = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
                    $ the_person.draw_animated_removal(the_item)
                    if the_person.outfit.tits_visible():
                        "[the_person.possessive_title] takes off her [the_item.display_name] slowly, teasing you as she frees her tits."
                        if the_person.has_taboo("bare_tits"):
                            the_person.char "God, I can't believe you're going to see my tits. You're a fucking dick of a cousin, you know that?"
                            mc.name "Whatever. Pull those girls out so I can have a look."
                            the_person.char "I don't know why my Mom likes you... Fine."
                            $ the_person.break_taboo("bare_tits")
                    else:
                        "[the_person.possessive_title] takes off her [the_item.display_name]."
                if the_person.outfit.wearing_panties():
                    while the_person.outfit.panties_covered():
                        $ the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
                        $ the_person.draw_animated_removal(the_item)
                        "[the_person.possessive_title] takes off her [the_item.display_name]."
                else:
                    the_person.char "I'm not wearing any panties right now. That means I can't take this off."
                    mc.name "Come on, that's not what the deal is."
                    the_person.char "Sad you don't get to see my tight, wet pussy [the_person.mc_title]?"
                    "She laughs and shakes her head."
                    the_person.char "Deal with it. Go cry to mommy if it matters that much to you."
                $ the_person.draw_person(position = "back_peek")
                if the_person.outfit.wearing_panties():
                    "Once [the_person.possessive_title] has stripped down to her panties, she turns around to let you look at her ass."
                else:
                    "Once [the_person.possessive_title] has stripped down, she turns around to let you look at her ass."
                the_person.char "Are you happy now? I bet you're about to cream your fucking pants looking at this."
                "You take a second to enjoy the view."
                mc.name "Alright, that'll do."
                the_person.char "Finally... Pervert!"
                $ clear_scene()
                "A moment later she's back in the bathroom changing again her clothes."
                $ the_person.update_outfit_taboos()
                $ the_person.apply_planned_outfit()
                $ the_person.change_slut_temp(10)
                $ the_person.draw_person(emotion = "happy", position = "stand4")
                the_person.char "Thank you for the money, see you!"
                $ the_person.draw_person(position = "walking_away")
                "Happily [the_person.title] leaves the room and closes the door behind her."
            else: #She'll get completely naked.
                while not the_person.outfit.tits_visible():
                    $ the_item = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
                    $ the_person.draw_animated_removal(the_item)
                    if the_person.outfit.tits_visible():
                        "[the_person.possessive_title] takes off her [the_item.display_name] slowly, teasing you as she frees her tits."
                        if the_person.has_taboo("bare_tits"):
                            the_person.char "God, I can't believe you're going to see my tits. You're a fucking dick of a cousin, you know that?"
                            mc.name "Whatever. Pull those girls out so I can have a look."
                            the_person.char "I don't know why my Mom likes you... Fine."
                            $ the_person.break_taboo("bare_tits")
                    else:
                        "[the_person.possessive_title] takes off her [the_item.display_name]."
                while not the_person.outfit.vagina_visible(): # Strip down completely naked.
                    $ the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
                    $ the_person.draw_animated_removal(the_item)
                    if the_person.outfit.vagina_visible():
                        "[the_person.possessive_title] peels off her [the_item.display_name], slowly revealing her cute little pussy."
                        if the_person.has_taboo("bare_pussy"):
                            "[the_person.title] pauses and takes a deep breath."
                            mc.name "What's the hold up?"
                            the_person.char "Nothing! I though you would have chickened out by now, but whatever."
                            $ the_person.break_taboo("bare_pussy")
                    else:
                        "[the_person.possessive_title] takes off her [the_item.display_name]."
                the_person.char "There, are you satisfied?"
                $ the_person.draw_person(position = "back_peek")
                "She spins on the spot, letting you get a look at her ass."
                the_person.char "I know you like my ass, I bet you're about to cream your fucking pants looking at this."
                "You take a second to enjoy the view."
                mc.name "You're right, I like your ass!"
                $ the_person.draw_person(position = "stand4")
                the_person.char "Pervert!"
                $ clear_scene()
                "A moment later she's back in the bathroom changing again her clothes."
                $ the_person.update_outfit_taboos()
                $ the_person.apply_planned_outfit()
                $ the_person.change_slut_temp(10)
                $ the_person.draw_person(emotion = "happy", position = "stand4")
                the_person.char "Thank you for the money, see you!"
                $ the_person.draw_person(position = "walking_away")
                "Happily [the_person.title] leaves the room and closes the door behind her."

            $ the_person.clear_situational_slut("desperate")

    $ the_item = None
    $ the_person.review_outfit()
    $ clear_scene()
    return
