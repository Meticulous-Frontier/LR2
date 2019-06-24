## Company Wardrobe Mod by Tristimdorion
# Adds outfits based on company name to outfit manager
init 3 python:
    company_wardrobe_loaded = False

    def company_wardrobe_requirement():
        return not company_wardrobe_loaded

    def company_wardrobe_initialization(self):
        lobby.actions.append(self)
        return

    company_wardrobe_action = ActionMod("Add Company Wardrobe", company_wardrobe_requirement, "append_company_wardrobe", initialization = company_wardrobe_initialization,  
        menu_tooltip = "Adds a collection of over- and underwear for your company to your outfit manager.", category = "Wardrobe")

label append_company_wardrobe:
    if mc.designed_wardrobe.has_outfit_with_name("[mc.business.name] - Sexy Uniform"):
        "Company wardrobe is already in your outfit manager"
        return

    "Choose you primary business color"
    menu:
        "Primary Color Red":
            python:
                upper_color = [.6, .1, .1, .9]
                under_color = [.9, .9, .9, .8]
                upper_color_dim = [.55, .15, 0.1, .9]

        "Primary Color Yellow":
            python:
                upper_color = [.8, .7, .1, .9]
                under_color = [.15, .15, .15, .8]                
                upper_color_dim = [.7, .6, 0, .9]

        "Primary Color Blue":
            python:
                upper_color = [.1, .15, .55, .9]
                under_color = [.8, .7, .1, .8]                
                upper_color_dim = [0, 0.05, .45, .9]

    python:
        lower_color = [.1, .1, .1, .9]
        uniform_mode = "under"

        normalu = Outfit("[mc.business.name] - Normal Underwear")
        normalu.add_upper(bralette.get_copy(), under_color)
        normalu.add_lower(cute_panties.get_copy(), under_color)
        mc.save_design(normalu, normalu.name, outfit_type = uniform_mode)

        normalu = Outfit("[mc.business.name] - Relaxed Underwear")
        normalu.add_upper(strapless_bra.get_copy(), under_color)
        normalu.add_lower(lace_panties.get_copy(), under_color)
        normalu.add_feet(high_socks.get_copy(), under_color)
        mc.save_design(normalu, normalu.name, outfit_type = uniform_mode)

        normalu = Outfit("[mc.business.name] - Sexy Underwear")
        normalu.add_upper(lace_bra.get_copy(), under_color)
        normalu.add_lower(lace_panties.get_copy(), under_color)
        normalu.add_feet(thigh_highs.get_copy(), under_color)
        mc.save_design(normalu, normalu.name, outfit_type = uniform_mode)

        normalu = Outfit("[mc.business.name] - Provocative Underwear")
        normalu.add_upper(thin_bra.get_copy(), under_color)
        normalu.add_lower(thong.get_copy(), under_color)
        normalu.add_feet(fishnets.get_copy(), under_color)
        mc.save_design(normalu, normalu.name, outfit_type = uniform_mode)

        normalu = Outfit("[mc.business.name] - Risque Underwear")
        normalu.add_upper(corset.get_copy(), under_color)
        normalu.add_lower(tiny_g_string.get_copy(), under_color)
        normalu.add_feet(fishnets.get_copy(), under_color)
        mc.save_design(normalu, normalu.name, outfit_type = uniform_mode)

        normalu = Outfit("[mc.business.name] - Slutty Underwear")
        normalu.add_lower(tiny_g_string.get_copy(), under_color)
        normalu.add_feet(garter_with_fishnets.get_copy(), under_color)
        normalu.add_accessory(heavy_eye_shadow.get_copy(), [0,0,0,.8])
        normalu.add_accessory(light_eye_shadow.get_copy(), upper_color)
        mc.save_design(normalu, normalu.name, outfit_type = uniform_mode)

        normalu = Outfit("[mc.business.name] - Commando Underwear")
        normalu.add_feet(fishnets.get_copy(), under_color)
        normalu.add_accessory(heavy_eye_shadow.get_copy(), [0,0,0,.8])
        normalu.add_accessory(light_eye_shadow.get_copy(), upper_color)
        normalu.add_accessory(lipstick.get_copy(), [0.6,0.1,0.1,0.8])
        mc.save_design(normalu, normalu.name, outfit_type = uniform_mode)

        uniform_mode = "over"

        normalo = Outfit("[mc.business.name] - Normal Overwear")
        normalo.add_lower(pencil_skirt.get_copy(), lower_color)
        normalo.add_upper(dress_shirt.get_copy(), upper_color)
        normalo.add_feet(slips.get_copy(), upper_color)
        mc.save_design(normalo, normalo.name, outfit_type = uniform_mode)

        normalo = Outfit("[mc.business.name] - Pants Overwear")
        normalo.add_upper(dress_shirt.get_copy(), upper_color)
        normalo.add_upper(vest.get_copy(), lower_color)
        normalo.add_lower(suitpants.get_copy(), lower_color)
        normalo.add_feet(slips.get_copy(), upper_color)
        mc.save_design(normalo, normalo.name, outfit_type = uniform_mode)

        normalo = Outfit("[mc.business.name] - Relaxed Overwear")
        normalo.add_lower(pencil_skirt.get_copy(), lower_color)
        normalo.add_upper(lace_crop_top.get_copy(), upper_color)
        normalo.add_feet(boot_heels.get_copy(), upper_color)
        mc.save_design(normalo, normalo.name, outfit_type = uniform_mode)

        normalo = Outfit("[mc.business.name] - Sexy Overwear")
        normalo.add_lower(pencil_skirt.get_copy(), lower_color)
        normalo.add_upper(business_vest.get_copy(), upper_color)
        normalo.add_feet(boot_heels.get_copy(), upper_color)
        mc.save_design(normalo, normalo.name, outfit_type = uniform_mode)

        normalo = Outfit("[mc.business.name] - Fitness Overwear")
        normalo.add_upper(sweater.get_copy(), upper_color)
        normalo.add_lower(leggings.get_copy(), lower_color)
        normalo.add_feet(sneakers.get_copy(), upper_color)
        mc.save_design(normalo, normalo.name, outfit_type = uniform_mode)

        normalo = Outfit("[mc.business.name] - Provocative Overwear")
        normalo.add_lower(belted_skirt.get_copy(), lower_color)
        normalo.add_upper(belted_top.get_copy(), upper_color)
        normalo.add_feet(high_heels.get_copy(), upper_color)
        mc.save_design(normalo, normalo.name, outfit_type = uniform_mode)

        normalo = Outfit("[mc.business.name] - Hotpants Overwear")
        normalo.add_upper(tanktop.get_copy(), upper_color)
        normalo.add_lower(jean_hotpants.get_copy(), lower_color)
        normalo.add_feet(heels.get_copy(), upper_color)
        mc.save_design(normalo, normalo.name, outfit_type = uniform_mode)

        normalo = Outfit("[mc.business.name] - Risque Overwear")
        normalo.add_lower(mini_skirt.get_copy(), lower_color)
        normalo.add_upper(business_vest.get_copy(), upper_color)
        normalo.add_feet(high_heels.get_copy(), upper_color)
        mc.save_design(normalo, normalo.name, outfit_type = uniform_mode)

        uniform_mode = "full"
        normalf = Outfit("[mc.business.name] - Normal Uniform")
        normalf.add_upper(bralette.get_copy(), under_color)
        normalf.add_upper(dress_shirt.get_copy(), upper_color)
        normalf.add_lower(cute_panties.get_copy(), under_color)
        normalf.add_lower(pencil_skirt.get_copy(), lower_color)
        normalf.add_feet(slips.get_copy(), upper_color)
        normalf.add_accessory(lipstick.get_copy(), [0.6,0.1,0.1,0.8])
        mc.save_design(normalf, normalf.name, outfit_type = uniform_mode)

        normalf = Outfit("[mc.business.name] - Normal Pants Uniform")
        normalf.add_upper(bralette.get_copy(), under_color)
        normalf.add_upper(dress_shirt.get_copy(), upper_color)
        normalf.add_upper(vest.get_copy(), lower_color)
        normalf.add_lower(cute_panties.get_copy(), under_color)
        normalf.add_lower(suitpants.get_copy(), lower_color)
        normalf.add_feet(slips.get_copy(), upper_color)
        normalf.add_accessory(lipstick.get_copy(), [0.6,0.1,0.1,0.8])
        mc.save_design(normalf, normalf.name, outfit_type = uniform_mode)

        normalf = Outfit("[mc.business.name] - Sexy Uniform")
        normalf.add_upper(business_vest.get_copy(), upper_color)
        normalf.add_lower(lace_panties.get_copy(), under_color)
        normalf.add_lower(pencil_skirt.get_copy(), lower_color)
        normalf.add_feet(thigh_highs.get_copy(), under_color)
        normalf.add_feet(boot_heels.get_copy(), upper_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), [0.1,0.2,0.7,.9])
        normalf.add_accessory(lipstick.get_copy(), [0.6,0.1,0.1,0.8])
        mc.save_design(normalf, normalf.name, outfit_type = uniform_mode)

        normalf = Outfit("[mc.business.name] - Fitness Uniform")
        normalf.add_upper(sweater.get_copy(), upper_color)
        normalf.add_lower(lace_panties.get_copy(), under_color)
        normalf.add_lower(leggings.get_copy(), lower_color)
        normalf.add_feet(sneakers.get_copy(), upper_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), [0.1,0.2,0.7,.9])
        normalf.add_accessory(lipstick.get_copy(), [0.6,0.1,0.1,0.8])
        mc.save_design(normalf, normalf.name, outfit_type = uniform_mode)

        normalf = Outfit("[mc.business.name] - Hotpants Uniform")
        normalf.add_upper(tanktop.get_copy(), upper_color)
        normalf.add_lower(tiny_lace_panties.get_copy(), under_color)
        normalf.add_lower(jean_hotpants.get_copy(), lower_color)
        normalf.add_feet(heels.get_copy(), upper_color)
        normalf.add_feet(thigh_highs.get_copy(), under_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), [0.1,0.2,0.7,.9])
        normalf.add_accessory(lipstick.get_copy(), [0.6,0.1,0.1,0.8])
        mc.save_design(normalf, normalf.name, outfit_type = uniform_mode)

        normalf = Outfit("[mc.business.name] - Risque Uniform")
        normalf.add_lower(mini_skirt.get_copy(), lower_color)
        normalf.add_upper(business_vest.get_copy(), upper_color)
        normalf.add_feet(garter_with_fishnets.get_copy(), under_color)
        normalf.add_feet(high_heels.get_copy(), upper_color)
        normalf.add_accessory(heavy_eye_shadow.get_copy(), [0,0,0,.8])
        normalf.add_accessory(light_eye_shadow.get_copy(), [0,0,0,1])
        normalf.add_accessory(lipstick.get_copy(), [0.6,0.1,0.1,0.8])
        mc.save_design(normalf, normalf.name, outfit_type = uniform_mode)

        normalf = Outfit("[mc.business.name] - Slutty Uniform")
        normalf.add_upper(two_part_dress.get_copy(), lower_color)
        normalf.add_upper(vest.get_copy(), upper_color)
        normalf.add_feet(fishnets.get_copy(), under_color)
        normalf.add_feet(high_heels.get_copy(), upper_color)
        normalf.add_accessory(wide_choker.get_copy(), upper_color_dim)
        normalf.add_accessory(heavy_eye_shadow.get_copy(), [0,0,0,.8])
        normalf.add_accessory(light_eye_shadow.get_copy(), [0,0,0,1])
        normalf.add_accessory(blush.get_copy(), [0.76, 0.376, 0.368, 0.8])
        normalf.add_accessory(lipstick.get_copy(), [0.6,0.1,0.1,0.8])
        mc.save_design(normalf, normalf.name, outfit_type = uniform_mode)

        company_wardrobe_loaded = True
    
    "Company wardrobe complete. Check your outfit manager."
    return
