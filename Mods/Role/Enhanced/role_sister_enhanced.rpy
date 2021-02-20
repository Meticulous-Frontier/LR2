init 5 python:
    config.label_overrides["sister_instathot_label_mom"] = "sister_instathot_label_mom_enhanced"

label sister_instathot_label_mom_enhanced(the_sister, the_mom):
    $ clear_scene()
    $ scene_manager = Scene()

    "You leave [the_sister.title] in her room and go to find [the_mom.possessive_title]."
    $ first_time = the_mom.event_triggers_dict.get("mom_instathot_pic_count",0) == 0
    $ kitchen.show_background()
    $ scene_manager.add_actor(the_mom, position = "back_peek")
    "You find her in the kitchen, standing in front of the open fridge."
    the_mom "Oh, hi [the_mom.mc_title]. I was just about to prepare something to eat, is there anything you need?"
    if first_time:
        mc.name "[the_sister.title] is getting ready to take some pictures for her Insta-pic account."
        mc.name "She wanted to know if you wanted to join in."
        $ scene_manager.update_actor(the_mom, position = "stand2", emotion = "happy")
        the_mom "Really? She's not just saying that to make me happy, is she?"
        mc.name "No, she really wants to spend time with you [the_mom.title]."
        the_mom "Okay then, I'll give it a try."
    else:
        mc.name "[the_sister.title] is getting ready to take some more pictures for her Insta-pic."
        mc.name "Do you want to join in?"
        $ scene_manager.update_actor(the_mom, position = "stand2", emotion = "happy")
        the_mom "I really should get something to eat, but it was a lot of fun..."
        the_mom "Oh what the heck, let's do this and have some fun."

    "[the_mom.possessive_title] closes the fridge and follows you back to [the_sister.possessive_title]'s room."
    $ lily_bedroom.show_background()
    $ scene_manager.update_actor(the_mom, emotion = "default", display_transform = character_center_flipped)
    $ scene_manager.add_actor(the_sister, display_transform = character_right)

    if first_time:
        the_sister "Hey [the_mom.title], come on in."
        the_mom "Thank you for inviting me, I just hope I'm not going to get in your way."
        mc.name "You're going to do great [the_mom.title]."
        the_mom "Thank you sweetheart. You can run along then, me and your sister will..."
        the_sister "Wait [the_mom.title], we need him. He's going to take the pictures."
        the_mom "Oh! I was wondering how we were going to both be in the pictures. That makes sense."
        the_mom "What do we first then?"
        if the_sister.event_triggers_dict.get("sister_instathot_mom_pics_slutty", False):
            the_sister "I've got some outfits picked out for us. I had to guess at some of your sizes, so it might be a bit small."
            the_sister "You don't have to wear it if you don't want to though. I..."
            $ scene_manager.update_actor(the_mom, position = "stand4", emotion = "angry")
            "[the_mom.title] shakes her head and interrupts."
            the_mom "[the_sister.title], I want the whole experience! These outfits will get you more view on your insta... view... pic thing, right?"
            the_mom "Come on, show me what you picked out for me. I'm sure I can squeeze into it with a little bit of work."
        else:
            the_sister "First I need to pick an outfit and get changed."
            the_sister "You don't have to change anything though, I'll just..."
            $ scene_manager.update_actor(the_mom, position = "stand4", emotion = "angry")
            "[the_mom.title] shakes her head and interrupts."
            the_mom "[the_sister.title], I want the whole experience! Don't you want more views on your insta... view... pic thing?"
            the_mom "Come on, show me what you have. I'm sure you have something I can squeeze into."
        $ scene_manager.update_actor(the_mom, position = "stand3", emotion = "default")
        "[the_sister.possessive_title] smiles and nods. She waves [the_mom.possessive_title] over to the pile of clothes she has laid out on her bed."
        the_sister "Really? Alright! Well, I've got this a few days ago that's really cute and..."
        "You lean against a wall and pass some time on your phone while [the_sister.possessive_title] and [the_mom.title] pick out outfits."
        the_sister "Right, I think these are going to drive them wild. Come on, let's see how they look!"

    else:
        the_sister "Hey [the_mom.title], come on in!"
        the_mom "Hi [the_mom.mc_title], thanks for having me back. So, do you have something for us to wear today?"
        the_sister "I've got some really cute outfits I think we'll look amazing in. Come on, let's get changed."

    if the_mom.has_taboo(["bare_tits", "bare_pussy"]): #She doesn't want to strip in front of you, let's break those taboos!
        the_mom "[the_mom.mc_title], you don't mind, do you? I can go back to my room if this..."
        mc.name "Don't worry [the_mom.title], I don't mind at all. Go ahead and get changed and we can take some pics."
        the_mom "Right, nothing to worry about then..."
        "She seems uncomfortable undressing in front of you, but gets over it quickly as [the_sister.title] starts stripping down without comment."
        $ the_mom.break_taboo("bare_tits")
        $ the_mom.break_taboo("bare_pussy")
    else: #No problems here, strip away!
        "[the_sister.title] starts to strip down, and [the_mom.possessive_title] hurries to keep up."

    $ scene_manager.strip_actor_outfit(the_sister, exclude_feet = False)
    $ scene_manager.strip_actor_outfit(the_mom, exclude_feet = False)

    $ insta_outfit_mom = insta_wardrobe.pick_random_outfit()
    $ insta_outfit_sister = insta_wardrobe.pick_random_outfit()

    if insta_outfit_mom.name == insta_outfit_sister.name:
        the_sister "I got us matching outfits, because I thought it would really show off the family resemblance."
        the_sister "It should make for a really cute shoot! Maybe [the_sister.mc_title] can tell us who wears it best."

    $ the_mom.apply_outfit(insta_outfit_mom)
    $ the_sister.apply_outfit(insta_outfit_sister)

    $ scene_manager.draw_scene()

    "The girls get dressed. [the_mom.title] turns to [the_sister.possessive_title], ready for her inspection."

    $ scene_manager.update_actor(the_mom, position = "back_peek")
    the_mom "Okay, am I wearing this right?"
    the_sister "You look great [mom.title], it's so cute on you!"
    $ scene_manager.update_actor(the_mom, position = "stand3")
    if the_mom.judge_outfit(insta_outfit_mom):
        the_mom "Thank you! We need to go shopping together, I think I need more fashion advice from you."
    else:
        the_mom "Are you sure there isn't any more? A slip or a cover-up, maybe?"

    the_sister "Come on [mom.title], we've got to take some pictures now. Get up here."

    $ scene_manager.update_actor(the_sister, position = "kneeling1", emotion = "happy")
    "[the_sister.title] jumps onto her bed and gets onto her knees, looking towards you and her phone camera."
    the_mom "Okay, I think I can do that..."
    $ scene_manager.update_actor(the_mom, position = "kneeling1", emotion = "happy")
    "[the_mom.possessive_title] gets onto the bed with [the_sister.possessive_title]."
    mc.name "That's looking good you two, now look at me and smile."
    "You take a few pictures of them, moving around the bed to get a few different angles."
    menu:
        "Get a little friendlier" if not first_time:
            mc.name "Squeeze together you two, I need to get you both in the shot."
            $ scene_manager.update_actor(the_mom, display_transform = character_center_flipped(xoffset = .1), z_order = -10)
            "[the_mom.title] slides closer to [the_sister.title] on the bed."
            the_mom "Like this?"
            mc.name "A little more. Try putting your arms around her."
            $ scene_manager.update_actor(the_mom, display_transform = character_center_flipped(xoffset = .2))
            "[the_mom.possessive_title] slips behind [the_sister.possessive_title] and pulls her into a hug"
            the_mom "I haven't played with you like this since you were a kid [the_sister.title]!"
            the_sister "Oh my god, you're so embarrassing [the_mom.title]!"
            the_mom "[the_mom.mc_title], make sure to get some shots of me embarrassing your sister."
            "She leans over [the_sister.title]'s shoulder and kisses her on the side of the cheek."
            $ the_mom.change_happiness(10)
            $ the_mom.change_slut_temp(2)
            $ the_sister.change_happiness(5)
            "You get some great pictures of [the_mom.title] and [the_sister.title] playing around on the bed together."


        # TODO: Add some extra variations for this as sluttiness and Obedience rises.
        "All done":
            pass

    mc.name "Alright, I think we've got all the shots we need."
    $ scene_manager.update_actor(the_mom, position = "stand2", display_transform = character_center_flipped)
    "[the_mom.possessive_title] hops off of the bed."
    the_mom "That was really fun, thanks for inviting me you two."
    $ scene_manager.update_actor(the_sister, position = "stand3")
    the_sister "It was! Oh, I should give [the_sister.mc_title] his cut for being our photographer."

    menu:
        "Take the money\n{color=#00ff00}{size=18}Income: $100{/size}{/color}":
            the_mom "It's so nice to see you two working well together."
            $ mc.business.funds += 100

        "Let her keep it":
            mc.name "Don't worry about it, I'm just happy to see you doing something cool."
            $ the_sister.change_love(1)
            the_sister "Aww, you're the best!"
            "She gives you a hug and a quick kiss on the cheek."
            $ the_mom.change_love(1)
            the_mom "You're such a good brother [the_mom.mc_title]."

        "Let [the_mom.title] have it":
            mc.name "[the_mom.title], you can have what [the_sister.title] normally gives me."
            mc.name "I hope that helps with the bills."
            the_mom "Oh sweetheart, you don't have to..."
            mc.name "Really [the_mom.title], I want you to have it."
            $ the_mom.change_love(2)
            the_mom "Thank you, it really does help."

    if the_mom.judge_outfit(insta_outfit_mom) and not the_mom.wardrobe.has_outfit_with_name(insta_outfit_mom.name):
        the_mom "Say [the_sister.title], do you need this outfit back?"
        the_sister "No, you can keep it if you want. It's obviously not my size, and I don't think they'll take returns."
        $ the_mom.wardrobe.add_outfit(insta_outfit_mom)
        $ the_mom.planned_outfit = insta_outfit_mom #She wears it for the rest of the day.
        the_mom "Thank you! It's so cute, it would be a shame for it to go to waste. Now I really need to get back to the kitchen!"
        $ scene_manager.update_actor(the_mom, position = "walking_away")
        "[the_mom.title] collects her clothing and hurries off to her room."

    else:
        the_mom "Well, I need to go get changed and get back to the kitchen."
        $ scene_manager.update_actor(the_mom, position = "walking_away")
        "[the_mom.title] collects her clothing and hurries off to her room."

    $ scene_manager.remove_actor(the_mom)
    "You give [the_sister.title] her phone back and leave her to upload the pics."

    if the_sister.judge_outfit(insta_outfit_sister) and not the_sister.wardrobe.has_outfit_with_name(insta_outfit_sister.name):
        $ the_sister.wardrobe.add_outfit(insta_outfit_sister)

    if the_mom.event_triggers_dict.get("mom_instathot_pic_count", 0) == 0:
        $ the_mom.event_triggers_dict["mom_instathot_pic_count"] = 1
        $ add_sister_instathot_mom_report_action(the_sister)
    else:
        $ the_mom.event_triggers_dict["mom_instathot_pic_count"] += 1

    if the_sister.event_triggers_dict.get("sister_instathot_pic_count", 0) == 0:
        $ the_sister.event_triggers_dict["sister_instathot_pic_count"] = 1
    else:
        $ the_sister.event_triggers_dict["sister_instathot_pic_count"] += 1

    python:
        scene_manager.clear_scene()
        insta_outfit_mom = None
        insta_outfit_sister = None
    return
