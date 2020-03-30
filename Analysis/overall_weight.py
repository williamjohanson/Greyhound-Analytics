import config

def overall_stat(race_file, weighted_dict):
    """ Take the dogs overall win/loss stats and add that to the winning weighting"""
    for key, value in weighted_dict.items():
        for i in range(0, len(race_file)):
            if (key == race_file[i]):
                line = race_file[i + 12].split(":")
                win_rate = int(line[1]) / int(line[0])
                place_rate = (int(line[1]) + int(line[2]) + int(line[3])) / int(line[0])
                value = value * (1 + config.OVERALL_WIN_WEIGHTING * win_rate + config.OVERALL_PLACE_WEIGHTING * place_rate)
                weighted_dict[key] = value    
                
    return weighted_dict