# print_runners.py

# Imports
from greyhound import Greyhound
import math

# Return a string using class attributes and calculate relative weighting to print to results.
def runners_print_class(runners_list, weighting_dict):
    """ Print the runners discovered. """
    value_sum = 0
    for key, value in weighting_dict.items():
        value_sum += value

    result_str = ''
    for key, value in weighting_dict.items():
        try:
            run_price = 1 / (value / value_sum)
        except:
            run_price = math.nan

        for runner in runners_list:   
            if runner.name == key:
                if runner.barrier != 0:
                    add_str = '{}: {}, in box {}. Rated price: ${:.2f}. Fastest: {}. Win Record: {}. Prize: {}. Trainer: {}, {}. Owners: {}.\n{} \n'.format(runner.name, 
                    runner.number, runner.barrier, run_price, runner.fastest, runner.sort_win_record(), runner.prize, runner.trainer, runner.trainer_district, runner.owners, runner.comment)
                else:
                    add_str = '{}: {}, is scratched.\n'.format(runner.name, 
                    runner.number)

                result_str += add_str

    return result_str

# Old print to terminal method.
def runners_print(runners_list):
    """ Print the runners discovered. """
    print("The runners are: \n ")
    for runner in runners_list:        
        print("- {}in box {}.\n".format(runner.name, runner.number))