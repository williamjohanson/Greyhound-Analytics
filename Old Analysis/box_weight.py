# box_weight.py
# Change runner chance based on box win/place stats.
# IMPROVEMENT: Inside outside boxes??? Shorten the bugger down with the 4 loops my dudeski.

# Imports.
import config 

# Iterate through the dogs, find their box and their history from the box.
def box_stat(race_file, weighted_dict, runner_dict):
    """Modify the dogs weighting by its results from its box."""
    for key, value in weighted_dict.items():
        for i in range(0, len(race_file)):
            if (key == race_file[i]):
                if runner_dict[key] == 1:
                    line = race_file[i + 28].split(":")
                    try:
                        win_box = int(line[1]) / int(line[0])
                    except ZeroDivisionError:
                        win_box = 0
                    try:
                        place_box = (int(line[1]) + int(line[2])) / int(line[0])
                    except ZeroDivisionError:
                        place_box = 0
                    value = value * (1 + config.BOX_WIN_WEIGHTING * win_box + config.BOX_PLACE_WEIGHTING * place_box)
                    weighted_dict[key] = value    

                if runner_dict[key] == 2:
                    line = race_file[i + 30].split(":")
                    try:
                        win_box = int(line[1]) / int(line[0])
                    except ZeroDivisionError:
                        win_box = 0
                    try:
                        place_box = (int(line[1]) + int(line[2])) / int(line[0])
                    except ZeroDivisionError:
                        place_box = 0
                    value = value * (1 + config.BOX_WIN_WEIGHTING * win_box + config.BOX_PLACE_WEIGHTING * place_box)
                    weighted_dict[key] = value      

                if runner_dict[key] == 3:
                    line = race_file[i + 32].split(":")
                    try:
                        win_box = int(line[1]) / int(line[0])
                    except ZeroDivisionError:
                        win_box = 0
                    try:
                        place_box = (int(line[1]) + int(line[2])) / int(line[0])
                    except ZeroDivisionError:
                        place_box = 0
                    value = value * (1 + config.BOX_WIN_WEIGHTING * win_box + config.BOX_PLACE_WEIGHTING * place_box)
                    weighted_dict[key] = value    

                if runner_dict[key] == 4:
                    line = race_file[i + 34].split(":")
                    try:
                        win_box = int(line[1]) / int(line[0])
                    except ZeroDivisionError:
                        win_box = 0
                    try:
                        place_box = (int(line[1]) + int(line[2])) / int(line[0])
                    except ZeroDivisionError:
                        place_box = 0
                    value = value * (1 + config.BOX_WIN_WEIGHTING * win_box + config.BOX_PLACE_WEIGHTING * place_box)
                    weighted_dict[key] = value                             

                if runner_dict[key] == 5:
                    line = race_file[i + 36].split(":")
                    try:
                        win_box = int(line[1]) / int(line[0])
                    except ZeroDivisionError:
                        win_box = 0
                    try:
                        place_box = (int(line[1]) + int(line[2])) / int(line[0])
                    except ZeroDivisionError:
                        place_box = 0
                    value = value * (1 + config.BOX_WIN_WEIGHTING * win_box + config.BOX_PLACE_WEIGHTING * place_box)
                    weighted_dict[key] = value   

                if runner_dict[key] == 6:
                    line = race_file[i + 38].split(":")
                    try:
                        win_box = int(line[1]) / int(line[0])
                    except ZeroDivisionError:
                        win_box = 0
                    try:
                        place_box = (int(line[1]) + int(line[2])) / int(line[0])
                    except ZeroDivisionError:
                        place_box = 0
                    value = value * (1 + config.BOX_WIN_WEIGHTING * win_box + config.BOX_PLACE_WEIGHTING * place_box)
                    weighted_dict[key] = value     

                if runner_dict[key] == 7:
                    line = race_file[i + 40].split(":")
                    try:
                        win_box = int(line[1]) / int(line[0])
                    except ZeroDivisionError:
                        win_box = 0
                    try:
                        place_box = (int(line[1]) + int(line[2])) / int(line[0])
                    except ZeroDivisionError:
                        place_box = 0
                    value = value * (1 + config.BOX_WIN_WEIGHTING * win_box + config.BOX_PLACE_WEIGHTING * place_box)
                    weighted_dict[key] = value    

                if runner_dict[key] == 8:
                    line = race_file[i + 42].split(":")
                    try:
                        win_box = int(line[1]) / int(line[0])
                    except ZeroDivisionError:
                        win_box = 0
                    try:
                        place_box = (int(line[1]) + int(line[2])) / int(line[0])
                    except ZeroDivisionError:
                        place_box = 0
                    value = value * (1 + config.BOX_WIN_WEIGHTING * win_box + config.BOX_PLACE_WEIGHTING * place_box)
                    weighted_dict[key] = value                                         
                              
    return weighted_dict