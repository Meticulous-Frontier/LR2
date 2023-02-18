init 1310 python:           # init after VREN personalities, but before our personalities
    def relaxed_titles(person):
        valid_titles = []
        valid_titles.append(person.formal_address + " " + person.last_name)
        if person.love > 20:
            valid_titles.append(person.name)
        if person.sluttiness > 40:
            valid_titles.append("Candy")
        if person.sluttiness > 60:
            valid_titles.append("Hot Stuff")

        return valid_titles

    def relaxed_player_titles(person):
        valid_titles = []
        valid_titles.append("Mr. " + mc.last_name)
        if person.love > 10:
            valid_titles.append(mc.name)
        if person.has_breeding_fetish():
            valid_titles.append("Bull")
        return valid_titles

    relaxed_personality.titles_function = relaxed_titles
    relaxed_personality.player_titles_function = relaxed_player_titles

label relaxed_sex_toy_taboo_break(the_person):
    pass
    return

label relaxed_roleplay_taboo_break(the_person):
    pass
    return

label relaxed_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.sluttiness < 80:
        the_person "Sounds great! Save some energy, we can make it a fun night."
    else:
        the_person "Are you having the same dirty urges as me? Save some energy for me. We can make it a great night!"
    return

label relaxed_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.sluttiness < 80:
        the_person "Mmm, that sounds great! Bring a toothbrush, you can spend the night."
    else:
        the_person "You don't need the wine to seduce me."
    return

label relaxed_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    "[the_person.title] slowly walks over to you, purposefully exaggerating her hip movements with each step."
    the_person "Thanks... you ready for some fun?"
    return

label relaxed_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    the_person "Mmm... what do you say we stay in and just cuddle tonight?"
    "She gives you a smirk. You can't help but frown at the thought of just cuddling..."
    the_person "Hah! Oh my god, you should have seen your face..."
    "She sets her wine down on her nightstand."
    the_person "Get over here! I'm ready for some fun!"
    return

label relaxed_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Oh my god, you're making me cum my brains out... this is amazing..."
    "[the_person.title] lies down in bed and catches her breath."
    the_person "I think I can keep going... I'm gonna be sore in the morning though!"
    return

label relaxed_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ahhh, that was nice..."
    "[the_person.title] lies down in bed and catches her breath."
    the_person "I'm ready to go again if you are!"
    return

label relaxed_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Whew, good job. Get some water and let's go for another!"
    "You take some time to catch your breath, drink some water, and wait for your refractory period to pass."
    "You hold [the_person.title] in bed while she caresses you and touches herself, keeping herself ready for you."
    return

label relaxed_lingerie_shopping_tame_response(the_person):
    the_person "Are you sure? This seems kinda tame..."
    mc.name "I know. I just want to see what it looks like on you."
    return

label relaxed_lingerie_shopping_excited_response(the_person):
    the_person "Ah, this look great! I bet you will like this!"
    return

label relaxed_lingerie_shopping_wow_response(the_person):
    the_person "Wow! I can honestly say I was not expecting you to go all in like this!"
    mc.name "If you don't feel comfortable with it, that's okay."
    "She is quiet, but you can hear her rustling around inside as she starts getting changed."
    the_person "It's okay... This is just to wear in private with you anyway... right?"
    return

label relaxed_GIC_finish_response(the_person, the_goal):
    if the_goal is None:
        the_person "Mmm, that was exactly what I was hoping for!"
    elif the_goal == "get mc off":
        the_person "Did that feel good? I just want to make you feel good..."
    elif the_goal == "anal creampie":
        the_person "Wow... I can feel it deep inside me..."
    elif the_goal == "get off":
        the_person "Oh god I really needed to get off."
    elif the_goal == "waste cum":
        the_person "Keep that cum where it belongs... far away from me!"
    elif the_goal == "hate fuck":
        the_person "God I needed to get off. Did you finish? Ah nevermind I don't care anyway."
    elif the_goal == "vaginal creampie":
        if the_person.has_breeding_fetish():
            the_person "MMmmm, I can feel your cum so deep..."
        else:
            the_person "I can't help it, it feels so good when you finish inside me..."
    elif the_goal == "facial":
        the_person "How does it look? It feels good on my face."
    elif the_goal == "body shot":
        the_person "Mmm, your cum is so hot. I love the way it feels on my skin."
    elif the_goal == "oral creampie":
        the_person "You tasted great..."
    else:
        the_person "Mmm, that was exactly what I was hoping for!"
    return
