# print_runners.py

def runners_print(runner_dict):
    """ Print the runners discovered. """
    print("The runners are: \n ")
    for key, value in runner_dict.items():        
        print("- {} in box {}\n".format(key, value))