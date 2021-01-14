# Use this file to store actions, crisis, and role related items that are going to be character specific or unique. May require single fetish or multiple
# Events in this file would be better added to specific roles

init -1 python:
    def fetish_mom_kitchen_requirement(the_person):
        if the_person.fetish_count() > 0:
            if person is mom and mc.location == kitchen:
                if mc.energy > 30:
                    return True
                else:
                    return "You're too tired for sex"
        return False


init 2 python:
    fetish_mom_kitchen = Action("Kitchen Sex (Fetish) {image=gui/heart/Time_Advance.png}", fetish_mom_kitchen_requirement, "fetish_mom_kitchen_label",
        menu_tooltip = "Indulge your mother's fantasies.")


label fetish_mom_kitchen_label(the_person):
    $ the_person = mom
    $ the_clothing = the_person.outfit.get_lower_top_layer() #Get the very top item of clothing.

    mc.name "Hey [the_person.title], dinner sure smells good. Just keep working on it, don't mind me!"
    "[the_person.possessive_title] hesitates for a second, clearly realizing you are up to something."
    "You pretend to look in the fridge for something as [the_person.possessive_title] resumes dinner preparations. She bends over the counter and starts to chop up some vegetables."
    $ the_person.draw_person(position = "standing_doggy")
    if the_person.outfit.vagina_available():
        "You steal a few glances over at [the_person.possessive_title]'s exposed ass. It looks soft and supple, and shakes a bit as she prepares dinner."
    else:
        "You steal a glance over at [the_person.possessive_title]'s ass as she is bent over. It looks great in her [the_clothing.name]."
    "Getting a naughty idea, you quietly move behind [the_person.possessive_title]."
    menu:
        "Fuck her ass" if the_person.has_anal_fetish():
            "You reach down and grope her ass aggressively."
            the_person.char "Hey! What are you doing? Stop that!"
            "You continue groping her. You give her ass a solid swat."
            mc.name "Stop? But doesn't that feel good, [the_person.title]?"
            the_person.char "Of course it does... But your sister, she could walk in anytime..."
            if the_person.outfit.vagina_available():
                mc.name "Shhh, just be quiet. Your ass looks so amazing [the_person.title]... I should just fuck it right here..."
            else:
                mc.name "Shhh, just be quiet. Your ass looks so good in your [the_clothing.name]... I should just pull it down and fuck you in the ass right here..."
            $ the_person.change_arousal(10)
            "[the_person.possessive_title] stifles a moan, she pushes her hips back against you as you continue to stroke her."
            the_person.char "Mmmmmm... Okay... Do it! Just go quick! I don't want your sister to catch us."
            if the_person.outfit.vagina_available():           #If its available no need to strip.
                "You quickly pull your cock out and begin to rub it between her cheeks."
            else:                                              #Otherwise, strip her down.
                "You don't bother to reply, instead you begin stripping away anything between you and her supple ass."
                $ the_person.strip_outfit(position = "standing_doggy", exclude_upper = True)
                "With her ass finally exposed you waste no time. You quickly pull your cock out and rub it between her cheeks."
            "[the_person.possessive_title] pulls some lube out of one of the kitchen drawers."
            mc.name "Wait... you keep lube in the...?"
            the_person.char "Shut up just fuck me before your sister notices!"
            "You rub some lube on your cock and on [the_person.title]'s ass hole. You grab her by the hips and then roughly pull her back until your cock is buried inside her rump."
            call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_table(), skip_intro = True) from _call_sex_description_SBR40
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title] is positively glowing. She knows that even while preparing dinner, you may come and fuck her ass at any time."
            else:
                "[the_person.possessive_title] remains silent. She knows that even while preparing dinner, you may come use her ass for your pleasure at any time."

            $ the_person.event_triggers_dict["LastAnalFetish"] = day
        "Fuck her ass\n{color=#ff0000}{size=18}Requires Anal Fetish{/size}{/color} (disabled)" if not the_person.has_anal_fetish():
            pass
        "Creampie her" if the_person.has_breeding_fetish():
            if the_person.outfit.vagina_available():
                "You slowly reach down and start to slowly caress her cunt."
            else:
                "You slowly reach down and start to slowly rub her pussy through her [the_clothing.name]."
            the_person "Hey! What are you doing? Stop that!"
            "You continue rubbing her."
            mc.name "Stop? But doesn't that feel good, [the_person.title]?"
            the_person "Of course it does... But your sister, she could walk in anytime..."
            mc.name "You know you want a pussy full of my cum. Feel it dripping out of your fertile cunt all through dinner time."
            the_person "Yes I know but..."
            if the_person.outfit.vagina_available():
                "Shhh, just be quiet. Your ass looks so amazing [the_person.title]... I should just fuck you right here..."
            else:
                "Shhh, just be quiet. Your ass looks so good in your [the_clothing.name]... I should just pull it down and fuck you right here..."
            $ the_person.change_arousal(10)
            "[the_person.possessive_title] stifles a moan, she pushes her hips back against you as you continue to stroke her."
            the_person "Mmmmmm... Okay... Do it! Just go quick! I don't want your sister to catch us."
            if the_person.outfit.vagina_available():           #If its available no need to strip.
                "You quickly pull your cock out and line it up with her wet slit."
            else:                                              #Otherwise, strip her down.
                "You don't bother to reply, instead you begin stripping away anything between you and her delicious pussy"
                $ the_person.strip_outfit(position = "standing_doggy", exclude_upper = True)
                "With her pussy finally exposed you waste no time. You quickly pull your cock out and line it up with her wet slit."
            call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_table(), skip_intro = True) from _call_sex_mom_kitchen_breeding_01
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title] is positively glowing. She knows that even while preparing dinner, you may come and fuck her at any time."
            else:
                "[the_person.possessive_title] remains silent. She knows that even while preparing dinner, you may come use her for your pleasure at any time."

            $ the_person.event_triggers_dict["LastBreedingFetish"] = day
        "Creampie her\n{color=#ff0000}{size=18}Requires Breeding Fetish{/size}{/color} (disabled)" if not the_person.has_breeding_fetish():
            pass
        "Cover her in cum\n{color=#ff0000}{size=18}Not yet written{/size}{/color} (disabled)" if the_person.has_cum_fetish():
            pass #TODO
        "Cover her in cum\n{color=#ff0000}{size=18}Requires Cum Fetish{/size}{/color} (disabled)" if not the_person.has_cum_fetish():
            pass
        "Fuck her loudly" if the_person.has_exhibition_fetish():
            "You reach down and slap her ass aggressively. It makes a loud slapping noise."
            the_person.char "Hey! What are you doing? Stop that!"
            mc.name "Stop? But doesn't that feel good, [the_person.title]?"
            "You don't bother to wait for a reply. You give her multiple hard spanks. The sound of your hand slapping her buttocks echoes through the room."
            "You hear your sister call out from the living room."
            lily "You okay in there mom?"
            the_person "Yes dear! I'm just... you knowing... chopping some vegetables!"
            "You give her ass another hard spank, as if to punctuate her remark. [the_person.possesive_title] is barely able to stifle her moan."
            $ the_person.change_arousal(15)
            "Barely whispering, [the_person.possesive_title] tries to resist, but you can tell this is really turning her on."
            the_person "Your sister, she's going to..."
            if the_person.outfit.vagina_available():
                mc.name "Shhh, just be quiet. Your ass looks so amazing [the_person.title]... I should just fuck you right here..."
            else:
                mc.name "Shhh, just be quiet. Your ass looks so good in your [the_clothing.name]... I should just pull it down and fuck you right here..."
            mc.name "Besides, would it really be that bad if she caught us? I bet you'd like it if she came in and watched, wouldn't you."
            $ the_person.change_arousal(15)
            "[the_person.possessive_title] stifles a moan, she pushes her hips back against you so you give her another round of spanks."
            the_person "Oh god... Do it! Just go quick."
            mc.name "If I fuck you fast, it might get kinda noisy in here."
            the_person "I don't care! Just do it!"
            if the_person.outfit.vagina_available():           #If its available no need to strip.
                "You quickly pull your cock out and line it up with her wet slit."
            else:                                              #Otherwise, strip her down.
                "You don't bother to reply, instead you begin stripping away anything between you and her delicious pussy"
                $ the_person.strip_outfit(position = "standing_doggy", exclude_upper = True)
                "With her pussy finally exposed you waste no time. You quickly pull your cock out and line it up with her wet slit."
            "You thrust yourself inside of her slowly. Her pussy accepts your length easily, well lubricated from your spanking."
            $ the_person.change_arousal(15)
            $ mc.change_arousal(15)
            "You don't waste anytime and being to fuck her roughly. The sound of her ass cheeks clapping with each thrust fills the room."
            lily "Are you sure you're okay mom? That doesn't sound like vegetables."
            the_person "I'm sure! I'm not chopping vegetables anymore... I'm... oh god... I'm... beating meat!"
            "You try to stifle a laugh."
            lily "Beating...meat?"
            the_person "I mean... tenderizing it! You have to really spank... I mean... smack it hard to get it tender!"
            "You give her ass a solid spank."
            $ the_person.change_arousal(20)
            lily "You sure you don't want some help?"
            the_person "No! I mean... your brother is in here giving me a hand... there's a LOT of meat to tenderize... it might take us a while!"
            "Holy shit she is actually gonna sell that."
            lily "Well... okay, if you're sure."
            "You take the opportunity now to pick up the pace. You are really giving it to [the_person.possesive_title] now."
            call fuck_person(the_person, start_position = SB_doggy_standing, start_object = make_table(), skip_intro = True) from _call_sex_mom_kitchen_loud_sex_01
            $ the_report = _return
            $ the_person.event_triggers_dict["LastExhibitionFetish"] = day
        "Fuck her loudly\n{color=#ff0000}{size=18}Requires Exhibitionist Fetish{/size}{/color} (disabled)" if not the_person.has_exhibition_fetish():
            pass
    "Clearly, in her current attire, it will be obvious what [the_person.possesive_title] has been up to. You look at the state of dinner. Its almost done."
    mc.name "You go clean yourself up. I'll finish preparing dinner."
    "Ahhh... okay... thank you honey!"
    $ clear_scene()
    "[the_person.title] leaves the room, leaving you a lone with dinner. You start portioning out plates."
    menu: #Copy the normal dinner time serum screen.
        "Add serum to Mom's food":
            call give_serum(mom) from _call_give_mom_kitchen_fetish_01
        "Leave Mom's food alone":
            pass
    menu:
        "Add serum to [lily.name]'s food":
            call give_serum(lily) from _call_give_mom_kitchen_fetish_02
        "Leave [lily.name]'s food alone":
            pass
    if hall.has_person(aunt):
        menu:
            "Add serum to [aunt.name]'s food":
                call give_serum(aunt)from _call_give_mom_kitchen_fetish_03
            "Leave [aunt.name]'s food alone":
                pass
    if hall.has_person(cousin) or lily_bedroom.has_person(cousin):
        menu:
            "Add serum to [cousin.name]'s food":
                call give_serum(cousin) from _call_give_mom_kitchen_fetish_04
            "Leave [cousin.name]'s food alone":
                pass
    "Just as you are finishing up with plating the food, when [the_person.possesive_title] walks back into the kitchen."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    the_person "Thank you [the_person.mc_title]... for finishing dinner and... you know..."
    "[the_person.possesive_title] gives you a kiss on the cheek."
    "You bring the food out and have a nice family dinner together."
    call advance_time from _call_advance_time_kitchen_mom_fetish_time_01
    return
