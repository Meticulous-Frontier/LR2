init 2:
    screen aspect_grid(the_thing, given_xanchor = 0.5, given_xalign = 0.5): #Note: This can be given either a trait or a serum, since both have aspect info.
        default tsize = 16
        frame:
            background None
            xanchor given_xanchor
            xalign given_xalign
            margin 0,0,0,0
            padding 0,0,0,0

            hbox:
                spacing 10
                if the_thing.tier > mc.business.max_serum_tier:
                    text "Tier: {color=#fb6868}" + str(the_thing.tier) + "{/color}" style "menu_text_style" size tsize
                else:
                    text "Tier: " + str(the_thing.tier) style "menu_text_style" size tsize
                text "Ment: " + str(the_thing.mental_aspect) style "menu_text_style" size tsize color "#387aff"
                text "Phys: " + str(the_thing.physical_aspect) style "menu_text_style" size tsize color "#00AA00"
                text "Sex: " + str(the_thing.sexual_aspect) style "menu_text_style" size tsize color "#FFC0CB"
                text "Med: " + str(the_thing.medical_aspect) style "menu_text_style" size tsize color "#FFFFFF"
                text "Flaw: " + str(the_thing.flaws_aspect) style "menu_text_style" size tsize color "#AAAAAA"
                text "Attn: " + str(the_thing.attention) style "menu_text_style" size tsize color "#FF6249"
