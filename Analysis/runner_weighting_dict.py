# runner_weighting_dict.py
# New version creates the full weighting dict within.

# Imports
import config
from greyhound import Greyhound

# Break up the performances.
def performance_weight(runner):
    ''' Break up the recent 5? performances. '''
    performance_array = runner.break_up_performance()

    sum_run_value = 1

    for _, _, position, runners, grade, _ in performance_array:
        try:
            run_value = 2 - int(position) / int(runners) 
        except:
            run_value = 1

        if runner.grade == 'C0':
            run_value = run_value * config.rec_C0
    
        elif grade == 'C1':
            run_value = run_value * config.rec_C1

        elif grade == 'C1/2':
            run_value = run_value * config.rec_C1_2

        elif grade == 'C2':
            run_value = run_value * config.rec_C2
        
        elif grade == 'C2/3':
            run_value = run_value * config.rec_C2_3

        elif grade == 'C3':
            run_value = run_value * config.rec_C3
        
        elif grade == 'C3/4':
            run_value = run_value * config.rec_C3_4

        elif grade == 'C4':
            run_value = run_value * config.rec_C4
        
        elif grade == 'C4/5':
            run_value = run_value * config.rec_C4_5

        elif grade == 'C5':
            run_value = run_value * config.rec_C5

        else:
            run_value = run_value

        sum_run_value += (1 + run_value)

    return sum_run_value

        #print("{} {} {} {} {} {}".format(box, track, position, runners, grade, distance))

# Assign the values to the greyhound weighting in one big ugly mess.
def assign_weight_values(weighted_dict, runner):
    """ Assign the weightings * key inputs to each greyhound in the weighting dict. """
    if runner.grade == 'C0':
        grade_weight = config.C0 * config.GRADE_WEIGHTING
    
    if runner.grade == 'C1':
        grade_weight = config.C1 * config.GRADE_WEIGHTING

    if runner.grade == 'C2':
        grade_weight = config.C2 * config.GRADE_WEIGHTING

    if runner.grade == 'C3':
        grade_weight = config.C3 * config.GRADE_WEIGHTING

    if runner.grade == 'C4':
        grade_weight = config.C4 * config.GRADE_WEIGHTING

    if runner.grade == 'C5':
        grade_weight = config.C5 * config.GRADE_WEIGHTING

    weighted_dict[runner.name] = weighted_dict[runner.name] * (1 + grade_weight)

    speed_map_weight = float(runner.speed_map) * config.SPEED_MAP_WEIGHTING

    weighted_dict[runner.name] = weighted_dict[runner.name] * (1 + speed_map_weight)

    win_rate_all_stat, place_rate_all_stat = runner.ret_all_stat()
    win_rate_all_stat = win_rate_all_stat * config.OVERALL_WIN_WEIGHTING
    place_rate_all_stat = place_rate_all_stat * config.OVERALL_PLACE_WEIGHTING

    weighted_dict[runner.name] = weighted_dict[runner.name] * (1 + win_rate_all_stat) * (1 + place_rate_all_stat)

    win_rate_track_stat, place_rate_track_stat = runner.ret_track_stat()
    win_rate_track_stat = win_rate_track_stat * config.TRACK_WIN_WEIGHTING
    place_rate_track_stat = place_rate_track_stat * config.TRACK_PLACE_WEIGHTING

    weighted_dict[runner.name] = weighted_dict[runner.name] * (1 + win_rate_track_stat) * (1 + place_rate_track_stat)

    win_rate_track_and_distance_stat, place_rate_track_and_distance_stat = runner.ret_track_and_distance_stat()
    win_rate_track_and_distance_stat = win_rate_track_and_distance_stat * config.TRACK_AND_DISTANCE_WIN_WEIGHTING
    place_rate_track_and_distance_stat = place_rate_track_and_distance_stat * config.TRACK_AND_DISTANCE_PLACE_WEIGHTING

    weighted_dict[runner.name] = weighted_dict[runner.name] * (1 + win_rate_track_and_distance_stat) * (1 + place_rate_track_and_distance_stat)

    # Need key race information first.
    # sprint
    # middle
    # distnace

    # Should update with relevant box records. e.g. can it overcome the bias associated with the box its given based on prev.
    if runner.barrier == '1':
        win_rate_box_stat, place_rate_box_stat = runner.ret_box_1_stat()
        win_rate_box_stat = win_rate_box_stat * config.BOX_WIN_WEIGHTING
        place_rate_box_stat = place_rate_box_stat * config.BOX_PLACE_WEIGHTING

    elif runner.barrier == '2':
        win_rate_box_stat, place_rate_box_stat = runner.ret_box_2_stat()
        win_rate_box_stat = win_rate_box_stat * config.BOX_WIN_WEIGHTING
        place_rate_box_stat = place_rate_box_stat * config.BOX_PLACE_WEIGHTING

    elif runner.barrier == '3':
        win_rate_box_stat, place_rate_box_stat = runner.ret_box_3_stat()
        win_rate_box_stat = win_rate_box_stat * config.BOX_WIN_WEIGHTING
        place_rate_box_stat = place_rate_box_stat * config.BOX_PLACE_WEIGHTING

    elif runner.barrier == '4':
        win_rate_box_stat, place_rate_box_stat = runner.ret_box_4_stat()
        win_rate_box_stat = win_rate_box_stat * config.BOX_WIN_WEIGHTING
        place_rate_box_stat = place_rate_box_stat * config.BOX_PLACE_WEIGHTING

    elif runner.barrier == '5':
        win_rate_box_stat, place_rate_box_stat = runner.ret_box_5_stat()
        win_rate_box_stat = win_rate_box_stat * config.BOX_WIN_WEIGHTING
        place_rate_box_stat = place_rate_box_stat * config.BOX_PLACE_WEIGHTING

    elif runner.barrier == '6':
        win_rate_box_stat, place_rate_box_stat = runner.ret_box_6_stat()
        win_rate_box_stat = win_rate_box_stat * config.BOX_WIN_WEIGHTING
        place_rate_box_stat = place_rate_box_stat * config.BOX_PLACE_WEIGHTING

    elif runner.barrier == '7':
        win_rate_box_stat, place_rate_box_stat = runner.ret_box_7_stat()
        win_rate_box_stat = win_rate_box_stat * config.BOX_WIN_WEIGHTING
        place_rate_box_stat = place_rate_box_stat * config.BOX_PLACE_WEIGHTING

    elif runner.barrier == '8':
        win_rate_box_stat, place_rate_box_stat = runner.ret_box_8_stat()
        win_rate_box_stat = win_rate_box_stat * config.BOX_WIN_WEIGHTING
        place_rate_box_stat = place_rate_box_stat * config.BOX_PLACE_WEIGHTING

    weighted_dict[runner.name] = weighted_dict[runner.name] * (1 + win_rate_box_stat) * (1 + place_rate_box_stat)

    sum_run_grades = performance_weight(runner)

    weighted_dict[runner.name] = weighted_dict[runner.name] * sum_run_grades

    return weighted_dict

# Initialise the auto weighting, send to other functions to get all.
def auto(runners_list, num_runners):
    """ Give all runners an equal chance in a new dictionary with name as key and weighting as value. """
    weighted_dict = dict()
    runners_chance = 1/len(num_runners)
    for runner in runners_list:
        if runner.number in num_runners:
            weighted_dict[runner.name] = runners_chance
            weighted_dict = assign_weight_values(weighted_dict, runner)
    '''    
    for key, value in weighted_dict.items():
        print("{}{}".format(key,value))'''

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