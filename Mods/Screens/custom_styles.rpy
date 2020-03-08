init -2 style serum_text_style: # General text style used in the serum screens.
    text_align 0.5
    size 20
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    xalign 0.5

init -2 style serum_background_style: # General text style used in the serum screens.
    padding [5,5]
    margin [5,5]
    background "#999999"
    insensitive_background "#222222"


init -2 style serum_textbutton_style_positive: # Used for positive trait / serum slugs
    margin [2,2]
    background "#007000"
    insensitive_background "#222222"
    hover_background "#aaaaaa"

init -2 style textbutton_no_padding: # Textbutton without padding
    margin [2,2]
    background "#000080"
    insensitive_background "#222222"

init -2 style serum_textbutton_style_negative: # Used for negative trait / serum slugs
    margin [2,2]
    background "#930000"
    insensitive_background "#222222"
    hover_background "#aaaaaa"

init -2 style serum_textbutton_style_header: # Used for header / title boxes NOTE: Make this different later to easier distinguish
    padding [5,5]
    margin [5,5]
    background "#000080"
    insensitive_background "#222222"
    hover_background "#aaaaaa"

init -2 style serum_text_style_header: # Increased text size for headers
    text_align 0.5
    size 20
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    bold True
    xalign 0.5

init -2 style serum_text_style_traits: # Unaligned text style for traits in the serum_tooltip screen
    size 16
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    text_align 0.5
    xalign 0.5

init -2 style textbutton_no_padding_highlight: # Textbutton without padding
    margin [2,2]
    background "#000080"
    insensitive_background "#222222"
    hover_background "#aaaaaa"

init -2 style custom_outfit_style: ##The text style used for text inside of the outfit manager.
    size 20
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    insensitive_color "#dddddd"
    hover_color "#ffffff"
    bold False
    italic False

init 2 style textbutton_text_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    size 20
    italic False
    bold False
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    text_align 0.5

init 2 style menu_text_style:
    size 18
    italic False
    bold False
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    text_align 0.5
