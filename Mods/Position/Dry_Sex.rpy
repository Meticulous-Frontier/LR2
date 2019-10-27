#Dry sex position. This position is my attempt at creating a bridge between kissing and missionary.
#This position will link itself dynamically with missionary if the girl's vagina becomes available. Otherwise no link is made.

init:
    python:
        dry_sex = Position("Dry Sex",30,55,"missionary","Lay","None","Vaginal",16,16,[],
        "intro_dry_sex",
        ["scene_dry_sex_1","scene_dry_sex_2"],
        "outro_dry_sex",
        "transition_default_dry_sex",
        "strip_dry_sex", "strip_ask_dry_sex",
        "orgasm_dry_sex",
        opinion_tags = ["missionary style sex","big dicks"])  #Lol I have no idea
        #list_of_positions.append(dry_sex)   #Disabled for now

# init 1:
#     python:
#         dry_sex.link_positions(piledriver,"transition_dry_sex_piledriver")

label intro_dry_sex(the_girl, the_location, the_object, the_round):
    $ the_clothing = None
    if the_girl.outfit.vagina_available():
        $ the_clothing = "pussy"
        $ dry_sex.link_positions(missionary,"transition_dry_sex_piledriver")
    else:
        $ the_clothing = the_person.outfit.get_lower_ordered()[-1].name
        $ dry_sex.transitions = []
        $ dry_sex.connections = []
    "You run your hands along [the_girl.title]'s hips, feeling the shape of her body."
    mc.name "I want you to lie down for me."
    "She nods and lies down on the [the_object.name], waiting while you climb on top of her."
    "[the_girl.possessive_title] wraps her arms around you and holds you close. Still in your underwear, you bring to rub your erection against her [the_clothing] between her legs."
    return

label scene_dry_sex_1(the_girl, the_location, the_object, the_round):
    $ the_clothing = None
    if the_girl.outfit.vagina_available():
        $ the_clothing = "pussy"
        $ dry_sex.link_positions(missionary,"transition_dry_sex_piledriver")
    else:
        $ the_clothing = the_person.outfit.get_lower_ordered()[-1].name
        $ dry_sex.transitions = []
        $ dry_sex.connections = []


    return

label scene_dry_sex_2(the_girl, the_location, the_object, the_round):
    # CHOICE CONCEPT: Pin her down // Kiss her
    $ the_clothing = None
    if the_girl.outfit.vagina_available():
        $ the_clothing = "pussy"
        $ the_clothing = the_person.outfit.get_lower_ordered()[-1].name
    else:
        $ the_clothing = the_person.outfit.get_lower_ordered()[-1]
        $ dry_sex.transitions = []
        $ dry_sex.connections = []


    return

label outro_dry_sex(the_girl, the_location, the_object, the_round):

    $ the_clothing = None
    if the_girl.outfit.vagina_available():
        $ the_clothing = "pussy"
    else:
        $ the_clothing = the_person.outfit.get_lower_ordered()[-1].name

    "You get to hear every little gasp and moan from [the_girl.title] as you're pressed up against her. Combined with the feeling of fucking her pussy it's not long before you're pushed past the point of no return."
    mc.name "I'm going to cum!"


    return

label transition_dry_sex_missionary(the_girl, the_location, the_object, the_round):
    "[the_girl.title]'s pussy feels so warm and inviting, you can't help but want to get deeper inside of her. You pause for a moment and reach down for her legs."
    the_girl.char "Hey, what's... Whoa!"
    "You pull her legs up and bend them over her shoulders. You hold onto her ankles as you start to fuck her again, pushing your hard cock nice and deep."
    return

label transition_default_dry_sex(the_girl, the_location, the_object, the_round):
    "You put [the_girl.title] on her back and lie down on top of her, lining your hard cock up with her tight cunt."
    "After running the tip of your penis along her slit a few times you press forward, sliding inside of her. She gasps softly and closes her eyes."
    return

label strip_dry_sex(the_girl, the_clothing, the_location, the_object, the_round):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = dry_sex.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
    "She lays back as you begin to rub against her again."
    if the_girl.outfit.vagina_available():
        $ dry_sex.link_positions(missionary,"transition_dry_sex_piledriver")
    return

label strip_ask_dry_sex(the_girl, the_clothing, the_location, the_object, the_round):
    the_girl.char "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.title] pants as you hump her."
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = dry_sex.position_tag)
            "You move back kneel for a moment while [the_girl.title] struggles out of her [the_clothing.name] and throws it to the side."
            "She lays back as you begin to rub against her again."
            if the_girl.outfit.vagina_available():
                $ dry_sex.link_positions(missionary,"transition_dry_sex_piledriver")
        "Leave it on.":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 80:
                the_girl.char "Do you think I look sexy in it?"
                "You speed up, humping her faster in response to her question."
            elif the_girl.sluttiness < 100:
                the_girl.char "Does it make me look like a good little slut? All I want to be is your good little slut sir."
                "She pushes her hips against yours and moans happily."
            else:
                the_girl.char "Does it make me look like the cum hungry slut that I am? That's all I want to be for you sir, your dirty little cum dumpster!"
                "She grinds her hips against you and moans ecstatically."
    return

label orgasm_dry_sex(the_girl, the_location, the_object, the_round):
    "[the_girl.title] turns her head and pants loudly. Suddenly she bucks her hips up against yours and gasps."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    "Her pussy is dripping wet as you fuck through her climax. She paws at the [the_object.name], trying to find something to hold onto."
    "After a few seconds she lets out a long sigh and all the tension drains out of her body. You slow down your thrusts to catch your own breath."
    the_girl.char "Don't stop [the_girl.mc_title], I might be able to get there again..."
    return
