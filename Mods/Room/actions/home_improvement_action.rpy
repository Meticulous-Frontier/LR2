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
init 0 python:
    home_improvement_crisis_weight = 5
    mc_bedroom_renovation_cost = 5000 # Currently used for all bedrooms, this could be varied.
    home_improvement_base_duration = 0 # (+0-3 days, always takes at least one full day), dungeon takes longer.

    def mc_bedroom_renovate_requirement():
        if bedroom.background_image == standard_bedroom3_background:
            return False
        if is_home_improvement_in_progress():
            return "Wait for current project completion"
        if not mc.business.is_open_for_business():
            return "Only during business hours"
        if mc.business.funds > mc_bedroom_renovation_cost:
            return True
        return False

    def home_improvement_unlocked_requirement(trigger_day): # Currently ignoring trigger_day
        return bedroom.background_image == standard_bedroom3_background

    def lily_bedroom_renovate_requirement():
        if lily.home.background_image == lily_bedroom_background:
            return False
        if is_home_improvement_in_progress():
            return "Wait for current project completion"
        if not mc.business.is_open_for_business():
            return "Only during business hours"
        if mc.business.funds > mc_bedroom_renovation_cost:
            return True
        else:
            return "Requires: $" + str(mc_bedroom_renovation_cost)
        return False

    def mom_bedroom_renovate_requirement():
        if mom.home.background_image == standard_bedroom1_background:
            return False
        if is_home_improvement_in_progress():
            return "Wait for current project completion"
        if not mc.business.is_open_for_business():
            return "Only during business hours"
        if mc.business.funds > mc_bedroom_renovation_cost:
            return True
        else:
            return "Requires: $" + str(mc_bedroom_renovation_cost)
        return False

    def home_shower_renovate_requirement():
        if home_shower.background_image == standard_home_shower_backgrounds:
            return False
        if is_home_improvement_in_progress():
            return "Wait for current project completion"
        if not mc.business.is_open_for_business():
            return "Only during business hours"
        if mc.business.funds > mc_bedroom_renovation_cost:
            return True
        else:
            return "Requires: $" + str(mc_bedroom_renovation_cost)
        return False

    def dungeon_build_action_requirement():
        if (mc.has_dungeon()):
            return False
        if is_home_improvement_in_progress():
            return "Wait for current project completion"
        if not mc.business.is_open_for_business():
            return "Only during business hours"
        if mc.business.funds > 10000:
            return True
        else:
            return "Requires: $10000"
        return False

init 2 python:
    # ModAction initialization. Kicks off initial entry into code.
    add_mc_bedroom_renovate_action = ActionMod("Home Improvement", mc_bedroom_renovate_requirement, "mc_bedroom_renovate_option_label",
        menu_tooltip = "Enables a series of renovations for your home into more impressive state (with some bonuses), including home dungeon.", category = "Home", is_crisis = True, crisis_weight = home_improvement_crisis_weight )

    def mc_bedroom_renovate_action_requirement():
        if (mc.business.funds > mc_bedroom_renovation_cost and bedroom.background_image != standard_bedroom3_background):
            return True
        elif (mc.business.funds < mc_bedroom_renovation_cost and bedroom.background_image != standard_bedroom3_background):
            return "Requires: $" + str(mc_bedroom_renovation_cost)
        else:
            return False

    def add_mc_bedroom_renovate_action():
        bedroom.add_action(Action("Renovate room", mc_bedroom_renovate_requirement, "mc_bedroom_renovate_label", menu_tooltip = "Renovates your bedroom into more impressive state (+5 Obedience and Sluttiness for some encounters within). Cost $" + str(mc_bedroom_renovation_cost) + ".", priority = 10))
        return

    def add_home_improvement_actions():
        dungeon_build_action = Action("Build dungeon", dungeon_build_action_requirement, "dungeon_build_label", menu_tooltip = "Clear the cellar and build a Sex Dungeon, complete with \"Guest Accommodations\". Cost $10000.", priority = 10)
        lily_bedroom_renovate_action = Action("Renovate room", lily_bedroom_renovate_requirement, "lily_bedroom_renovate_label", menu_tooltip = "Renovates Lily's bedroom into more impressive state and increases her love for you. Cost $" + str(mc_bedroom_renovation_cost) + ".", priority = 10)
        mom_bedroom_renovate_action = Action("Renovate room", mom_bedroom_renovate_requirement, "mom_bedroom_renovate_label", menu_tooltip = "Renovates Mom's bedroom into more impressive state and increases her love for you. Cost $" + str(mc_bedroom_renovation_cost) + ".", priority = 10)
        home_shower_renovate_action = Action("Renovate shower", home_shower_renovate_requirement, "home_shower_renovate_label", menu_tooltip = "Renovates the shower in your house and increases your daily energy. Cost $" + str(mc_bedroom_renovation_cost) + ".", priority = 10)

        mom_bedroom.add_action(mom_bedroom_renovate_action)
        lily_bedroom.add_action(lily_bedroom_renovate_action)
        bedroom.add_action(home_shower_renovate_action)
        #hall.actions.append(room_renovation_action) # Eventually improve the front hall as well.
        # Kitchen? When we get a good graphic for a VERY nice kitchen?
        if not is_dungeon_unlocked():
            hall.add_action(dungeon_build_action)
            mc.business.event_triggers_dict["dungeon_unlocked"] = True
        return

    def renovate_room_requirement():
        return True

    def home_renovation_completion_requirement(completion_day):
        if day > completion_day and mc.business.is_open_for_business():
            return True
        return False

    def add_mc_bedroom_renovate_completed_action():
        mc_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", home_renovation_completion_requirement, "mc_bedroom_renovate_completed_label", requirement_args = (day + home_improvement_base_duration + renpy.random.randint(0,3)))
        mc.business.add_mandatory_crisis(mc_bedroom_renovate_completed_action)

    def add_lily_bedroom_renovate_completed_action():
        lily_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", home_renovation_completion_requirement, "lily_bedroom_renovate_completed_label", requirement_args = (day + home_improvement_base_duration + renpy.random.randint(0,3)))
        mc.business.add_mandatory_crisis(lily_bedroom_renovate_completed_action)

    def add_mom_bedroom_renovate_completed_action():
        mom_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", home_renovation_completion_requirement, "mom_bedroom_renovate_completed_label", requirement_args = (day + home_improvement_base_duration + renpy.random.randint(0,3)))
        mc.business.add_mandatory_crisis(mom_bedroom_renovate_completed_action)

    def add_home_shower_renovate_completed_action():
        home_shower_renovate_completed_action = Action("Shower Renovation Completed", home_renovation_completion_requirement, "home_shower_renovate_completed_label", requirement_args = (day + 2 + home_improvement_base_duration + renpy.random.randint(0,3)))
        mc.business.add_mandatory_crisis(home_shower_renovate_completed_action)

    def add_dungeon_build_completed_action():
        dungeon_completed_action = Action("Dungeon Completed", home_renovation_completion_requirement, "dungeon_build_completed_label", requirement_args = day + 6 + renpy.random.randint(0,3))
        mc.business.add_mandatory_crisis(dungeon_completed_action)

    def upgrade_bedroom(room, background):
        room.background_image = background
        room.remove_object("bed")
        room.remove_object("chair")
        room.add_object( make_comfy_chair() )
        room.add_object( make_impressive_bed() )
        return


label mc_bedroom_renovate_option_label():
    "It occurs to you that your bedroom still looks like that of a poor college student rather than someone who owns a business. Perhaps you should consider spending some time and money renovating?"
    "After a bit of online shopping you figure about $[mc_bedroom_renovation_cost] ought to cover it."
    $ add_mc_bedroom_renovate_action()
    return

label mc_bedroom_renovate_label():
    "You decide to renovate your bedroom and call a contractor recommended by a college friend: Turner construction, renowned for their efficiency and discretion."
    mc.name "Good day, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details to vastly improve your bedroom from a college student's decor to something more befitting the head of a successful company."
    python:
        mc.business.change_funds(- mc_bedroom_renovation_cost)
        mc.business.event_triggers_dict["home_improvement_in_progress"] = True
        add_mc_bedroom_renovate_completed_action()
    return

label mc_bedroom_renovate_completed_label():
    $ man_name = get_random_male_name()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "Your bedroom renovation is complete."
    python:
        upgrade_bedroom(bedroom, standard_bedroom3_background)
        mc.business.event_triggers_dict["home_improvement_in_progress"] = False
        mc.business.add_mandatory_crisis(Action("Open up additional home improvement", home_improvement_unlocked_requirement, "home_improvement_unlocked_label", requirement_args = day + 1))
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
    mc.name "Good day, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details to vastly improve your bedroom from a college student's decor to something more befitting the head of a successful company."
    python:
        mc.business.change_funds(- mc_bedroom_renovation_cost)
        mc.business.event_triggers_dict["home_improvement_in_progress"] = True
        add_lily_bedroom_renovate_completed_action()
    return

label lily_bedroom_renovate_completed_label():
    $ man_name = get_random_male_name()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "Your [lily.possessive_title]'s bedroom renovation is complete."
    python:
        upgrade_bedroom(lily.home, lily_bedroom_background)
        lily.change_stats(love = 3 + mc.charisma, obedience = 1 + mc.charisma)
        mc.business.event_triggers_dict["home_improvement_in_progress"] = False
    return

label mom_bedroom_renovate_label():
    "You decide to renovate [mom.title]'s bedroom. After discussing with your [mom.possessive_title] what she wants, you call your contractor."
    mc.name "Good day, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details to vastly improve your [mom.possessive_title]'s bedroom."
    python:
        mc.business.change_funds(- mc_bedroom_renovation_cost)
        mc.business.event_triggers_dict["home_improvement_in_progress"] = True
        add_mom_bedroom_renovate_completed_action()
    return

label mom_bedroom_renovate_completed_label():
    $ man_name = get_random_male_name()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The bedroom renovation is complete."
    python:
        upgrade_bedroom(mom.home, standard_bedroom1_background)
        mom.change_stats(love = 3 + mc.charisma, obedience = 1 + mc.charisma)
        mc.business.event_triggers_dict["home_improvement_in_progress"] = False
    return

label home_shower_renovate_label():
    "You decide to renovate the home shower, a little more luxury in the morning can go a long way. After talking it over with Mom and Lily, you call your contractor."
    mc.name "Good day, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details to vastly improve your home shower."
    python:
        mc.business.change_funds(- mc_bedroom_renovation_cost)
        mc.business.event_triggers_dict["home_improvement_in_progress"] = True
        add_home_shower_renovate_completed_action()
    return

label home_shower_renovate_completed_label():
    $ man_name = get_random_male_name()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The new shower is complete and ready for inspection."
    python:
        home_shower.background_image = standard_home_shower_backgrounds
        mc.change_max_energy(10)
        mc.business.event_triggers_dict["home_improvement_in_progress"] = False
    return
