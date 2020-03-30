# runner_weighting_dict.py
# Simply give each runner a proportional chance based on the number of runners.

def init(runner_dict, num_runners):
    """ Give all runners an equal chance in a new dictionary with name as key and weighting as value. """
    weighted_dict = dict()
    runners_chance = 1/num_runners
    for key in runner_dict.keys():
        weighted_dict[key] = runners_chance
        
    return weighted_dict