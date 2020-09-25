init -10 python:
    config.search_prefixes = [ "", "images/", "Mods/Core/Images/" ]

init 2 python:
    secret_mask = Facial_Accessory("Secret Mask", 2, False, False, "Secret_Mask", False, False, 0, display_name = "masks", opacity_adjustment = .5)
    earings_list.append(secret_mask)
    
    master_clothing_offset_dict["Secret_Mask"] = {"cowgirl":(266,221), "missionary":(338,93), "kissing":(282,62), "sitting":(387,192), "against_wall":(202,64), "back_peek":(169,103), "blowjob":(227,282), "stand4":(231,111), "stand5":(249,91), "standing_doggy":(146,144), "kneeling1":(248,219), "walking_away":(190,103), "doggy":(319,454), "stand2":(172,115), "stand3":(205,77)}