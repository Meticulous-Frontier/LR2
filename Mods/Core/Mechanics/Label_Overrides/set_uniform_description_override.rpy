init 2 python:
    config.label_overrides["set_uniform_description"] = "set_uniform_description_enhanced" # Original label in script.rpy

label set_uniform_description_enhanced():
    $ slut_limit, underwear_limit, limited_to_top = mc.business.get_uniform_limits() #Function generates all uniform related limits to keep them consistent between events and active/deavtive policies.

    # TODO: Enable vanilla functionality of having seperate underwear slut limit and prevent underwear assignment without reduced_coverage_uniform_policy.is_owned()
    # I personally don't think it is nescessary due to the being limited to 25 sluttiness
    call screen import_outfit_manager(mc.designed_wardrobe, slut_limit = slut_limit, underwear_limit = underwear_limit, show_export = False)

    return
