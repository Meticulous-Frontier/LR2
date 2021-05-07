#
# Home Improvement  MOD:
# Plan:
# MC realizes his bedroom is pretty shabby and gets an option to renovate when he gets enough cash on hand to do so. (Action button in Bedroom)
# Mom later comment that he shouldn't stop there, the house could use additional improvements
# Renovate Sis bedroom
# Renovate Mom's bedroom
# Build Dungeon - Dungeon makes more sense in the context of multiple renovations on the house. Can even work in Mom's permission to do whatever he likes.
# Depends on dungeon code in: dungeon_room_actions.rpy
# Possible future improvements:
# Renovate Living room
# Renovate Exterior
# Jucazzi baths for bedrooms (still leaves main shower for encounters)
# Guest rooms/servants quarters?
init -1 python:
    home_improvement_crisis_weight = 5
    mc_bedroom_renovation_cost = 2500 # Currently used for all bedrooms, this could be varied.
    home_improvement_base_duration = 0 # (+0-3 days, always takes at least one full day), dungeon takes longer.

    def mc_bedroom_renovate_requirement():
        if (mc.business.funds > mc_bedroom_renovation_cost and bedroom.background_image != standard_bedroom3_background and not is_home_improvement_in_progress()):
            return True
        elif (bedroom.background_image != standard_bedroom3_background and is_home_improvement_in_progress()):
            return "Wait for renovation completion"
        return False

    def home_improvement_unlocked_requirement(trigger_day): # Currently ignoring trigger_day
        return bedroom.background_image == standard_bedroom3_background

    def lily_bedroom_renovate_requirement():
        if lily.home.background_image == lily_bedroom_background:
            return False
        if is_home_improvement_in_progress():
            return "Wait for current project completion"
        if mc.business.funds > mc_bedroom_renovation_cost:
            return True
        else:
            return "Requires: $2500"
        return False

    def mom_bedroom_renovate_requirement():
        if mom.home.background_image == standard_bedroom1_background:
            return False
        if is_home_improvement_in_progress():
            return "Wait for current project completion"
        if mc.business.funds > mc_bedroom_renovation_cost:
            return True
        else:
            return "Requires: $2500"
        return False

    def dungeon_build_action_requirement():
        if (mc.has_dungeon()):
            return False
        if is_home_improvement_in_progress():
            return "Wait for current project completion"
        if mc.business.funds > 10000:
            return True
        else:
            return "Requires: $10000"
        return False

    def dungeon_build_completed_action_requirement(completion_day):
        if day > completion_day and mc.is_at_work() and mc.business.is_open_for_business():
            return True
        return False

init 2 python:
    # Action Buttons for use when active.
    mc_bedroom_renovate_action = Action("Renovate room", mc_bedroom_renovate_requirement, "mc_bedroom_renovate_label", menu_tooltip = "Renovates your bedroom into more impressive state (+5 Obedience and Sluttiness for some encounters within). Cost $2500")

    # ModAction initialization. Kicks off initial entry into code.
    add_mc_bedroom_renovate_action = ActionMod("Home Improvement", mc_bedroom_renovate_requirement, "mc_bedroom_renovate_option_label",
        menu_tooltip = "Enables a series of renovations for your home into more impressive state (with some bonuses), including home dungeon.", category = "Home", is_crisis = True, crisis_weight = home_improvement_crisis_weight )

    def mc_bedroom_renovate_action_requirement():
        if (mc.business.funds > mc_bedroom_renovation_cost and bedroom.background_image != standard_bedroom3_background):
            return True
        elif (mc.business.funds < mc_bedroom_renovation_cost and bedroom.background_image != standard_bedroom3_background):
            return "Requires: $[mc_bedroom_renovation_cost]"
        else:
            return False


    def add_mc_bedroom_renovate_action():
        bedroom.actions.append(mc_bedroom_renovate_action)
        return

    def add_home_improvement_actions():
        dungeon_build_action = Action("Build dungeon", dungeon_build_action_requirement, "dungeon_build_label", menu_tooltip = "Clear the cellar and build a Sex Dungeon, complete with \"Guest Accomodations\". Cost $10000")
        lily_bedroom_renovate_action = Action("Renovate room", lily_bedroom_renovate_requirement, "lily_bedroom_renovate_label", menu_tooltip = "Renovates Lily's bedroom into more impressive state (+10 Love Lily). Cost $2500")
        mom_bedroom_renovate_action = Action("Renovate room", mom_bedroom_renovate_requirement, "mom_bedroom_renovate_label", menu_tooltip = "Renovates Mom's bedroom into more impressive state (+10 Love Mom). Cost $2500")

        mom_bedroom.actions.append(mom_bedroom_renovate_action)
        lily_bedroom.actions.append(lily_bedroom_renovate_action)
        #hall.actions.append(room_renovation_action) # Eventually improve the front hall as well.
        # Kitchen? When we get a good graphic for a VERY nice kitchen?
        if not is_dungeon_unlocked():
            hall.actions.append(dungeon_build_action)
            mc.business.event_triggers_dict["dungeon_unlocked"] = True
        return

    def renovate_room_requirement():
        return True

    def mc_bedroom_renovate_complete_requirement(completion_day):
        if day > completion_day and mc.is_at_work() and mc.business.is_open_for_business():
            return True
        return False

    def add_mc_bedroom_renovate_completed_action():
        mc_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", mc_bedroom_renovate_complete_requirement, "mc_bedroom_renovate_completed_label", requirement_args = (day + home_improvement_base_duration + renpy.random.randint(0,3)))
        mc.business.add_mandatory_crisis(mc_bedroom_renovate_completed_action)

    def add_lily_bedroom_renovate_completed_action():
        lily_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", mc_bedroom_renovate_complete_requirement, "lily_bedroom_renovate_completed_label", requirement_args = (day + home_improvement_base_duration + renpy.random.randint(0,3)))
        mc.business.add_mandatory_crisis(lily_bedroom_renovate_completed_action)

    def add_mom_bedroom_renovate_completed_action():
        mom_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", mc_bedroom_renovate_complete_requirement, "mom_bedroom_renovate_completed_label", requirement_args = (day + home_improvement_base_duration + renpy.random.randint(0,3)))
        mc.business.add_mandatory_crisis(mom_bedroom_renovate_completed_action)

    def add_dungeon_build_completed_action():
        dungeon_completed_action = Action("Dungeon Completed", dungeon_build_completed_action_requirement, "dungeon_build_completed_label", requirement_args = day + 7)
        mc.business.add_mandatory_crisis(dungeon_completed_action)

label mc_bedroom_renovate_option_label():
    "It occurs to you that your bedroom still looks like that of a poor college student rather than someone who owns a business. Perhaps you should consider spending some time and money renovating?"
    "After a bit of online shopping you figure about $[mc_bedroom_renovation_cost] ought to cover it."
    $ add_mc_bedroom_renovate_action()
    return

label mc_bedroom_renovate_label():
    "You decide to renovate your bedroom and call a contractor recommended by a college friend: Turner construction, reknowned for their efficiency and descretion."
    mc.name "Good afternoon, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details to vastly improve your bedroom from a college student's decor to something more befitting the head of a successful company."
    $ mc.business.change_funds(- mc_bedroom_renovation_cost)
    $ mc.business.event_triggers_dict["home_improvement_in_progress"] = True
    $ add_mc_bedroom_renovate_completed_action()
    return

label mc_bedroom_renovate_completed_label():
    $ man_name = get_random_male_name()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "Your bedroom renovation is complete."
    python:
        bedroom.background_image =  standard_bedroom3_background
        # TODO: Add bonuses to objects in the room? Improved objects? Comfy Chair and Impressive Bed to start
        bedroom.add_object( make_comfy_chair() )
        found = find_in_list(lambda x: x.name == "bed", bedroom.objects)
        if found:
            bedroom.objects.remove(found)
        bedroom.add_object( make_impressive_bed() )
        mc.business.event_triggers_dict["home_improvement_in_progress"] = False
        add_home_improvement_unlocked_action = Action("Open up additional home improvement", home_improvement_unlocked_requirement, "home_improvement_unlocked_label", requirement_args = day + 1)
        mc.business.add_mandatory_crisis(add_home_improvement_unlocked_action)
    return

label home_improvement_unlocked_label():
    $ the_person = mom
    $ mc.start_text_convo(the_person)
    mom "Wow [mom.mc_title], you did a great job on renovating your bedroom. You know if you feel like it, keep going! The house sure could use some upgrades. Just give us a heads up on what you want to do."
    mc.name "Okay, will think about it. And see when we have budget free."
    mom "No pressure, I know money's tight. But wow, if you could, that would be fantastic! Love you!"
    $ add_home_improvement_actions()
    $ mc.end_text_convo()
    return

label lily_bedroom_renovate_label():
    "You decide to renovate [lily.title]'s bedroom. After discussing with your [lily.possessive_title] what she wants, you call your contractor."
    mc.name "Good afternoon, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details to vastly improve your bedroom from a college student's decor to something more befitting the head of a successful company."
    $ mc.business.change_funds(- mc_bedroom_renovation_cost)
    $ mc.business.event_triggers_dict["home_improvement_in_progress"] = True
    $ add_lily_bedroom_renovate_completed_action()
    return

label lily_bedroom_renovate_completed_label():
    $ man_name = get_random_male_name()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "Your [lily.possessive_title]'s bedroom renovation is complete."
    python:
        lily.home.background_image =  lily_bedroom_background
        lily.home.add_object( make_chair() )
        found = find_in_list(lambda x: x.name == "bed", lily.home.objects)
        if found:
            lily.home.objects.remove(found)
        lily.home.add_object( make_impressive_bed() )
        lily.change_love(10 + mc.charisma)
        lily.change_obedience(5 + mc.charisma)
        mc.business.event_triggers_dict["home_improvement_in_progress"] = False
    return

label mom_bedroom_renovate_label():
    "You decide to renovate [mom.title]'s bedroom. After discussing with your [mom.possessive_title] what she wants, you call your contractor."
    mc.name "Good afternoon, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details to vastly improve your [mom.possessive_title]'s bedroom."
    $ mc.business.change_funds(- mc_bedroom_renovation_cost)
    $ mc.business.event_triggers_dict["home_improvement_in_progress"] = True
    $ add_mom_bedroom_renovate_completed_action()
    return

label mom_bedroom_renovate_completed_label():
    $ man_name = get_random_male_name()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The bedroom renovation is complete."
    python:
        mom.home.background_image =  standard_bedroom1_background
        mom.home.add_object( make_chair() )
        found = find_in_list(lambda x: x.name == "bed", mom.home.objects)
        if found:
            mom.home.objects.remove(found)
        mom.home.add_object( make_impressive_bed() )
        mom.change_love(10 + mc.charisma)
        mom.change_obedience(5 + mc.charisma)
        mc.business.event_triggers_dict["home_improvement_in_progress"] = False
    return
