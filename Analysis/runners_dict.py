# runners_dict.py
# Build and sort the runners dict from the race file.

# Imports.
from greyhound import Greyhound 

# Globals
runners_list = []  

# Find the dogs which have been scratched. Only really works if less than two scratchings.
def find_scratched(runners_list):
    """ Place dogs in 9, 10 into a box in the field. """
    # This is an assumption on relocation.
    scratched_list = []
    spare_list = []
    num_runners = []
    barrier = 1
    for dog in runners_list:
        if int(dog.number) < 9 and dog.scratched == 'true':
            scratched_list.append(dog.barrier) 
            dog.barrier = 0
            # Dont need to reassign barrier as it is assumed correct.
        elif int(dog.number) > 8 and dog.scratched == 'false':
            spare_list.append(dog)
        # All dogs which are scratched need barrier removed.
        elif int(dog.number) > 8 and dog.scratched == 'true':
            dog.barrier = 0
        
        barrier += 1

    if len(spare_list) == 2:
        runners_list[-1].barrier = scratched_list[0]
        runners_list[-2].barrier = scratched_list[1]
    
    elif len(spare_list) == 1:
        if runners_list[-1].scratched == 'false':
            runners_list[-1].barrier = scratched_list[0]
        elif runners_list[-2].scratched == 'false':
            runners_list[-2].barrier = scratched_list[0]

    for runners in runners_list:
        if runners.scratched == 'false':
            num_runners.append(runners.number)

    return runners_list, num_runners


# Assign the data from the HTML to text and assign it to greyhound variables.
def assign_data(data_set):
    """ Find the specific data and assign to each greyhound variable. """
    global runners_list

    age_index_start = data_set.find("age")
    age_index_end = data_set.find(',"barrier"')
    age = data_set[age_index_start + 5: age_index_end]

    breeding = ''
    breeding_index_start = data_set.find('"breeding":')
    breeding_index_end = data_set.find(',"breeding_extra":')
    breeding_list = data_set[breeding_index_start + 12: breeding_index_end -1].split('\n')
    for line in breeding_list:
        breeding = breeding + line + ' '

    grade_index_start = data_set.find('"class":')
    grade_index_end = data_set.find(',"colour":')
    grade = data_set[grade_index_start + 9: grade_index_end -1]

    comment = ''
    comment_index_start = data_set.find('"comment":')
    comment_index_end = data_set.find(',"fastest"')
    comment_list = data_set[comment_index_start + 11: comment_index_end -1].split('\n')
    for line in comment_list:
        comment = comment + line + ' '

    fastest_index_start = data_set.find(',"fastest":')
    fastest_index_end = data_set.find(',"form"')
    fastest = data_set[fastest_index_start + 12: fastest_index_end -1]

    owners = ''
    owners_index_start = data_set.find('"owners":')
    owners_index_end = data_set.find(',"performance"')
    owners_list = data_set[owners_index_start + 10: owners_index_end -1].split('\n')
    for line in owners_list:
        owners = owners + line + ' '

    performance = ''
    performance_index_start = data_set.find('"performance":')
    performance_index_end = data_set.find(',"runner"')
    performance_list = data_set[performance_index_start + 14: performance_index_end -1].split('\n')
    for line in performance_list:
        performance = performance + line + ' '
    # Send to another function for splitting up the performances

    name = ''
    name_index_start = data_set.find('"runner":')
    name_index_end = data_set.find(',"scratched"')
    name_list = data_set[name_index_start + 10: name_index_end -1].split('\n')
    for line in name_list:
        name = name + line + ' '

    scratched_index_start = data_set.find('"scratched":')
    scratched_index_end = data_set.find(',"sex"')
    scratched = data_set[scratched_index_start + 12: scratched_index_end]
    # True/false

    number_index_start = data_set.find('"silk_text":')
    number_index_end = data_set.find(',"silk_url"')
    number = data_set[number_index_start + 13: number_index_end -1]
    # Looks like number and barrier is gonna be tricky dicky.

    all_stat_index_start = data_set.find('"type":"All","value":')
    all_stat_index_end = data_set.find('},{"type":"Track","value":')
    all_stat = data_set[all_stat_index_start + 22: all_stat_index_end -1]

    track_stat_index_start = data_set.find('"type":"Track","value":')
    track_stat_index_end = data_set.find('},{"type":"Track\n&')
    track_stat = data_set[track_stat_index_start + 24: track_stat_index_end -1]

    track_and_distance_stat_index_start = data_set.find('&\nDistance","value":')
    track_and_distance_stat_index_end = data_set.find('},{"type":"Sprint","value"')
    track_and_distance_stat = data_set[track_and_distance_stat_index_start + 21: track_and_distance_stat_index_end -1]

    sprint_stat_index_start = data_set.find('"type":"Sprint","value":')
    sprint_stat_index_end = data_set.find('},{"type":"Middle","value"')
    sprint_stat = data_set[sprint_stat_index_start + 25: sprint_stat_index_end -1]

    middle_stat_index_start = data_set.find('"type":"Middle","value":')
    middle_stat_index_end = data_set.find('},{"type":"Distance","value"')
    middle_stat = data_set[middle_stat_index_start + 25: middle_stat_index_end -1]

    distance_stat_index_start = data_set.find('"type":"Distance","value":')
    distance_stat_index_end = data_set.find('},{"type":"Box')
    distance_stat = data_set[distance_stat_index_start + 27: distance_stat_index_end -1]

    box_1_stat_index_start = data_set.find('1","value":')
    box_1_stat_index_end = data_set.find('},{"type":"Box 2","value":')
    box_1_stat = data_set[box_1_stat_index_start + 12: box_1_stat_index_end -1]

    box_2_stat_index_start = data_set.find('"type":"Box 2","value":')
    box_2_stat_index_end = data_set.find('},{"type":"Box\n3"')
    box_2_stat = data_set[box_2_stat_index_start + 24: box_2_stat_index_end -1]

    box_3_stat_index_start = data_set.find('3","value":')
    box_3_stat_index_end = data_set.find('},{"type":"Box 4","value":')
    box_3_stat = data_set[box_3_stat_index_start + 12: box_3_stat_index_end -1]

    box_4_stat_index_start = data_set.find('"type":"Box 4","value":')
    box_4_stat_index_end = data_set.find('},{"type":"Box\n5"')
    box_4_stat = data_set[box_4_stat_index_start + 24: box_4_stat_index_end -1]

    box_5_stat_index_start = data_set.find('5","value":')
    box_5_stat_index_end = data_set.find('},{"type":"Box 6","value":')
    box_5_stat = data_set[box_5_stat_index_start + 12: box_5_stat_index_end -1]

    box_6_stat_index_start = data_set.find('"type":"Box 6","value":')
    box_6_stat_index_end = data_set.find('},{"type":"Box\n7"')
    box_6_stat = data_set[box_6_stat_index_start + 24: box_6_stat_index_end -1]

    box_7_stat_index_start = data_set.find('7","value":')
    box_7_stat_index_end = data_set.find('},{"type":"Box\n8"')
    box_7_stat = data_set[box_7_stat_index_start + 12: box_7_stat_index_end -1]

    box_8_stat_index_start = data_set.find('8","value":')
    box_8_stat_index_end = data_set.find('}],"plc_div"')
    box_8_stat = data_set[box_8_stat_index_start + 12: box_8_stat_index_end -1]

    prize_index_start = data_set.find('"prize":')
    prize_index_end = data_set.find(',"prize2"')
    prize = data_set[prize_index_start + 9: prize_index_end -1]

    trainer = ''
    trainer_index_start = data_set.find('"trainer":')
    trainer_index_end = data_set.find(',"trainer_district"')
    trainer_list = data_set[trainer_index_start + 11: trainer_index_end -1].split('\n')
    for line in trainer_list:
        trainer = trainer + line + ' '

    trainer_district = ''
    trainer_district_index_start = data_set.find('"trainer_district":')
    trainer_district_index_end = data_set.find(',"weight":0,')
    trainer_district_list = data_set[trainer_district_index_start + 20: trainer_district_index_end -1].split('\n')
    for line in trainer_district_list:
        trainer_district = trainer_district + line + ' '

    win_record = ''
    win_record_index_start = data_set.find('"win_record":')
    win_record_index_end = data_set.find(',"sire"')
    win_record_list = data_set[win_record_index_start + 16: win_record_index_end -3].split('\n')
    for line in win_record_list:
        win_record = win_record + line + ' '

    barrier = number # Just for now to solve

    # Send to the global runners list. Defined by position? All info is included within the object.
    runners_list.append(Greyhound(name, age, breeding, grade, comment, fastest, owners, performance, 
    scratched, number, all_stat, track_stat, track_and_distance_stat, sprint_stat, middle_stat, 
    distance_stat, box_1_stat, box_2_stat, box_3_stat, box_4_stat, box_5_stat, box_6_stat, box_7_stat, box_8_stat, 
    prize, trainer, trainer_district, win_record, barrier))

# Create the dogs using the greyhound class for all the dogs with each of their attributes. Will require breaking up a lot of the HTML text which will be very consuming.
def create_greyhounds_running(race_file):
    """ Build a list of greyhound types that are running in the race. """
    global runners_list
    i = race_file.find('"entries":')
    j = race_file.find('"form_title":')

    nominated_string = race_file[i:j]
    nominated_list = nominated_string.split('"jockey":null,"runner":')
    nominated_list = nominated_list[1:]

    for nom in nominated_list:
        assign_data(nom)

    runners_list = find_scratched(runners_list)

    return runners_list

# ----------------------------------------------------------------------------------------------- #
# le old version of doing things.

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