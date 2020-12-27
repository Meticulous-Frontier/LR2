# Under construction UI, visual indication that current content is Work In Progress
# make visible by:  show screen under_construction_ui
# hide using:       hide screen under_construction_ui
#
# Make visible at start of label that denotes content not completed.

screen under_construction_ui():
    zorder 60
    frame:
        background under_construction_image
        pos (450, 830)
