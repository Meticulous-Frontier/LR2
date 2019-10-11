# Dirty Laundy crisis by Starbuck!
# Scene: You go to do your laundry before bed, but notice your sister / mom has clean clothes stacked next to the dryer.
# Player has option to masturbate into clean panties and put them back.
# 50% chance mom or sister catches MC in the act. TODO higher chance at higher sluttiness? 50/50? Have cum soaked panties have some kind of effect on the person?
# Zero sluttiness they get angry, gives chance for obedience check?
# Low sluttiness they watch and touch themselves
# Mid sluttiness they give MC a handjob with the panties in their hand
# high sluttiness they put the panties on and have MC cum in the panties while they wear them

init -1 python:
    dirty_laundry_weight = 0  #Disable for now

init 2 python:
    def dirty_laundry_requirement():
        if mc_asleep():
            if mc_at_home():
                return True
        return False
    #
    # dirty_laundry_action = ActionMod("Dirty Laundry", dirty_laundry_requirement, "dirty_laundry_action_label",
    #     menu_tooltip = "Start your laundry before bed.", category = "Home", is_crisis = True, crisis_weight = dirty_laundry_weight)

label dirty_laundry_action_label:

    $ the_person = get_random_from_list(people_in_mc_home())
    $ the_panties = get_random_from_list(people_in_mc_home())

    "You are just drifting off to sleep when you suddenly you remember. You don't have any clean clothes for tomorrow!"
    "You look a the clock. It is already pretty late. You guess that your family is already asleep, so you grab your laundry and take it to the laundry room just wearing your boxers."
    "You throw your laundry in the washing machine, add some detergent and start it up."
    "As you are thinking about what to do for the next 30 minutes while the washer runs and you can move your clothes to the dryer, you notice a laundry basket on the floor filled with clean, folded clothes."
    "It looks like they all belong to [the_panties.title]. Sitting on top of the laundy is a pair of sexy black panties."
    "You feel your cock stir when you think about the ass those panties cover. Maybe while you wait for your laundry you could relieve some tension fantasizing about that..."
    menu:
        "Masturbate with panties":
            "You take a quick look out the door to make sure the coast is clear, then close it behind you. You grab the panties and then pull your pants down."
            "You wrap the cloth of the panties around your cock and start to work them up and down. The satin texture feels great."
            "You close your eyes and imagine [the_panties.title]. You imagine her in the morning, pulling up her cum filled panties up and wearing them around all day long."
            if renpy.random.randint(1,2) == 1: #No one catches you
                "Images of [the_panties.title] flood you brain as you continue to jack off. She's bent over now, begging you to cum all over her ass."
                "You go past the point of no return. You wrap the panties around the tip and then fire your load off into them."
                "When you finish, you take a look at them. Your cum is all over [the_panties.title]'s panties."
                "You do your best to fold them back up and put them back at the top of her laundry pile. You wonder if she'll notice."
                "Soon the washer is done. You swap your clothes to the dryer and start it, then head for bed. They should be dry in the morning!"
                #TODO mandatory event the next day when the girl discovers her used panties
            elif the_person == the_panties:                               #the panty owner catches you!
                "Your imagination is running wild and lewd images of [the_person.title] run through your head. Suddenly, you hear the laundry room door open!"
                the_person.char "Holy fuck!"
                $ the_person.draw_person()
                "You are totally busted!"
                if the_person.sluttiness < 20:
                    $ the_person.draw_person(position = "stand4", emotion= "angry")
                    the_person.char "[the_person.mc_title]! Those are my panties! What the fuck do you think you're doing? "
                    "You try to respond but just stammer. You're pretty sure theres no way to salvage this."
                    the_person.char "God I can't believe you. Don't touch my stuff! This is so gross! I'm gonna have to rewash these!"
                    "She quickly grabs her panties from your hand. She grabs the rest of her laundry and walks out of the laundry room."
                    $ the_person.change_happiness(-10)
                    $ the_person.change_obedience(-10)
                    $ the_person.change_slut_temp(10)
                    "Soon the washer is done. You swap your clothes to the dryer and start it, then head for bed. They should be dry in the morning!"
                elif the_person.sluttiness < 50:
                    $ the_person.draw_person(position = "stand4")
                    the_person.char "Is that... are those MY panties?"
                    "Her eyes are glued on your crotch. She actually doesn't seem mad?"
                    the_person.char "I didn't realize that my panties made you feel that way..."
                    "You decide to take a risk. You look her in the eyes and start to stroke your cock. The movement shocks her out of her staring and you make eye contact."
                    the_person.char "Oh god... can I... can I watch you?"
                    mc.name "Go ahead."
                    "Her eyes go back down to your crotch as you continue to stroke yourself."
                    mc.name "You should do it to. We all need to get off once a while!"
                    "She looks at you, still a bit conflicted."
                    the_person.char "I could... I mean... you aren't going to tell anyone about this are you?"
                    mc.name "Of course not."
                    $ the_person.draw_person(position = "kneeling1")
                    "[the_person.possessive_title] begins to rub her crotch. She gets down on her knees and continues to watch as you stroke yourself."
                    the_person.char "It looks so hard, I bet you are gonna cum so much."
                    "Her hand is moving rapidly between her legs. She is really getting off on this!"
                    the_person.char "You should do it... cum in my panties! I want to watch you hose them down!"
                    "Her encouragement and attention drive you over the edge.  You wrap the panties around the tip and then fire your load off into them."
                    the_person.char "Oh wow! There's so much!"
                    "You glance down and see her rapidly rubbing circles around her pussy."
                    mc.name "Do you want some help getting off?"
                    if the_person.obedience > 130:          #
                        the_person.char "Oh, I mean umm, I couldn't possibly ask you to do something like that..."
                        "You decide to take charge."
                        mc.name "Nonsense. Here, let me help you up."
                        "You put her cum soaked panties back on top of her clean laundry, then pick her up and put her on the edge of the dryer with her ass on the edge."
                        "You gently push her on her back."
                        $ the_person.draw_person (position = "missionary")
                        the_person.char "[the_person.mc_title]? Oh god, what are you going to do to me?"
                        "You put your finger over her lips to silence her."
                        if the_person.outfit.vagina_available():           #If its available no need to strip.
                             "You lower your face down between her legs. With her pussy exposed you waste no time diving right in"
                        else:                                              #Otherwise, strip her down.
                             "You don't bother to reply, instead you begin stripping away anything between you and her delicious pussy"

                             python:
                                    for clothing in the_person.outfit.get_lower_ordered():
                                         the_person.outfit.remove_clothing(clothing)
                                         the_person.draw_person(position = "missionary")
                                         renpy.say("","")

                             "With her pussy finally exposed you waste no time diving right in"
                        "Cupping her ass with your hands, you circle your tongue all around her wet, inviting cunt."
                        the_person.char "Oh [the_person.mc_title], you have no idea how bad I need this."
                        "[the_person.possessive_title] runs her hands your hair. You bury your nose in her mound and flick your tongue in and out of her slick hole"
                        "You circle her clit a few times with your tongue. You suck it into your mouth roughly a couple of times and then release it, you lips making a wet, lewd smacking noise"
                        the_person.char "I am so close... you're gonna make me cum!"
                        $ the_person.draw_person(emotion="orgasm", position ="missionary")
                        "You double your efforts, licking, sucking, and teasing every corner of her pleasing slit"
                        "[the_person.possessive_title] begins to orgasm convulsively, and she cries out."
                        the_person.char "Yes [the_person.mc_title]! Yes! Yes! Oh fuck how do you do that"
                        $ mc.listener_system.fire_event("girl_climax", the_person = the_person, the_position = "missionary")
                        $ the_person.change_happiness(5)
                        $ the_person.change_obedience(5)
                        $ the_person.change_slut_core(2)
                        $ the_person.change_slut_temp(5)
                        $ the_person.change_love(3)
                        "[the_person.possessive_title] runs her hands through your hair one last time. She sits up and gives you a kiss, tasting herself on your tongue."
                        the_person.char "Remember... this is our little secret... okay?"
                        "You hear the sound of the washing machine stopping. You start to open it up and move your laundry over to the dryer."
                        "Each time you move some clothing over, you bend over unneccesarily far so your face is near her cunt again. A couple times you give her a quick lick and she shudders."
                        $ the_person.draw_person()
                        "[the_person.title] slowly gets to her feet, but she is a little unsteady. You start the dryer with all your clothes in it, then grab her clean laundry."
                        mc.name "I'll get this for you."
                        the_person.char "Thanks, just give me a second."
                        "You slowly escort her to her room with her clean laundry, her cum filled panties sitting on the top of the pile. You set the clothes down and say goodnight."
                        "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                    else:
                        the_person.char "Oh, that's okay [the_person.mc_title]. I'm just gonna grab my laundry and go back to my room for some private time..."
                        mc.name "You should let me help, after all..."
                        "She cuts you off mid-sentence."
                        the_person.char "No, you've done quite enough already! Thanks though!"
                        "She grabs her cum filled panties from your hands, then grabs her laundry and quickly leaves the room."
                        $ renpy.scene("Active")
                        "You wait a few minutes until the washer is done. You move your laundry over to the dryer then walk to your room."
                        "You walk by [the_person.title]'s room as you go. You stop for a second outside her door and can hear soft moans coming from inside. You wonder if she is playing with those panties..."
                        "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                        $ the_person.change_happiness(3)
                        $ the_person.change_slut_core(2)
                        $ the_person.change_slut_temp(3)
                elif the_person.sluttiness < 75:
                    $ the_person.draw_person(position = "stand4", emotion = "happy")
                    the_person.char "Oh! You're using my panties!"
                else:
                    pass

            else:                                                        #Someone else catches you!
                pass
            #TODO
            pass
        "Find something else to do":
            "You decide to do something else. You head back to room and hop on your PC, doing work related tasks until the washer is done."
            "You go back to swap your laundry to the dryer."
            $ the_panties.draw_person()
            "[the_panties.title] is just coming out of the laundry room with her laundry basket."
            #TODO outfit and text based on her sluttiness.
            "You say goodnight to [the_panties.title] and then swap your clothes from the washer to the dryer. They should be dry in the morning!"
            $ renpy.scene("Active")
            return



    $ renpy.scene("Active")
    $ the_person.review_outfit(show_review_message = False)
    return
