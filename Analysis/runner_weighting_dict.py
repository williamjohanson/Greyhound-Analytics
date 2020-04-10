# runner_weighting_dict.py
# New version creates the full weighting dict within.

# Imports
import config
from greyhound import Greyhound

# Initialise the auto weighting, send to other functions to get all.
def auto(runners_list, num_runners):
    """ Give all runners an equal chance in a new dictionary with name as key and weighting as value. """
    weighted_dict = dict()
    runners_chance = 1/len(num_runners)
    for runner in runners_list:
        weighted_dict[runner] = runners_chance
    
    # Go to another function.
    
    return weighted_dict

# ----------------------------------------------------------------------------------------------- #

# Old version. Simply give each runner a proportional chance based on the number of runners.
def init(runner_dict, num_runners):
    """ Give all runners an equal chance in a new dictionary with name as key and weighting as value. """
    weighted_dict = dict()
    runners_chance = 1/num_runners
    for key in runner_dict.keys():
        weighted_dict[key] = runners_chance
        
    return weighted_dict