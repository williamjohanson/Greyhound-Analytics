# grade_weight.py
# Give the dog a bias based on its rating band on NZG grading system.

# Imports
import config

# Following function could be rearranged to a for loop if wanting to shrink code down.
def grade_bias(race_file, weighted_dict):
    """Manipulate the weighted dict by a proportional grade rating"""
    for key, value in weighted_dict.items():
        for i in range(0, len(race_file)):
            if (key == race_file[i]):
                grade = race_file[i + 1].split(" ")[0]
                if grade == "C0":
                    value = value * (1 + config.GRADE_WEIGHTING * config.C0)
                    weighted_dict[key] = value
                elif grade == "C1":
                    value = value * (1 + config.GRADE_WEIGHTING * config.C1)
                    weighted_dict[key] = value
                elif grade == "C2":
                    value = value * (1 + config.GRADE_WEIGHTING * config.C2) 
                    weighted_dict[key] = value
                elif grade == "C3":
                    value = value * (1 + config.GRADE_WEIGHTING * config.C3)
                    weighted_dict[key] = value
                elif grade == "C4":
                    value = value * (1 + config.GRADE_WEIGHTING * config.C4)
                    weighted_dict[key] = value
                elif grade == "C5":
                    value = value * (1 + config.GRADE_WEIGHTING * config.C5)  
                    weighted_dict[key] = value
                else:                                                                               
                    weighted_dict[key] = value
                
    return weighted_dict