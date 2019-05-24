init 1400 python:
    def salon_manager_possessive_titles(person):
        valid_possessive_titles = [wild_titles(person)]
        valid_possessive_titles.append("My stylist")
        if person.sluttiness > 50:
            valid_possessive_titles.append("My intimate stylist")
        return valid_possessive_titles

    def create_salon_manager():
        # Wardrobe for employees in the salon
        salon_wardrobe = wardrobe_from_xml("Salon_Wardrobe")
        global salon_manager
        salon_manager = create_random_person(name = "Ophelia", last_name = "von Friseur", height = .9, age = renpy.random.randint(21,30), body_type = "thin_body",
            personality = salon_manager_personality, job = "Hair Stylist", starting_wardrobe = salon_wardrobe, eyes="blue", start_sluttiness = 10,
            possessive_title = "My stylist")

        # We want whoever the salon_manager is to be in the salon during work hours.
        salon_manager.schedule[1] = mall_salon
        salon_manager.schedule[2] = mall_salon
        salon_manager.schedule[3] = mall_salon
        return

    salon_manager_personality = Personality("salon manager", default_prefix = "wild", #Based on wild style personality
        common_likes = ["skirts", "small talk", "the weekend", "the colour purple", "makeup", "hiking", "flirting"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "giving head", "anal sex", "public sex", "skimpy outfits", "anal sex", "showing her tits", "showing her ass", "being submissive", "creampies", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "the colour yellow", "supply work", "conservative outfits", "work uniforms", "pants"],
        common_sexy_dislikes = ["taking control", "risking getting pregnant"],
        titles_function = wild_titles, possessive_titles_function = salon_manager_possessive_titles, player_titles_function = wild_player_titles)
