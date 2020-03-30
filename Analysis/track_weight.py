import config

def track_bias(weighted_dict, race_file):
    """Take the tracks form into consideration"""
    for key, value in weighted_dict.items():
        for i in range(0, len(race_file)):
            if (key == race_file[i]):
                track_list = race_file[i + 18].split(":")
                try:
                    weighted_dict[key] = value * (1 + config.TRACK_WIN_WEIGHTING * int(track_list[1]) / int(track_list[0]))
                except ZeroDivisionError:
                    weighted_dict[key] = value
                try:
                    weighted_dict[key] = value * (1 + config.TRACK_PLACE_WEIGHTING * int(track_list[2]) / int(track_list[0]))
                except ZeroDivisionError:
                    weighted_dict[key] = value
                    
    return weighted_dict  