# Read the result and determine the final positions of the runners in each race.
def read_result_file():
    """Read the text file into an array of lines. """
    name_file = input("What is the file name: ")
    open_race_file = open("Result Data/" + name_file, 'r')
    race_file_lines = []
    line = open_race_file.readline()
    while line != " Back to top":
        line = open_race_file.readline()
        race_file_lines.append(line.strip())
    
    return race_file_lines

def 


# Compare to the output of expected results from my code which is printed to CSV - This file probably needs to be refereshed every time.

# TBT - How to update the global_bias_configurable values to be represented by what happened in the race. 

# -- Is it a maths equation of all 30 inputs? Find the 30 inputs for each dog and need to be 


def main():
    """Main Function. """
    while(1):
        race_file_lines = read_result_file()
        #print(race_file_lines)
        


main()