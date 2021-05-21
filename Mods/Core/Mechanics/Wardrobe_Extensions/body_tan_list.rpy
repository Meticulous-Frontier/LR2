init 2 python:
    tan_list = []

    no_tan = Clothing("No Tan", 1, False, False, "no_tan", False, False, 0, is_extension = True, display_name = "no tan")
    tan_list.append(no_tan)

    normal_tan_bottom = Clothing("Normal Tan Bottom", 1, False, False, "Lace_Panties", False, True, 0, tucked = True, is_extension = False, opacity_adjustment = 0.3, whiteness_adjustment = .3, display_name = "normal tan bottom")
    normal_tan = Clothing("Normal Tan", 1, False, False, "Lace_Bra", True, False, 0, has_extension = normal_tan_bottom, tucked = True, opacity_adjustment = 0.3, whiteness_adjustment = .3, display_name = "normal tan")
    tan_list.append(normal_tan)

    sexy_tan_bottom = Clothing("Sexy Tan Bottom", 1, False, False, "Panties", False, True, 0, tucked = True, is_extension = False, opacity_adjustment = 0.3, whiteness_adjustment = .3, display_name = "sexy tan bottom")
    sexy_tan = Clothing("Sexy Tan", 1, False, False, "Strapless_Bra", True, False, 0, has_extension = sexy_tan_bottom, tucked = True, opacity_adjustment = 0.3, whiteness_adjustment = .3, display_name = "sexy tan")
    tan_list.append(sexy_tan)

    one_piece_tan = Clothing("One Piece Tan", 1, False, False, "Lingerie_One_Piece", True, False, 0, tucked = True, opacity_adjustment = 0.3, display_name = "one piece tan")
    tan_list.append(one_piece_tan)

    slutty_tan = Clothing("Slutty Tan", 1, False, False, "Thong", False, True, 0, tucked = True, opacity_adjustment = 0.3, whiteness_adjustment = .5, display_name = "slutty tan")
    tan_list.append(slutty_tan)
