init 2:
    screen aspect_grid(aspect_object, given_xanchor = 0.5, given_xalign = 0.5): #Note: This can be given either a trait or a serum, since both have aspect info.
        default tsize = 16
        frame:
            background None
            xanchor given_xanchor
            xalign given_xalign
            margin 0,0,0,0
            padding 0,0,0,0

            hbox:
                spacing 10
                if aspect_object.tier > mc.business.max_serum_tier:
                    text "Tier: {color=#fb6868}[aspect_object.tier]{/color}" style "menu_text_style" size tsize
                else:
                    text "Tier: [aspect_object.tier]" style "menu_text_style" size tsize
                text "Ment: [aspect_object.mental_aspect]" style "menu_text_style" size tsize color "#387aff"
                text "Phys: [aspect_object.physical_aspect]" style "menu_text_style" size tsize color "#00AA00"
                text "Sex: [aspect_object.sexual_aspect]" style "menu_text_style" size tsize color "#FFC0CB"
                text "Med: [aspect_object.medical_aspect]" style "menu_text_style" size tsize color "#FFFFFF"
                text "Flaw: [aspect_object.flaws_aspect]" style "menu_text_style" size tsize color "#AAAAAA"
                text "Attn: [aspect_object.attention]" style "menu_text_style" size tsize color "#FF6249"
