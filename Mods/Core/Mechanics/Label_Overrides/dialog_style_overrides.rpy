# override for default positioning in say dialog
# this should make names fit better in the namebox
# this should make text fit better in the say dialog box

init 100:
    python:
        gui.name_ypos = 0
        gui.name_xpos = 0.25
        gui.text_xpos = 0.25
        gui.text_ypos = 100


    style namebox:
        xpos gui.name_xpos
        xanchor gui.name_xalign
        xsize gui.namebox_width
        ypos gui.name_ypos - 10
        ysize gui.namebox_height

        background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
        padding gui.namebox_borders.padding

    style say_dialogue:
        xpos gui.text_xpos
        xanchor gui.text_xalign
        xsize gui.text_width + 80
        ypos gui.text_ypos - 10
        first_indent 20
        outlines [(2,"#222222",0,0)]

        text_align gui.text_xalign
        layout ("subtitle" if gui.text_xalign else "tex")
