# race_file.py
# Return an array of lines for the file.

def get_race_file():
    """Find the race file which is  a copy into a text file from the extended form."""
    name_file = input("What is the number of the race? ")
    open_race_file = open("Race Data/race" + name_file + ".txt", 'r')
    race_file_lines = []
    line = open_race_file.readline()
    while line != "Back to top":
        line = open_race_file.readline()
        race_file_lines.append(line.strip())
    
    return race_file_lines
# To update to GUI just open a function argument which is the race file from dropdown on GUI