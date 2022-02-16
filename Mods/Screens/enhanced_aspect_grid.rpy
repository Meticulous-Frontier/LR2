init 2:
    screen aspect_grid(the_thing, given_xanchor = 0.5, given_xalign = 0.5): #Note: This can be given either a trait or a serum, since both have aspect info.
        grid 7 1:
            xanchor given_xanchor
            xalign given_xalign
            if the_thing.tier > mc.business.max_serum_tier:
                text "Tier: {color=#fb6868}" + str(the_thing.tier) + "{/color}" style "menu_text_style" size 14
            else:
                text "Tier: " + str(the_thing.tier) style "menu_text_style" size 14
            text "Ment: " + str(the_thing.mental_aspect) style "menu_text_style" size 14 color "#0049d8"
            text "Phys: " + str(the_thing.physical_aspect) style "menu_text_style" size 14 color "#00AA00"
            text "Sex: " + str(the_thing.sexual_aspect) style "menu_text_style" size 14 color "#FFC0CB"
            text "Medic: " + str(the_thing.medical_aspect) style "menu_text_style" size 14 color "#FFFFFF"
            text "Flaw: " + str(the_thing.flaws_aspect) style "menu_text_style" size 14 color "#BBBBBB"
            text "Attn: " + str(the_thing.attention) style "menu_text_style" size 14 color "#FF6249"
