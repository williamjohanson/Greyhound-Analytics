import csv

def print_to_csv(value2, val, key):
    """Print the results to a csv file for tracking. """
    open_file = open("picks_analysis.csv", mode='a', newline='')
    writer = csv.writer(open_file, delimiter=',', quotechar='"')
    writer.writerow([key, value2, val])
    open_file.close()

def print_grades(runner_dict, weighted_dict):     
    """Print the formatted grades."""
    value_array = []
    sum = 0
    i = 0
    for key, value in weighted_dict.items():
        value_array.append(value)
        sum += value
    value_array.sort(reverse=True)
    for val in value_array: 
        for key, value in weighted_dict.items():
            for key2, value2 in runner_dict.items():
                if weighted_dict[key] == val:
                    if key == key2:
                        val = 1/(val / sum)
                        print_to_csv(value2, val, key)
                        print("{} : ${:.2f} {}\n".format(value2, val, key))
                        i += 1  