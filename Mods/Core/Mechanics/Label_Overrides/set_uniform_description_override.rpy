init 2 python:
    config.label_overrides["set_uniform_description"] = "set_uniform_description_enhanced" # Original label in script.rpy

label set_uniform_description_enhanced():
    #First, establish the maximums the uniform can reach.
    if maximal_arousal_uniform_policy.is_owned():
        $slut_limit = 999 #ie. no limit at all.
        $underwear_limit = 999
    elif corporate_enforced_nudity_policy.is_owned():
        $slut_limit = 100
        $underwear_limit = 60
    elif minimal_coverage_uniform_policy.is_owned():
        $slut_limit = 80
        $underwear_limit = 40
    elif reduced_coverage_uniform_policy.is_owned():
        $slut_limit = 60
        $underwear_limit = 25
    elif casual_uniform_policy.is_owned():
        $slut_limit = 45
        $underwear_limit = -1
    elif relaxed_uniform_policy.is_owned():
        $slut_limit = 30
        $underwear_limit = -1
    elif strict_uniform_policy.is_owned():
        $slut_limit = 25
        $underwear_limit = -1
    else:
        $slut_limit = 0
        $underwear_limit = -1

    # TODO: Enable vanilla functionality of having seperate underwear slut limit and prevent underwear assignment without reduced_coverage_uniform_policy.is_owned()
    # I personally don't think it is nescessary due to the being limited to 25 sluttiness
    call screen import_outfit_manager(mc.designed_wardrobe, slut_limit = slut_limit, underwear_limit = underwear_limit, show_export = False)

    return
