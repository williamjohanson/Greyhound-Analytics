# config.py
# Configure the global weighting values from the csv variable file.

# Imports
import csv

# Read the csv file.
def get_values_csv():
    """ Read the 'global_bias_configurable' file and read the values to a list."""
    value_list = []
    i = 0
    csvfile = open('global_bias_configurable.csv')
    value_list.append(csvfile.readline().strip('\n'))

    while i < 31:
        value_list.append(csvfile.readline().strip('\n'))
        i += 1

    return value_list

# Set the returned values as global values.
def init():
    """ Weighting Variables. """
    # Set as globals.
    global GRADE_WEIGHTING 
    global OVERALL_WIN_WEIGHTING
    global OVERALL_PLACE_WEIGHTING
    global BOX_WIN_WEIGHTING
    global BOX_PLACE_WEIGHTING
    global RECENT_WEIGHTING
    global TRACK_WIN_WEIGHTING
    global TRACK_PLACE_WEIGHTING
    global C0
    global C1
    global C2
    global C3
    global C4
    global C5
    global first
    global second
    global third
    global fourth
    global fifth
    global sixth
    global seventh
    global eighth
    global rec_C0
    global rec_C1
    global rec_C1_2
    global rec_C2
    global rec_C2_3
    global rec_C3
    global rec_C3_4
    global rec_C4
    global rec_C4_5
    global rec_C5

    # Read function for weightings.
    weightings = get_values_csv()
    
    # Assign weightings.
    GRADE_WEIGHTING = float(weightings[0])
    OVERALL_WIN_WEIGHTING = float(weightings[1])
    OVERALL_PLACE_WEIGHTING = float(weightings[2])
    BOX_WIN_WEIGHTING = float(weightings[3])
    BOX_PLACE_WEIGHTING = float(weightings[4])
    RECENT_WEIGHTING = float(weightings[5])
    TRACK_WIN_WEIGHTING = float(weightings[6])
    TRACK_PLACE_WEIGHTING = float(weightings[7])
    C0 = float(weightings[8])
    C1 = float(weightings[9])
    C2 = float(weightings[10])
    C3 = float(weightings[11])
    C4 = float(weightings[12])
    C5 = float(weightings[13])
    first = float(weightings[14])
    second = float(weightings[15])
    third = float(weightings[16])
    fourth = float(weightings[17])
    fifth = float(weightings[18])
    sixth = float(weightings[19])
    seventh = float(weightings[20])
    eighth = float(weightings[21])
    rec_C0 = float(weightings[22])
    rec_C1 = float(weightings[23])
    rec_C1_2 = float(weightings[24])
    rec_C2 = float(weightings[25])
    rec_C2_3 = float(weightings[26])
    rec_C3 = float(weightings[27])
    rec_C3_4 = float(weightings[28])
    rec_C4 = float(weightings[29])
    rec_C4_5 = float(weightings[30])
    rec_C5 = float(weightings[31])

