# override existing mom breeding limited time action that uses the breeding position
# instead of the default missionary.

init 5 python:
    config.label_overrides["breeding_mom_intro_label"] = "breeding_mom_intro_label_enhanced"

label breeding_mom_intro_label_enhanced(the_person):
    $ the_person.apply_outfit(the_person.wardrobe.get_random_appropriate_underwear(the_person.sluttiness, guarantee_output = True))
    $ the_person.strip_outfit(exclude_upper = True, delay = 0)
    $ the_person.draw_person(position = "sitting")
    $ the_person.update_outfit_taboos()
    $ mc.change_locked_clarity(10)
    "You walk into [the_person.title]'s room and find her sitting on the edge of her bed, sexily dressed without any panties."
    if the_person.has_breeding_fetish():
        if the_person.knows_pregnant():
            "She is idly rubbing her belly. Your seed has already taken root there and a baby is growing."
            the_person "I was just thinking about... you know... the night where you knocked me up..."
            the_person "Do you want to re-enact it? It would be nice..."
        elif the_person.is_highly_fertile():
            the_person "Why don't you come here? I was just getting ready to come find you..."
            "She lowers her voice a bit."
            the_person "I'm pretty sure I'm fertile right now... and you know how bad I've been wanting you to knock me up!"
        return
    else:
        the_person "[the_person.mc_title], close the door, please. I have something I need to ask you."
        "You close the door to [the_person.possessive_title]'s bedroom and walk over to her bed."
        "She pats the bed beside her and you sit down."
        the_person "I've been thinking a lot about this. You're all grown up and [lily.fname] isn't far behind."
        the_person "Soon you'll both be leaving home, but I don't think I'm done being a mother yet."
        "She takes your hands in hers and looks passionately into your eyes."
        the_person "I want you to give me a child. I want you to breed me."

    if the_person.has_large_tits():
        "Her face is flush and her breathing rapid. Her [the_person.tits_description] heave up and down."
    else:
        "Her face is flush and her breathing rapid."
    $ mc.change_locked_clarity(50)

    menu:
        "Try to breed her":
            "You nod, and the mere confirmation makes her shiver. She lies down on the bed and holds out her hands for you."
            $ the_person.draw_person(position = "missionary")
            "You strip down and climb on top of her. The tip of your hard cock runs along the entrance of her cunt and finds it dripping wet."
            the_person "Go in raw [the_person.mc_title], enjoy my pussy and give me your cum!"
            $ mc.change_locked_clarity(20)
            $ the_person.break_taboo("vaginal_sex")
            $ the_person.break_taboo("condomless_sex")
            "She wraps her arms around your torso and pulls you tight against her. She gives you a breathy moan when you slide your cock home."
            the_person "Ah... Fuck me and give me your baby! I'll take such good care of it, just like I did for you and [lily.fname]!"
            call fuck_person(the_person, start_position = breeding_missionary, start_object = mc.location.get_object_with_name("bed"), skip_intro = True, position_locked = True, skip_condom = True) from _call_fuck_person_breeding_mom_enhanced_label
            $ the_report = _return #TODO: The creampie check should now be possible with the report system instead of checking her total record.
            if the_report.get("guy orgasms", 0) > 0 and the_person.has_creampie_cum():
                "You roll off of [the_person.possessive_title] and onto the bed beside her, feeling thoroughly spent."
                "She brings her knees up against her chest and tilts her hips up, holding all of your cum deep inside of her."
                mc.name "Do you think that did it?"

                if the_person.is_highly_fertile():
                    the_person "I don't know. It's the right time of the month."
                else:
                    the_person "Chances are not very high, but I'm still hopeful."

                $ the_person.change_stats(love = 2)

                "You lie together in silence. [the_person.possessive_title] rocks herself side to side. You imagine your cum sloshing around her womb."
                $ the_person.draw_person(position = "sitting")
                "Eventually she puts her legs down and the two of you sit up in bed."
                #TODO: Add an action where you can try and breed her some more.

            else:
                "You roll off of [the_person.possessive_title] and onto the bed beside her."
                $ the_person.change_happiness(-20)
                the_person "I'm sorry... I'm sorry I'm not good enough to make you cum. I'm not good enough to earn your child..."
                "She sounds as if she is almost on the verge of tears."
                "You wrap your arms around her and hold her close."
                mc.name "Shh... You were fantastic. It's me, I'm just not feeling it today. Maybe we can try some other day."
                the_person "I don't know, this might have all been a mistake. Let's just... be quiet for a while, okay?"
                $ the_person.draw_person(position = "sitting")
                "You hold [the_person.possessive_title] until she's feeling better, then sit up in bed with her."

        "Say no":
            $ the_person.draw_person(position = "sitting", emotion = "sad")
            "You shake your head. [the_person.title] looks immediately crestfallen."
            $ the_person.change_happiness(-20)
            the_person "But why..."
            mc.name "[the_person.title], I love you but I can't give you what you want."
            "She nods and turns her head."
            $ the_person.change_stats(love = -2)
            the_person "Of course... I was just being silly. I should know better."

    $ clear_scene()
    return
