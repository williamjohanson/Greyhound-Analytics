# race_file.py
# Return an array of lines for the file.

# Imports
import datetime

# Read all the lines. Use find later to get the info.
def get_race_file_auto(race_num, meeting):
    """ Get the data from the html race file and place into greyhound class. """
    current = datetime.datetime.today()
    year = current.year
    month = current.month
    if month < 10: 
        month = '0' + str(month)
    day = current.day
    if day < 10: 
        day = '0' + str(day)
    date = ("{}-{}-{}".format(year, month, day))

    open_race_file = open('Race Data/M' + str(int(meeting)) + '_' + str(date) + '/Raceb' + race_num, 'r')
    race_file = open_race_file.read()
    
    return race_file

# ----------------------------------------------------------------------------------------------- #
# Original method of appending text to lines.
def get_race_file_original(race_num):
    """Find the race file which is  a copy into a text file from the extended form."""
    #name_file = input("What is the number of the race? ")
    open_race_file = open('Race Data/race' + race_num, 'r')
    race_file_lines = []
    line = open_race_file.readline()
    while line != "Back to top":
        line = open_race_file.readline()
        race_file_lines.append(line.strip())
    
    return race_file_lines
# To update to GUI just open a function argument which is the race file from dropdown on GUI