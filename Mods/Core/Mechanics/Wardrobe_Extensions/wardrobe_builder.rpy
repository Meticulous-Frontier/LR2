init 5 python:
    from collections import OrderedDict

    #def casual_sex_mod_initialization(action_mod):
    university_wardrobe = wardrobe_from_xml("University_Wardrobe")

    color_clothing_map = {
        "Jean_Hotpants": ["the colour black", "the colour blue", "the colour brown", "the colour white"],
        "Daisy_Dukes" : ["the colour black", "the colour blue", "the colour brown", "the colour white"],
        "Jeans" : ["the colour black", "the colour blue", "the colour brown", "the colour white"],
        "Suit_Pants" : ["the colour black", "the colour blue", "the colour brown", "the colour white", "the colour red", "the colour yellow", "the colour green"],
        "Capris" : ["the colour black", "the colour blue", "the colour brown", "the colour white"],
        "Pencil_Skirt": ["the colour black", "the colour blue", "the colour brown", "the colour white", "the colour red", "the colour yellow", "the colour green"],
        "Short_Socks" : ["the colour black", "the colour white", "the colour red"],
        "Long_Socks" : ["the colour black", "the colour white", "the colour red"],
        "High_Socks" : ["the colour black", "the colour white", "the colour red", "the colour pink", "the colour yellow"],
        "Slips": ["the colour black", "the colour white", "the colour brown"],
        "Shoes" : ["the colour black", "the colour white", "the colour brown"],
        "Sneakers" : ["the colour black", "the colour white", "the colour red"],
        "Sandal_Heels": ["the colour black", "the colour white", "the colour red", "the colour brown"],
        "Heels": ["the colour black", "the colour white", "the colour red", "the colour brown"],
        "High_Heels": ["the colour black", "the colour white", "the colour red", "the colour brown"],
        "Boot_Heels": ["the colour black", "the colour white", "the colour red", "the colour brown"],
        "High_Boots": ["the colour black", "the colour white", "the colour red", "the colour brown"],
        "Gold_Earings": ["the colour yellow"],
        "Copper_Bracelet": ["the colour yellow"],
        "Diamond_Ring": ["the colour yellow"],
        "Copper_Ring_Set": ["the colour yellow"],
        "Spiked_Bracelet": ["the colour white"],
        "Spiked_Choker": ["the colour white"],
    }

    #Use this to define a set of neutral colors, useful for colors that match most anything else.
    neutral_colors = {
        "khaki": [.765, .69, .569, .95],
        "swiss coffee": [.859, .331, .321, .95], #wut? this is salmon colored lol
        "light grey": [.827, .827, .827, .95],
        "cotton white": [.992, .953, .918, .95],
        "dark grey": [.365, .365, .365, .95],
        "midnight black": [.15, .15, .15, .95]
    }

    neutral_palette = {
        "dark denim": [0, .278, .671, .95],
        "denim": [.082, .376, .741, .95],
        "light denim": [.365, .678, .925, .95],
        "midnight black": [.15, .15, .15, .95],
        "khaki": [.765, .69, .569, .95],
        "dark grey": [.365, .365, .365, .95],
        "indian yellow": [.89, .659, .341, .95],
        "grey": [.502, .502, .502, .95],
        "light grey": [.827, .827, .827, .95],
        "sky blue": [.529, .808, .922, 0.95],
        "antique white": [.98, .922, .843, .95],
        "white smoke": [.95, .95, .95, .95],
        "light beige": [.94, .94, .78, .95],
        "leather": [.384, .29, .18, .95],
        "mocha": [.514, .373, .345, .95],
        "charcoal": [.212, .271, .31, .95],
        "scarlet": [1, .141, .0, .95],    #Looks decent for some patterns, might have to delete
        "pale pink": [.98, .885, .867, .95]
    }

    neutral_color_map = {
    "Jeans": ["dark denim", "denim", "light denim", "midnight black"],
    "Suit_Pants": ["midnight black", "khaki", "grey"],
    "Capris": ["dark denim", "denim", "dark grey"],
    "Leggings": ["midnight black", "dark grey"],
    "Leggings_Pattern": ["pale pink", "light grey", "white smoke"],
    "Jean_Hotpants": ["dark denim", "denim", "light denim", "midnight black", "dark grey"],
    "Booty_Shorts": ["midnight black", "dark grey"],
    "Daisy_Dukes": ["light denim", "sky blue"],

    "Long_Skirt": ["midnight black"],
    "Pencil_Skirt": ["midnight black", "dark grey", "grey", "khaki", "white smoke"],
    "Lace_Skirt": ["midnight black", "white smoke", "light grey"],
    "Skirt": ["khaki", "light grey", "light beige", "white smoke"],
    "Belted_Skirt": ["khaki", "grey", "light grey"],
    "Belted_Skirt_Pattern": ["leather", "dark grey"],
    "Mini_Skirt": ["khaki", "dark grey", "white smoke"],
    "Micro_Skirt": ["midnight black", "light grey", "white smoke"],

    "Lab_Coat": ["midnight black", "white smoke", "light grey"],
    "Suit_Jacket": ["midnight black", "white smoke", "dark denim", "dark grey"],
    "Vest": ["midnight black", "white smoke", "light grey", "leather"],

    "Short_Socks": ["white smoke", "light grey", "midnight black"],
    "Long_Socks": ["midnight black", "white smoke"],
    "High_Socks": ["midnight black", "white smoke", "light grey"],
    "Thigh_Highs": ["midnight black", "white smoke", "light grey", "mocha"],
    "Fishnets": ["midnight black", "white smoke", "dark grey"],
    "Garter_and_Fishnets": ["charcoal", "dark grey", "grey", "white smoke"],
    "Garter_and_Fishnets_Pattern": ["charcoal", "white smoke"],

    "Sandles": ["white smoke", "midnight black", "leather", "grey"],
    "Shoes": ["leather", "light grey"],
    "Slips": ["leather", "white smoke", "midnight black", "mocha", "dark grey"],
    "Sneakers": ["grey", "white smoke", "light beige"],
    "Sneakers_Pattern": ["white smoke"],
    "Sandal_Heels": ["midnight black", "grey", "white smoke", "light beige"],
    "Pumps": ["white smoke", "charcoal"],
    "Heels": ["midnight black", "charcoal", "white smoke"],
    "High_Heels": ["midnight black", "white smoke", "grey"],
    "Boot_Heels": ["leather", "grey"],
    "High_Boots": ["charcoal", "leather"],
    "Thigh_Boots": ["charcoal", "leather", "light grey"],

    "Tshirt": ["midnight black", "dark grey", "white smoke"],
    "Tshirt_Pattern": ["grey", "light grey"],
    "Lace_Sweater": ["white smoke", "light grey", "midnight black"],
    "Long_Sweater": ["midnight black", "light grey", "white smoke"],
    "Sleveless_Top": ["midnight black", "dark grey", "white smoke"],
    "Long_Tshirt": ["midnight black", "white smoke", "dark grey"],
    "Long_Tshirt_Pattern": ["white smoke", "light grey", "light beige"],
    "Frilly_Longsleeve_Shirt": ["white smoke", "dark grey", "charcoal"],
    "Sweater": ["leather", "white smoke", "charcoal", "khaki"],
    "Belted_Top": ["leather", "khaki", "grey", "white smoke", "charcoal"],
    "Lace_Crop_Top": ["charcoal", "light beige", "light grey", "white smoke"],
    "Tanktop": ["leather", "white smoke", "grey", "midnight black"],
    "Camisole": ["midnight black", "dark grey", "white smoke"],
    "Long_Sleeve_Blouse": ["white smoke", "midnight black", "sky blue"],
    "Short_Sleeve_Blouse": ["charcoal", "white smoke", "light beige", "light grey"],
    "Wrapped_Blouse": ["charcoal", "light beige", "white smoke"],
    "Tube_Top": ["white smoke", "midnight black", "dark grey", "charcoal"],
    "Tie_Sweater": ["midnight black", "dark grey", "white smoke"],
    "Tie_Sweater_Pattern": ["scarlet", "pale pink", "light grey", "light beige"],
    "Dress_Shirt": ["charcoal", "grey", "white smoke"],
    "Tight_Vest": ["white smoke", "light beige", "dark grey", "charcoal"],

    "Wool_Scarf": ["khaki", "charcoal", "grey", "white smoke"],
    "Lace_Choker": ["charcoal", "white smoke", "dark grey", "pale pink"],
    "Wide_Choker": ["charcoal", "white smoke", "dark grey", "pale pink"],
    "Spiked_Choker": ["charcoal", "white smoke", "dark grey", "pale pink"],
    # "Necklace_Set"
    # "Gold_Chain_Necklace"
    # "Collar_Breed"    # probably just leave these collars alone...
    # "Collar_Cum_Slut"
    # "Collar_Fuck_Doll"

    "Forearm_Gloves": ["charcoal", "light beige", "light grey", "white smoke"],
    "Forearm_Gloves_Pattern": ["charcoal", "pale pink", "white smoke"],
    # "Copper_Bracelet"
    # "Gold_Bracelet"
    # "Spiked_Bracelet"
    # "Bead_Bracelet"
    # "Colourful_Bracelets"
    #
    # "Diamond_Ring"
    # "Garnet_Ring"
    # "Copper_Ring_Set"

    # "Chandelier_Earings" #TODO
    # "Gold_Earings"
    "Modern_Glasses": ["charcoal", "midnight black"],
    "Big_Glasses": ["charcoal", "midnight black"],
    "Sunglasses": ["charcoal", "midnight black"],
    "Head_Towel": ["white smoke"],
    # "Ball_Gag"
    # "Upper_Eye_Shadow"
    # "Full_Shimmer"
    # "Blush"
    # "Lipstick"


    "Underwear": ["charcoal", "white smoke", "dark grey", "pale pink"]
    }

    swap_bottoms_map = {
    "Jeans": long_skirt,
    "Suit_Pants": pencil_skirt,
    "Capris": skirt,
    "Leggings": belted_skirt,
    "Jean_Hotpants": belted_skirt,
    "Booty_Shorts": mini_skirt,
    "Daisy_Dukes": micro_skirt,

    "Long_Skirt": jeans,
    "Pencil_Skirt": suitpants,
    "Lace_Skirt": capris,
    "Skirt": capris,
    "Belted_Skirt": leggings,
    "Mini_Skirt": booty_shorts,
    "Micro_Skirt": daisy_dukes
    }

    coverup_upper_list = [lab_coat, suit_jacket, vest]
    coverup_lower_list = []

    def neutralize_item_colour(the_item, the_colour = None):
        if the_item == None:
            return None

        current_alpha = the_item.colour[3]

        if the_item in real_bra_list or the_item in panties_list:
            if the_colour:
                the_item.colour = the_colour
            else:
                the_item.colour = neutral_palette[get_random_from_list(neutral_color_map["Underwear"])]
            the_item.pattern = None
            the_item.colour[3] = current_alpha
            return the_item

        if the_item in dress_list and the_item not in real_dress_list:
            if the_colour:
                the_item.colour = the_colour
            else:
                the_item.colour = neutral_palette[get_random_from_list(neutral_color_map["Underwear"])]
            the_item.pattern = None
            the_item.colour[3] = current_alpha
            return the_item

        if the_item.proper_name in neutral_color_map.keys():
            the_item.colour = neutral_palette[get_random_from_list(neutral_color_map[the_item.proper_name])]
            the_item.colour[3] = current_alpha
            if the_item.proper_name == "Sneakers": #For sneakers we always set the pattern color to white (laces)
                the_item = the_item.get_copy() # get copy before applying pattern
                key_value = get_random_from_list(list(the_item.supported_patterns.keys()))
                the_item.pattern = the_item.supported_patterns[key_value]
                color_key = the_item.proper_name + "_Pattern"
                the_item.colour_pattern = neutral_palette[get_random_from_list(neutral_color_map[color_key])]
                the_item.colour_pattern[3] = current_alpha
            elif isinstance(the_item, Facial_Accessory):    #facial accessories don't have patterns
                pass
            elif the_item.pattern:
                color_key = the_item.proper_name + "_Pattern"
                if color_key in neutral_color_map.keys():
                    the_item.colour_pattern = neutral_palette[get_random_from_list(neutral_color_map[color_key])]
                    the_item.colour_pattern[3] = current_alpha
                else:
                    the_item.colour_pattern = the_item.colour   #Preserve the pattern to possibly colorize later

        return the_item

    def neutralize_full_outfit(the_outfit):
        for item in the_outfit.upper_body:
            neutralize_item_colour(item)
        for item in the_outfit.lower_body:
            neutralize_item_colour(item)
        for item in the_outfit.feet:
            neutralize_item_colour(item)
        for item in the_outfit.accessories:
            neutralize_item_colour(item)
        return the_outfit

    def swap_outfit_bottoms(the_outfit):
        for item in the_outfit.lower_body:
            if (item in real_pants_list or item in skirts_list) and item.proper_name in swap_bottoms_map.keys():
                swap_item = swap_bottoms_map[item.proper_name].get_copy()
                swap_item.colour = item.colour
                the_outfit.lower_body.remove(item)
                the_outfit.add_lower(swap_item)
                return the_outfit
        return the_outfit

    def enhance_existing_wardrobe(person, max_outfits):
        outfit_builder = WardrobeBuilder(person)

        while __builtin__.len(person.wardrobe.outfits) < max_outfits:    # add some generated outfits
            outfit = outfit_builder.build_outfit("FullSets", renpy.random.randint(2, 6) * 2)
            if outfit.has_overwear() and outfit_builder.approves_outfit_color(outfit):
                person.wardrobe.add_outfit(outfit)

        while __builtin__.len(person.wardrobe.overwear_sets) < max_outfits:    # add some generated outfits
            overwear = outfit_builder.build_outfit("OverwearSets", renpy.random.randint(2, 6) * 2)
            if overwear.is_suitable_overwear_set() and outfit_builder.approves_outfit_color(overwear):
                person.wardrobe.add_overwear_set(overwear)

        while __builtin__.len(person.wardrobe.underwear_sets) < max_outfits:    # add some generated outfits
            underwear = outfit_builder.build_outfit("UnderwearSets", renpy.random.randint(2, 6) * 2)
            if underwear.is_suitable_underwear_set() and outfit_builder.approves_outfit_color(underwear):
                person.wardrobe.add_underwear_set(underwear)

        return

    def add_make_up_to_outfit(person, outfit, make_up_score_boost = 0):
        # determine make-up colors based on skin-tone
        if person.body_images == black_skin:
            eye_shadow_colours = [[.569, .349, .263, .9], [0, .2, .4, .9], [.47, .318, .663, .9]]
            lipstick_colours = [[.569, .318, .212, .8], [.451, .416, .526, .8], [.492, .419, .384, .8]]
            blush_colours = [[.435, .306, .216, .6], [.588, .251, 0, .6], [.451, .412, .576, .6]]
        else:
            eye_shadow_colours = [[.1, .1, .12, .9], [.4, .5, .9, .9], [.644, .418, .273, .9]]
            lipstick_colours = [[.745, .117, .235, .8], [1, .5, .8, .8], [ .8, .26, .04, .8]]
            blush_colours = [[.34, .34, .32, .6], [1, .898, .706, .6], [.867, .627, .867, .6]]

        make_up_score = person.get_opinion_score("makeup") + make_up_score_boost
        if make_up_score > 0 or (make_up_score == 0 and renpy.random.randint(0, 4) == 0):
            make_up_score += renpy.random.randint(1, 2)
            if make_up_score > 0:
                outfit.add_accessory(lipstick.get_copy(), get_random_from_list(lipstick_colours))
            if make_up_score > 1:
                outfit.add_accessory(light_eye_shadow.get_copy(), get_random_from_list(eye_shadow_colours))
            if make_up_score > 2:
                outfit.add_accessory(blush.get_copy(), get_random_from_list(blush_colours))
            if make_up_score > 3:
                outfit.add_accessory(heavy_eye_shadow.get_copy(), get_random_from_list(eye_shadow_colours))
        return

    real_bra_list = [x for x in bra_list if x not in [cincher, heart_pasties]]
    real_pants_list = [x for x in pants_list if not x in [cop_pants]]
    real_shirt_list = [x for x in shirts_list if not x in [cop_blouse]]
    real_dress_list = [x for x in dress_list if x not in [bath_robe, lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, apron, nightgown_dress, sweater_dress]]
    only_socks_list = [x for x in socks_list if x not in [thigh_highs, fishnets, garter_with_fishnets]]
    real_pantyhose_list = [x for x in socks_list if x not in only_socks_list]

    class WardrobeBuilder():
        default_person = None

        preferences = {}
        preferences["skimpy outfits"] = {}
        preferences["skimpy outfits"]["upper_body"] = [two_part_dress, thin_dress, leotard, lace_sweater, belted_top, lace_crop_top, frilly_longsleeve_shirt, tanktop, tube_top, business_vest, kitty_babydoll]
        preferences["skimpy outfits"]["lower_body"] = [booty_shorts, jean_hotpants, daisy_dukes, belted_skirt, mini_skirt, micro_skirt]
        preferences['skimpy outfits']["feet"] = [thigh_highs, fishnets, garter_with_fishnets, pumps, heels, high_heels, thigh_high_boots]
        preferences["skimpy outfits"]["accessories"] = [lace_choker, wide_choker, spiked_choker]
        preferences["conservative outfits"] = {}
        preferences["conservative outfits"]["upper_body"] = [long_sweater, sleeveless_top, long_tshirt, camisole, long_sleeve_blouse, short_sleeve_blouse, tie_sweater, dress_shirt, sweater_dress, bra, bralette, sports_bra]
        preferences["conservative outfits"]["lower_body"] = [pencil_skirt, skirt, long_skirt, jeans, suitpants, panties, plain_panties, cotton_panties, boy_shorts, kitty_panties]
        preferences["conservative outfits"]["feet"] = [sandles, shoes, slips, sneakers, short_socks]
        preferences["conservative outfits"]["accessories"] = [wool_scarf]
        preferences["dresses"] = {}
        preferences["dresses"]["upper_body"] = real_dress_list
        preferences["skirts"] = {}
        preferences["skirts"]["lower_body"] = skirts_list
        preferences["pants"] = {}
        preferences["pants"]["lower_body"] = real_pants_list
        preferences["showing her tits"] = {}
        preferences["showing her tits"]["upper_body"] = [strapless_bra, lace_bra, strappy_bra, quarter_cup_bustier, cincher, heart_pasties, thin_dress, two_part_dress, pinafore, lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, lace_sweater, sweater, belted_top, tube_top, business_vest, suit_jacket, vest]
        preferences["showing her ass"] = {}
        preferences["showing her ass"]["upper_body"] = [two_part_dress, thin_dress, summer_dress, virgin_killer, frilly_dress, leotard, lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear]
        preferences["showing her ass"]["lower_body"] = [cute_panties, lace_panties, cute_lace_panties, tiny_lace_panties, thong, tiny_g_string, string_panties, strappy_panties, crotchless_panties, leggings, booty_shorts, jean_hotpants, daisy_dukes, micro_skirt]
        preferences["high heels"] = {}
        preferences["high heels"]["feet"] = [sandle_heels, pumps, heels, high_heels, boot_heels, thigh_high_boots]
        preferences["boots"] = {}
        preferences["boots"]["feet"] = [boot_heels, tall_boots, thigh_high_boots]
        preferences["makeup"] = {}
        preferences["makeup"]["accessories"] = [light_eye_shadow, heavy_eye_shadow, blush, lipstick]
        preferences['lingerie'] = {}
        preferences['lingerie']["upper_body"] = [lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, strapless_bra, lace_bra, thin_bra, strappy_bra, cincher, corset, heart_pasties]
        preferences['lingerie']["lower_body"] = [lace_panties, cute_lace_panties, tiny_lace_panties, thin_panties, thong, tiny_g_string, string_panties, strappy_panties]
        preferences['lingerie']["feet"] = [thigh_highs, fishnets, garter_with_fishnets]
        preferences['lingerie']['accessories'] = [lace_choker, wide_choker]

        matching_underwear = {}
        matching_underwear["Bralette"] = [boy_shorts, cute_lace_panties, tiny_lace_panties, thong, tiny_g_string]
        matching_underwear["Sports_Bra"] = [cotton_panties, panties, lace_panties]
        matching_underwear["Lace_Bra"] = [cute_lace_panties, lace_panties, tiny_lace_panties, thong, tiny_g_string, crotchless_panties]
        matching_underwear["Strappy_Bra"] = [strappy_panties]
        matching_underwear["Corset"] = [panties, thin_panties, thong, tiny_lace_panties, tiny_g_string, string_panties, crotchless_panties]
        matching_underwear["Kitty_Babydoll"] = [kitty_panties, thong, kitty_panties, strappy_panties, kitty_panties]
        matching_underwear["Cincher"] = [panties, thin_panties, thong, tiny_lace_panties, tiny_g_string, string_panties, crotchless_panties]

        color_prefs = {}
        color_prefs["the colour blue"] = OrderedDict([
            ("dark slate blue", [.282, .239, .545, .95]),
            ("dark denim", [0, .278, .671, .95]),
            ("denim", [.082, .376, .741, .95]),
            ("steel blue", [.0275, .51, .706, .95]),
            ("light denim", [.365, .678, .925, .95]),
            ("cornflower blue", [.392, .584, .929, .95]),
            ("sky blue", [.529, .808, .922, 0.95]),
        ])
        color_prefs["the colour yellow"] = OrderedDict([
            ("khaki", [.765, .69, .569, .95]),
            ("indian yellow", [.89, .659, .341, .95]),
            ("saffron", [.96, .77, .19, .95]),
            ("corn", [.98, .92, .36, .95]),
        ])
        color_prefs["the colour red"] = OrderedDict([
            ("bordeaux red", [.38, .118, .149, .95]),
            ("berry", [.478, .09, .071, .95]),
            ("sinopia", [.80, .26, .04, .95]),
            ("vermillion", [.890, .258, .203, .95]),
            ("debian red", [.843, .039, .325, .95]),
        ])
        color_prefs["the colour pink"] = OrderedDict([
            ("dark pink", [.906, .329, .502, .95]),
            ("hot pink", [1, .412, .706, .95]),
            ("cotton candy", [1, .733, .851, .95]),
            ("pale pink", [.98, .885, .867, .95]),
        ])
        color_prefs["the colour black"] = OrderedDict([
            ("midnight black", [.15, .15, .15, .95]),
            ("charcoal", [.212, .271, .31, .95]),
            ("dark grey", [.365, .365, .365, .95]),
            ("warm black", [0, .26, .36, .95]),
        ])
        color_prefs["the colour green"] = OrderedDict([
            ("army green", [.294, .325, .125, .95]),
            ("sea green", [.18, .545, .341, .95]),
            ("jade", [.0, .659, .43 , .95]),
            ("caribbean green", [.0, .8, .6, .95]),
            ("pistachio", [.576, .772, .447, .95]),
        ])
        color_prefs["the colour purple"] = OrderedDict([
            ("palatinate purple", [.41, .16, .38, .95]),
            ("dark lavender", [.45, .31, .59, .95]),
            ("mauve", [.878, .690, 1, .95]),
            ("rich lilac", [.714, .4, .824, .95]),
        ])
        color_prefs["the colour orange"] = OrderedDict([
            ("burnt orange", [.8, .33, 0, .95]),
            ("tigers eye", [.878, .552, .235, .95]),
            ("honey orange", [.89, .6, .16, .95]),
            ("swiss coffee", [.859, .331, .321, .95]),
        ])
        color_prefs["the colour white"] = OrderedDict([
            ("antique white", [.98, .922, .843, .95]),
            ("cotton white", [.992, .953, .918, .95]),
            ("white smoke", [.95, .95, .95, .95]),
            ("ghost white", [.97, .97, 1, .95]),
        ])
        color_prefs["the colour brown"] = OrderedDict([
            ("leather", [.384, .29, .18, .95]),
            ("coffee", [.435, .305, .215, .95]),
            ("saddle brown", [.451, .313, .235, .95]),
            ("mocha", [.514, .373, .345, .95]),
            ("khaki", [.765, .69, .569, .95]),
            ("chocolate noir", [.352, 0.239, .239, .95]),
            ("light beige", [.94, .94, .78, .95]),
        ])
        #color_prefs[""][""] = [, , , ]

        @staticmethod
        def clothing_in_preferences(topic, clothing):
            for layer in WardrobeBuilder.preferences[topic].keys():
                if clothing in WardrobeBuilder.preferences[topic][layer]:
                    return True
            return False

        @staticmethod
        def get_item_color(item, color, exclude_list = [], multiplier = 1.0):
            if item.proper_name in color_clothing_map:
                # exclude hate list
                available_list = list(set(color_clothing_map[item.proper_name]) - set(exclude_list))
                if not available_list:
                    # no color left revert to original list
                    available_list = color_clothing_map[item.proper_name]

                # color not match list
                if not WardrobeBuilder.get_color_opinion(color) in available_list:
                    color_set = WardrobeBuilder.color_prefs[get_random_from_list(available_list)]
                    color_name = get_random_from_list(color_set.keys())
                    return [color_set[color_name][0] * multiplier, color_set[color_name][1] * multiplier, color_set[color_name][2] * multiplier, color_set[color_name][3]]
            return [color[0] * multiplier, color[1] * multiplier, color[2] * multiplier, color[3]]

        @staticmethod
        def get_color_opinion(colour):
            color_name = closest_preference_color(Color(rgb=(colour[0], colour[1], colour[2])))
            for opinion in WardrobeBuilder.color_prefs:
                if color_name in WardrobeBuilder.color_prefs[opinion]:
                    return opinion

            return "the colour black" # default fallback

        earings_only_list = [chandelier_earings, gold_earings, modern_glasses]
        neckwear_without_collars = [x for x in neckwear_list if x.proper_name not in ["Collar_Breed", "Collar_Cum_Slut", "Collar_Fuck_Doll", "Wool_Scarf"]]

        def __init__(self, person):
            if person and isinstance(person, Person):
                self.person = person
            else:
                if self.default_person is None:
                    self.default_person = create_random_person(name ="Ema", last_name = "Hesire", age = 23, body_type = "thin_body", tits = "B")
                    self.default_person.opinions.clear() # reset opinions so every item has an equal chance
                    self.default_person.sexy_opinions.clear()

                self.person = self.default_person

            skirts_score = self.person.get_opinion_score("skirts")
            pants_score = self.person.get_opinion_score("pants")
            dress_score = self.person.get_opinion_score("dresses")

            # person hates all main clothing items, make her like skirts.
            if skirts_score + pants_score + dress_score == -6:
                self.person.opinions["skirts"] = [1, True]

        def validate_colors(self):
            for cp in sorted(self.color_prefs):
                for col in sorted(self.color_prefs[cp]):
                    name = WardrobeBuilder.get_color_opinion(self.color_prefs[cp][col])
                    # print(cp + " - " + col + " -> " + (name if name else "Unknown"))
            return

        def build_outfit(self, outfit_type, points, min_points = 0):
            if (outfit_type == "OverwearSets"):
                return self.build_overwear(points, min_points)
            if (outfit_type == "UnderwearSets"):
                return self.build_underwear(points, min_points)

            underwear = self.build_underwear(points, min_points)
            overwear = self.build_overwear(points, min_points)

            for item in underwear.upper_body:
                if overwear.can_add_upper(item):
                    overwear.add_upper(item)

            for item in underwear.lower_body:
                if overwear.can_add_lower(item):
                    overwear.add_lower(item)

            for item in underwear.feet:
                if overwear.can_add_feet(item):
                    overwear.add_feet(item)

            for item in underwear.accessories:
                if overwear.can_add_accessory(item):
                    overwear.add_accessory(item)

            # prevent any item from having no colour set
            for cloth in overwear.upper_body + overwear.lower_body + overwear.feet + overwear.accessories:
                if __builtin__.len(cloth.colour) < 4:
                    cloth.colour = [1, 1, 1, .5]    # transparant white is easy to spot for debuggin

            return overwear

        def get_hate_list(self):
            item_list = []
            for pref in self.preferences.keys() + self.color_prefs.keys():
                score = self.person.get_opinion_score(pref)
                if score == -2:
                    item_list.append(pref)
            return item_list

        def get_love_list(self):
            item_list = []
            for pref in self.preferences.keys() + self.color_prefs.keys():
                score = self.person.get_opinion_score(pref)
                if score == 2:
                    item_list.append(pref)
            return item_list

        def get_color_hate_list(self):
            item_list = []
            for pref in self.color_prefs.keys():
                score = self.person.get_opinion_score(pref)
                if score == -2:
                    item_list.append(pref)
            return item_list

        def approves_outfit_color(self, outfit):
            for clothing in outfit.feet + outfit.lower_body + outfit.upper_body:
                opinion_color = self.get_color_opinion(clothing.colour)
                if opinion_color in self.get_color_hate_list():
                    return False
            return True

        def build_overwear(self, points = 0, min_points = 0):
            def make_upper_item_transparent(item, points, colour):
                colour[3] = .95 + (renpy.random.randint(0, 5) / 100.0)
                if item.layer == 2 and item.slut_value > 0 and points >= 4 and item in real_shirt_list + real_dress_list:
                    colour[3] = .8 + (renpy.random.randint(0, 15) / 100.0)
                return item.get_copy(), colour

            def make_lower_item_transparent(item, points, colour):
                colour[3] = .95 + (renpy.random.randint(0, 5) / 100.0)
                if item.layer == 2 and item.slut_value > 0 and points >= 4 and item in skirts_list + [suitpants, leggings, booty_shorts]:
                    colour[3] = .8 + (renpy.random.randint(0, 15) / 100.0)
                return item.get_copy(), colour

            outfit = Outfit("Overwear")

            color_upper, color_lower, color_feet = self.get_main_color_scheme()
            upper_item_list = real_dress_list + real_shirt_list

            # find upper body item
            item = self.get_item_from_list("upper_body", self.build_filter_list(upper_item_list, points, min_points), points, ["not wearing anything"])
            if item:
                outfit.add_upper(*make_upper_item_transparent(item, points, self.get_item_color(item, color_upper, self.get_color_hate_list())))

            # we added a overlay item, so find a real upper item this time
            if item and item.layer == 3:
                item = self.get_item_from_list("upper_body", self.build_filter_list(upper_item_list, points, min_points, layers = [2]), points, ["not wearing anything"])
                if item:
                    outfit.add_upper(*make_upper_item_transparent(item, points, self.get_item_color(item, color_lower, self.get_color_hate_list())))

            # find lowerbody item
            if item is None or (not item.has_extension or item.has_extension.layer == 1):
                item = self.get_item_from_list("lower_body", self.build_filter_list(real_pants_list + skirts_list, points, min_points), points, ["not wearing anything"])
                if item:
                    outfit.add_lower(*make_lower_item_transparent(item, points, self.get_item_color(item, color_lower, self.get_color_hate_list(), 0.9)))

            # find feet item
            item = self.get_item_from_list("feet", self.build_filter_list(shoes_list, points, min_points))
            if item:
                outfit.add_feet(item, self.get_item_color(item, color_feet, self.get_color_hate_list(), 0.8))

            self.add_accessory_from_list(outfit, self.build_filter_list(self.earings_only_list, points, min_points, self.person.base_outfit.accessories), 3, color_lower)
            self.add_accessory_from_list(outfit, self.build_filter_list(rings_list, points, min_points, self.person.base_outfit.accessories), 3, color_lower)
            self.add_accessory_from_list(outfit, self.build_filter_list(bracelet_list, points, min_points, self.person.base_outfit.accessories), 3, color_upper)
            self.add_accessory_from_list(outfit, self.build_filter_list(self.neckwear_without_collars, points, min_points, self.person.base_outfit.accessories), 3, color_upper)

            outfit.update_name()

            return outfit

        def build_underwear(self, points = 0, min_points = 0):
            def make_upper_item_transparent(item, points, colour):
                colour[3] = .95 + (renpy.random.randint(0, 5) / 100.0)
                if points >= 8 and item.slut_value > 0 and item in [lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear] + real_bra_list:
                    colour[3] = .7 + (renpy.random.randint(0, 25) / 100.0)
                return item.get_copy(), colour

            def make_lower_item_transparent(item, points, colour):
                colour[3] = .95 + (renpy.random.randint(0, 5) / 100.0)
                if points >= 8 and item.slut_value > 0 and item in panties_list:
                    colour[3] = .7 + (renpy.random.randint(0, 25) / 100.0)
                return item.get_copy(), colour

            outfit = Outfit("Underwear")

            color_upper, color_lower, color_feet = self.get_main_color_scheme(match_percent = 80) # underwear mismatch is less likely

            # find upper body item
            item = self.get_item_from_list("upper_body", self.build_filter_list(real_bra_list + [lingerie_one_piece, lacy_one_piece_underwear, bodysuit_underwear], points, min_points), points, ["showing her tits", "not wearing underwear"])
            if item:
                outfit.add_upper(*make_upper_item_transparent(item, points, color_upper))

            # random chance of adding sexy underwear part (heart pasties / cincher)
            if renpy.random.randint(0, 3 - self.person.get_opinion_score("lingerie")) == 0:
                outfit.add_upper(*make_upper_item_transparent(get_random_from_list([cincher, heart_pasties]), points, color_upper))

            # find lower body item
            if not item or not item.has_extension:
                if item and item.proper_name in self.matching_underwear:
                    item = self.get_item_from_list("lower_body", self.build_filter_list(self.matching_underwear[item.proper_name], points, min_points), points, ["showing her ass", "not wearing underwear"])
                else:
                    item = self.get_item_from_list("lower_body", self.build_filter_list(panties_list, points, min_points), points, ["showing her ass", "not wearing underwear"])
                if item:
                    outfit.add_lower(*make_lower_item_transparent(item, points, color_lower if item in [cincher, heart_pasties] else color_upper))

            # random socks
            if renpy.random.randint(0, 1) == 0:
                if points >= 5:
                    item = self.get_item_from_list("feet", self.build_filter_list([x for x in socks_list if x not in [short_socks, medium_socks]], points, min_points))
                else:
                    item = self.get_item_from_list("feet", self.build_filter_list(socks_list, points, min_points))
                if item:
                    outfit.add_feet(item.get_copy(), color_feet)

            # random chance of adding outfit custom makeup (base on pref for make-up)
            if self.person.get_opinion_score("makeup") > -2 and renpy.random.randint(0, 4 - self.person.get_opinion_score("makeup")) == 0:
                # add makeup to outfit (overrides makeup in base_outfit)
                add_make_up_to_outfit(self.person, outfit)

            outfit.update_name()

            return outfit


        def build_filter_list(self, item_list, points, min_points = 0, filter_list = [], layers = [1, 2, 3]):
            # extend range until we have items
            while not any(filter(lambda x: x.slut_value >= min_points and x.slut_value <= points and x.layer in layers and x not in filter_list, item_list)):
                if min_points > 0:
                    min_points -= 1
                if points < 15:
                    points += 1

            return list(filter(lambda x: x.slut_value >= min_points and x.slut_value <= points and x.layer in layers, item_list))

        def add_accessory_from_list(self, outfit, filtered_list, chance, item_color = [.8, .1, .1, .95]):
            if renpy.random.randint(0, chance) == 0:
                item = get_random_from_list(filtered_list)
                if item:
                    outfit.add_accessory(item.get_copy(), self.get_item_color(item, item_color))
            return

        def get_main_color_scheme(self, match_percent = 60):
            primary_color = self.get_color()
            alternate_color = self.get_color(primary_color)

            col_choice = renpy.random.randint(0, 100)
            lower_percent = (100 - match_percent) // 2
            if col_choice < lower_percent:
                color_upper = primary_color
                color_lower = alternate_color
                color_feet = primary_color
            elif col_choice >= lower_percent and col_choice < match_percent:
                color_upper = primary_color
                color_lower = primary_color
                color_feet = alternate_color
            else:
                color_upper = primary_color
                color_lower = alternate_color
                color_feet = alternate_color

            return (color_upper, color_lower, color_feet)

        def get_item_from_list(self, item_group, filtered_list, points = 0, empty_item_opinions = [], no_pattern = False):
            weighted_list = self.build_weighted_list(item_group, filtered_list)

            for pref in self.preferences:
                if item_group in self.preferences[pref]:
                    if self.person.get_opinion_score(pref) == -2:
                        item_list = [x for x in weighted_list if x[0] not in self.preferences[pref][item_group]]
                        if item_list: # check if we have any items left, if not use original weighted list
                            weighted_list = item_list

            item = get_random_from_weighted_list(weighted_list)
            if not item:    # make sure we have an item from the list
                item = get_random_from_list(filtered_list)

            if no_pattern:
                return item

            # force pattern for certain items, others random 50/50
            if item and hasattr(item, "supported_patterns") and item.supported_patterns and (renpy.random.randint(0, 1) == 1 or item in [apron, breed_collar, cum_slut_collar, fuck_doll_collar]):
                item = item.get_copy() # get copy before applying pattern
                key_value = get_random_from_list(list(item.supported_patterns.keys()))
                item.pattern = item.supported_patterns[key_value]
                item.colour_pattern = self.get_color(item.colour)

            return item

        def build_weighted_list(self, item_group, filtered_list):
            item_list = []
            for item in filtered_list:
                item_list.append([item, 0])
            for pref in self.preferences:
                score = self.person.get_opinion_score(pref)
                for name in [x for x in self.preferences[pref] if x == item_group]:
                    for item in [x for x in self.preferences[pref][name] if x in filtered_list]:
                        [x for x in item_list if item in x][0][1] += (score + 2) ^ 3

            return [x for x in item_list if x[1] > 0]


        def get_color(self, base_color = None):
            def get_excluded(base_color):
                if base_color:
                    # prevents clashing colours
                    opinion_color = WardrobeBuilder.get_color_opinion(base_color)
                    if opinion_color == "the colour red":
                        return ["the colour pink", "the colour purple", "the colour brown"]
                    if opinion_color == "the colour pink":
                        return ["the colour red", "the colour purple", "the colour brown"]
                    if opinion_color == "the colour purple":
                        return ["the colour red", "the colour pink", "the colour blue"]
                    if opinion_color == "the colour blue":
                        return ["the colour purple"]
                    if opinion_color == "the colour orange":
                        return ["the colour yellow"]
                    if opinion_color == "the colour yellow":
                        return ["the colour orange"]
                    if opinion_color == "the colour brown":
                        return ["the colour black", "the colour pink", "the colour red"]
                    if opinion_color == "the colour black":
                        return ["the colour brown"]
                return []

            color_list = []
            for cp in [x for x in self.color_prefs if x not in get_excluded(base_color)]:
                score = self.person.get_opinion_score(cp)
                if score > -2: # don't append colors she hates
                    for col in self.color_prefs[cp]:
                        color_list.append([self.color_prefs[cp][col], (score + 2) ^ 3])

            # renpy.random.shuffle(color_list)
            return get_random_from_weighted_list([x for x in color_list if x[1] > 0])

        def change_color_theme(self, outfit, the_colour):
            coloured_outfit = outfit.get_copy()
            color_list = []
            neutral_list = []
            for col in self.color_prefs[the_colour]:
                color_list.append(self.color_prefs[the_colour][col])
            for col in neutral_colors:
                neutral_list.append(neutral_colors[col])
            main_colour = get_random_from_list(color_list)
            neutral_colour = get_random_from_list(neutral_list)
            if coloured_outfit.is_dress():
                for item in coloured_outfit.upper_body:
                    if item in real_dress_list:
                        item.colour = main_colour
                    elif item in shoes_list or item in real_pants_list:
                        item_colour = neutral_colour
            # testing
            for item in coloured_outfit.upper_body:
                item.colour = main_colour
            return coloured_outfit

        def apply_bottom_preference(self, outfit):
            swapped = False
            if outfit.has_pants() and self.person.get_opinion_score("skirts") > self.person.get_opinion_score("pants"): #Outfit has pants and girl prefers skirts
                outfit = swap_outfit_bottoms(outfit)
                swapped = True
            elif outfit.has_skirt() and self.person.get_opinion_score("skirts") < self.person.get_opinion_score("pants"):
                outfit = swap_outfit_bottoms(outfit)
                swapped = True
            return outfit, swapped

        def personalize_outfit(self, outfit, opinion_color = None, coloured_underwear = False, max_alterations = 0, main_colour = None, swap_bottoms = False, allow_skimpy = True, allow_coverup = True):
            def change_colour_alpha(new_colour, old_colour):
                alpha_blended = new_colour
                alpha_blended[3] = old_colour[3]
                return alpha_blended

            personal_outfit = outfit.get_copy()
            personal_outfit.remove_all_collars()
            personal_outfit.remove_all_cum()

            underwear_colour = None
            alterations = 0

            #First, get a theme color
            if opinion_color == None:
                if main_colour:
                    opinion_color = WardrobeBuilder.get_color_opinion(main_colour)
                elif renpy.random.randint(0,100) < 50:  #50% chance we go straight to a favorite color.
                    main_colour = self.get_color()
                    opinion_color = WardrobeBuilder.get_color_opinion(main_colour)
                else:
                    opinion_color = self.person.favorite_colour()

            color_list = []
            for col in self.color_prefs[opinion_color]:
                color_list.append(self.color_prefs[opinion_color][col])
            if main_colour == None:
                main_colour = get_random_from_list(color_list)

            if coloured_underwear:
                if renpy.random.randint(0,100) < 70: #70% chance to use similar color as outfit theme
                    underwear_colour = get_random_from_list(color_list)
                else:
                    color_list = []
                    underwear_colour = self.get_color(main_colour)
                    # for col in self.color_prefs[under_colour]:
                    #     color_list.append(self.color_prefs[under_colour][col])
                    # underwear_colour = get_random_from_list(color_list)

            #First alteration we look at is bottom swap. Allow it if alterations are allowed or if we specifically allow bottom swaps.
            if swap_bottoms:
                (personal_outfit, swapped) = self.apply_bottom_preference(personal_outfit)
                if swapped:
                    alterations += 1

            if allow_skimpy:
                if alterations < max_alterations and personal_outfit.is_dress() or personal_outfit.has_skirt():  #Next, if we are wearing a dress or skirt, have slutty girls have a chance to drop their panties.
                    if personal_outfit.get_full_outfit_slut_score() + 20 < self.person.sluttiness and renpy.random.randint(0, 1) == 1:
                        item = personal_outfit.get_panties()
                        if item:
                            personal_outfit.lower_body.remove(item)
                            alterations += 1

                if alterations < max_alterations and personal_outfit.has_pants() or personal_outfit.has_shirt():   #If the outfit has pants, have a chance to drop a layer off the top
                    if personal_outfit.get_full_outfit_slut_score() + 20 < self.person.sluttiness and renpy.random.randint(0, 1) == 1:
                        personal_outfit.remove_random_upper(top_layer_first = True)
                        alterations += 1

            #TODO determine if underwear is on, and if it is boring. If girl wants she can swap underwear for sexier set
            self.set_sexier_panties(personal_outfit, underwear_colour)
            self.set_sexier_bra(personal_outfit, underwear_colour)
            #Next, determine what kind of outfit this is.

            if personal_outfit.is_dress(): #If it is a dress, let the dress be the focal point of the outfit.
                # renpy.say ("", "Suitable dress set")
                for item in personal_outfit.upper_body:
                    if item in real_bra_list and coloured_underwear:
                        item.colour = change_colour_alpha(underwear_colour, item.colour)
                    elif item in real_dress_list:
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item)
                        if item in real_bra_list:
                            underwear_colour = item.colour  #If we neutralized the bra, makes sure we save the colour the give matching panties
                for item in personal_outfit.lower_body:
                    if item in panties_list and (coloured_underwear or underwear_colour):
                        item.colour = change_colour_alpha(underwear_colour, item.colour)
                    elif item in real_dress_list:
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item)
                for item in personal_outfit.feet:
                    if item.proper_name == "Sneakers":
                        neutralize_item_colour(item)
                        item.colour_pattern = change_colour_alpha(main_colour, item.colour_pattern)
                    else:
                        neutralize_item_colour(item)
                for item in personal_outfit.accessories:
                    neutralize_item_colour(item)


            elif personal_outfit.has_pants(): #This outfit has lower body pants covering.
                # renpy.say ("", "Suitable pants set")
                #Fist determine if we want to switch to a skirt. #TODO figure out how to do this
                #Next, figure out what kind of top we have. Regular, bra, or topless.
                if personal_outfit.tits_visible():   #Tits are on display, but she may have a top still. Colour her top (if there) and pants
                    for item in personal_outfit.upper_body:
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    for item in personal_outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = change_colour_alpha(underwear_colour, item.colour)
                        elif item in real_pants_list:
                            item.colour = change_colour_alpha(main_colour, item.colour)
                        else:
                            neutralize_item_colour(item)

                elif not personal_outfit.bra_covered(): #Bra is on display, use that for our colour theme. Bra is focal point of outfit, so neutralize pants
                    for item in personal_outfit.upper_body:
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    for item in personal_outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = change_colour_alpha(underwear_colour, item.colour)
                        elif item in real_pants_list:
                            neutralize_item_colour(item)
                        else:
                            neutralize_item_colour(item)
                else: #Assume a decent top is being worn. Top is the focal point of the outfit
                    for item in personal_outfit.upper_body:
                        if item in real_bra_list and coloured_underwear:
                            item.colour = change_colour_alpha(underwear_colour, item.colour)
                        elif item in shirts_list:
                            item.colour = change_colour_alpha(main_colour, item.colour)
                        else:
                            neutralize_item_colour(item)
                            if item in real_bra_list:
                                underwear_colour = item.colour
                    for item in personal_outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = change_colour_alpha(underwear_colour, item.colour)
                        elif item in real_pants_list:
                            neutralize_item_colour(item)
                        else:
                            neutralize_item_colour(item)

                for item in personal_outfit.feet:
                    if item.proper_name == "Sneakers":
                        neutralize_item_colour(item)
                        item.colour_pattern = main_colour
                    elif renpy.random.randint(0,100) < 30 and item in shoes_list: #Nomrally we neutralize feet, but have a chance at having a matching set of shooes
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item)
                for item in personal_outfit.accessories:
                    neutralize_item_colour(item)

            elif personal_outfit.has_skirt(): #This outfit has a skirt.
                # renpy.say ("", "Suitable skirt set")
                #Similar logic to pants. First determine if we should switch to pants
                #Next, determine what kind of top is being worn.
                if personal_outfit.tits_visible():   #Tits are on display, but she may have a top still. Colour her top (if there) and skirt
                    for item in personal_outfit.upper_body:
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    for item in personal_outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = change_colour_alpha(underwear_colour, item.colour)
                        elif item in skirts_list:
                            item.colour = change_colour_alpha(main_colour, item.colour)
                        else:
                            neutralize_item_colour(item)
                elif not personal_outfit.bra_covered(): #Bra is on display, use that for our colour theme. Bra is focal point of outfit, so neutralize skirt
                    for item in personal_outfit.upper_body:
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    for item in personal_outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = change_colour_alpha(underwear_colour, item.colour)
                        elif item in skirts_list:
                            neutralize_item_colour(item)
                        else:
                            neutralize_item_colour(item)
                else:   #She's wearing a full outfit. Probably top is focal point, but there is a CHANCE that she may decide to make the skirt the outfit focal point.
                    skirt_focus = renpy.random.randint(0,100) < 30  #30% chance for skirt focus
                    for item in personal_outfit.upper_body:
                        if item in real_bra_list and coloured_underwear:
                            item.colour = change_colour_alpha(underwear_colour, item.colour)
                        elif item in shirts_list and not skirt_focus:
                            item.colour = change_colour_alpha(main_colour, item.colour)
                        else:
                            neutralize_item_colour(item)
                            if item in real_bra_list:
                                underwear_colour = item.colour
                            elif item.pattern: #Item has pattern that we can use to colorize
                                item.colour_pattern = main_colour

                    for item in personal_outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = change_colour_alpha(underwear_colour, item.colour)
                        elif item in skirts_list:
                            if skirt_focus:
                                item.colour = change_colour_alpha(main_colour, item.colour)
                            else:
                                neutralize_item_colour(item)
                        else:
                            neutralize_item_colour(item)
                for item in personal_outfit.feet:
                    if item.proper_name == "Sneakers":
                        neutralize_item_colour(item)
                        item.colour_pattern = main_colour
                    elif renpy.random.randint(0,100) < 30 and item in shoes_list: #Nomrally we neutralize feet, but have a chance at having a matching set of shooes
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item)
                for item in personal_outfit.accessories:
                    neutralize_item_colour(item)

            #Next type of outfite: housewear. Girl comfy clothes general in game are some top with just panties or no panties. EG mom's apron, pajamas, etc.
            #With this outfit, tits will be covered. Make top the focal point.
            elif personal_outfit.has_shirt():
                # renpy.say ("", "Suitable comfy set")
                for item in personal_outfit.upper_body:
                    if item in real_bra_list and coloured_underwear:
                        item.colour = change_colour_alpha(underwear_colour, item.colour)
                    elif item in shirts_list:
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item)
                        if item in real_bra_list:
                            underwear_colour = item.colour

                for item in personal_outfit.lower_body:
                    if item in panties_list and (coloured_underwear or underwear_colour):
                        item.colour = change_colour_alpha(underwear_colour, item.colour)
                    else:
                        neutralize_item_colour(item)
                for item in personal_outfit.feet:
                    if item.proper_name == "Sneakers":
                        neutralize_item_colour(item)
                        item.colour_pattern = main_colour
                    elif renpy.random.randint(0,100) < 30 and item in shoes_list: #Nomrally we neutralize feet, but have a chance at having a matching set of shooes
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item)
                for item in personal_outfit.accessories:
                    neutralize_item_colour(item)

            #This outfit does not have lower or upper body covering. Could be just underwear or lingerie.
            #First, check and see if this is just an underwear set. In that case, colour all underwear as main color.
            #To differentiate between underwear and lingerie, check and see if it is classic underwear set via layers.
            #If bottom layer only, check sluttiness rating and access and for pantyhose vs socks and determine if we treat as just underwear or as lingerie
            elif personal_outfit.is_suitable_underwear_set() and not (personal_outfit.has_hose() and personal_outfit.get_underwear_slut_score() > 15):
                #Make underwear main color, neutralize everything else.
                # renpy.say ("", "Suitable underwear set")
                for item in personal_outfit.upper_body:
                    if item in real_bra_list:
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item)

                for item in personal_outfit.lower_body:
                    if item in panties_list:
                        item.colour = change_colour_alpha(main_colour,item.colour)
                    else:
                        neutralize_item_colour(item)
                for item in personal_outfit.feet:
                    neutralize_item_colour(item)
                for item in personal_outfit.accessories:
                    neutralize_item_colour(item)
            else: #This is for exciting, lingerie style outfits. Lingerie is generally completely color matching, maybe with only one or two neutral pieces.
                # renpy.say ("", "Suitable lingerie set")
                for item in personal_outfit.upper_body:
                    item.colour = change_colour_alpha(main_colour, item.colour)
                for item in personal_outfit.lower_body:
                    item.colour = change_colour_alpha(main_colour, item.colour)
                for item in personal_outfit.feet:
                    if item in socks_list and renpy.random.randint(0,100) < 70:
                        item.colour = change_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item)
                for item in personal_outfit.accessories:
                    neutralize_item_colour(item)
            return personal_outfit

        def set_sexier_panties(self, outfit, the_colour = None):
            panties = outfit.get_panties()
            if panties is None or panties.is_extension: # no panties or one-piece
                return False
            slut_tier = get_slut_tier(self.person)

            if slut_tier <= panties.slut_value:
                return False
            if slut_tier >= 4 and renpy.random.randint(0, 3) == 2: # high slut level chance for no panties
                outfit.remove_clothing(panties)
                return True

            new_panties = get_random_from_list([x for x in panties_list if x.slut_value == slut_tier])
            if new_panties:
                if the_colour is None:
                    new_panties.colour = panties.colour
                else:
                    new_panties.colour = the_colour
                outfit.remove_clothing(panties)
                outfit.add_lower(new_panties)
                return True
            return False

        def set_sexier_bra(self, outfit, the_colour = None):
            bra = outfit.get_bra()
            if bra is None or bra.has_extension: # no bra or one-piece
                return False
            slut_tier = get_slut_tier(self.person)
            if slut_tier <= bra.slut_value:
                return False

            panties = outfit.get_panties()
            if panties is None:    # when not wearing panties, also remove bra
                outfit.remove_clothing(bra)
                return True

            if slut_tier >= 4 and renpy.random.randint(0, 3) == 2: # high slut level chance for no bra
                outfit.remove_clothing(bra)
                return True

            new_bra = get_random_from_list([x for x in real_bra_list if x.slut_value == slut_tier])
            if new_bra:
                if the_colour is None:
                    new_bra.colour = bra.colour
                else:
                    new_bra.colour = the_colour
                outfit.remove_clothing(bra)
                outfit.add_upper(new_bra)
                return True
            return False
