# print_runners.py

# Imports
from greyhound import Greyhound

# Return a string using class attributes to print to results.
def runners_print_class(runners_list):
    """ Print the runners discovered. """
    result_str = ''
    for runner in runners_list:      
        if runner.barrier != 0:
            add_str = '{}: {}, in box {}. Fastest: {}. Win Record: {}. Prize: {}. Trainer: {}, {}. Owners: {}.\n{} \n'.format(runner.name, 
            runner.number, runner.barrier, runner.fastest, runner.sort_win_record(), runner.prize, runner.trainer, runner.trainer_district, runner.owners, runner.comment)
        else:
            add_str = '{}: {}, is scratched.\n'.format(runner.name, 
            runner.number)

        result_str += add_str

    return result_str
# ----------------------------------------------------------------------------------------------- #

# Old print to terminal method.
def runners_print(runners_list):
    """ Print the runners discovered. """
    print("The runners are: \n ")
    for runner in runners_list:        
        print("- {}in box {}.\n".format(runner.name, runner.number))