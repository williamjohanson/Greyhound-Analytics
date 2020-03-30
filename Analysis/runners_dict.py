# runners_dict.py
# Build and sort the runners dict from the race file.

# Determine which dogs are scratched.
def determine_runners(runner_dict, race_file):
    """ Find which members of the dictionary are actually running/scratched. """
    # Find the dogs scratched and add to list for deleting.
    del_list = []
    i = 0
    for key, __ in runner_dict.items():
        i += 1
        for j in range(1, len(race_file)):
            if key == race_file[j].strip():
                if race_file[j + 2].strip() == "SCRATCHED":
                    del_list.append(key)
                    i -= 1
                    break
    
    # Delete scratched dogs from dict.
    for del_item in del_list:
        del runner_dict[del_item]

    # Reassign i to something useful.
    num_runners = i
    
    return runner_dict, num_runners

# Function to replace box numbers if 9 or 10 is a runner!
def replace_scratched(runner_dict):
    """ Place dogs in 9, 10 into a box in the field. """
    # This is an assumption on relocation.
    box_list = []
    spare_list = []
    for key, value in runner_dict.items():
        if int(value) < 9:
            box_list.append(value)
        else:
            spare_list.append(key)

    # Have assumed 10 goes into the earlier box if multiple spares.
    if len(spare_list) == 2:
        j = 0
        for i in range(1, len(box_list) + 1):
            if (i not in box_list) and (j == 0):
                runner_dict[spare_list[-1]] = i
                j += 1
            elif (i not in box_list) and (j == 1):
                runner_dict[spare_list[0]] = i

    # Have assumed spare goes into earliest box -- not sure if multiple scratches more than replacements.
    elif len(spare_list) == 1:
        for i in range(1, len(box_list) + 1):
            if (i not in box_list):
                runner_dict[spare_list[0]] = i
                
    # Do nothing.
    else:
        j = 69 # Noice

    return runner_dict
            
# Build the runners dict by finding all the potential runners in the race file.
def build_runners_dict(race_file):
    """ Build the dictionary containing the dogs name and its box number"""
    # Find where in the race file there is a box number and find the dog name associated, save both to dict.
    runner_dict = dict()
    i = 1
    for j in range(1, len(race_file)):
        try:
            if int(race_file[j].strip()) == i:
                runner_dict[race_file[j + 3].strip('\n')] = i
                i += 1 
        except ValueError:
            i += 0

    # Send to deleting function.
    runner_dict, num_runners = determine_runners(runner_dict, race_file)

    # Replace scratched dogs into boxes.
    runner_dict = replace_scratched(runner_dict)

    return runner_dict, num_runners