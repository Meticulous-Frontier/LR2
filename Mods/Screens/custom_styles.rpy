init -5:
    define persistent.display_text_size = 20

    style nvl_dialogue:
        line_spacing 4
    style say_dialogue:
        line_spacing 4

    python:
        def set_text_size(new_size):
            setattr(style.get("serum_text_style"), "size", new_size)
            setattr(style.get("serum_text_style_header"), "size", new_size + 2)
            setattr(style.get("serum_text_style_traits"), "size", new_size - 2)
            setattr(style.get("textbutton_green_style"), "size", new_size - 2)
            setattr(style.get("custom_outfit_style"), "size", new_size)
            setattr(style.get("textbutton_style"), "size", new_size + 2)
            setattr(style.get("textbutton_text_style"), "size", new_size + 2)
            setattr(style.get("menu_text_style"), "size", new_size - 2)
            setattr(style.get("menu_text_style_left"), "size", new_size - 2)
            style.rebuild()



init -2 style serum_text_style: # General text style used in the serum screens.
    text_align 0.5
    size persistent.display_text_size
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    xalign 0.5

init -2 style serum_background_style: # General text style used in the serum screens.
    padding (5,5)
    margin (5,5)
    background "#0a142688"
    insensitive_background "#171717"
    hover_background "#143869"

init -2 style serum_textbutton_style_positive: # Used for positive trait / serum slugs
    margin (2,2)
    background "#43B197"
    insensitive_background "#171717"
    hover_background "#143869"

init -2 style textbutton_no_padding: # Textbutton without padding
    margin (2,2)
    background "#0a142688"
    insensitive_background "#171717"
    hover_background "#143869"

init -2 style serum_textbutton_style_negative: # Used for negative trait / serum slugs
    margin (2,2)
    background "#B14365"
    insensitive_background "#171717"
    hover_background "#143869"

init -2 style serum_textbutton_style_header: # Used for header / title boxes NOTE: Make this different later to easier distinguish
    padding (5,5)
    margin (5,5)
    background "#0a142688"
    insensitive_background "#171717"
    hover_background "#143869"

init -2 style serum_text_style_header: # Increased text size for headers
    text_align 0.5
    size (persistent.display_text_size + 2)
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    bold True
    xalign 0.5

init -2 style serum_text_style_traits: # Unaligned text style for traits in the serum_tooltip screen
    size (persistent.display_text_size - 2)
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    text_align 0.5
    xalign 0.5
    line_spacing 2
    yoffset 2

init -2 style textbutton_no_padding_highlight: # Textbutton without padding
    margin (2,2)
    background "#0a142688"
    insensitive_background "#171717"
    hover_background "#143869"

init -2 style custom_outfit_style: ##The text style used for text inside of the outfit manager.
    size persistent.display_text_size
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    insensitive_color "#dddddd"
    hover_color "#ffffff"
    bold False
    italic False

init 2 style textbutton_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    size (persistent.display_text_size + 2)
    margin (2, 2)
    background "#0a142688"
    insensitive_background "#171717"
    hover_background "#143869"

init 2 style textbutton_text_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    size (persistent.display_text_size + 2)
    italic False
    bold False
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    text_align 0.5
    line_spacing 4
    yoffset 4

init 2 style transparent_style:
    background None
    padding (5, 0)

init 2 style outfit_description_style is textbutton_text_style:
    size 18

init 2 style menu_text_style:
    size (persistent.display_text_size - 2)
    italic False
    bold False
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    text_align 0.5
    line_spacing 2
    yoffset 2

init 2 style menu_text_style_left:
    size (persistent.display_text_size - 2)
    italic False
    bold False
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    line_spacing 2
    text_align 0.0
    yoffset 2

init 2 style menu_text_title_style is menu_text_style:
    font "Mods/Core/Fonts/ethnocentric rg.ttf"

init 2 style menu_text_header_style is menu_text_title_style:
    size (persistent.display_text_size + 10)
    yoffset 0
    line_spacing 4
    text_align 0.5
    xalign 0.5

init 2 style float_text:
    size 24
    italic False
    bold False
    outlines [(2,"#222222",0,0)]
    yalign 0.5
