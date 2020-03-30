# recent_weight.py
# Just le beautiful programmme.

# Imports.
import config

def recent_stat(race_file, weighted_dict, runner_dict):
    """From the previous 5 runs, take the position multiplied by the grade to find its recent form.""" 
    j = 1
    for key, value in weighted_dict.items():
        for i in range(0, len(race_file)):
            if (key == race_file[i]):
                if runner_dict[key] == j:
                    for k in range(45, 50):
                        try:
                            stat = race_file[i + k].split(" ")
                            position = stat[4]
                            position = position[0]
                            grade_spot = stat[6]
                            grade = grade_spot[3:]
                            if grade[-1] == "m" or grade[-1] == "f" or grade[-1] == "d" or grade[-1] == "q":
                                grade = grade[:-1]
                            if grade == "0":
                                if position[0] == "1":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C0 * config.first)
                                    weighted_dict[key] = value
                                if position[0] == "2":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C0 * config.second)   
                                    weighted_dict[key] = value
                                if position[0] == "3":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C0 * config.third)
                                    weighted_dict[key] = value
                                if position[0] == "4":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C0 * config.fourth) 
                                    weighted_dict[key] = value     
                                if position[0] == "5":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C0 * config.fifth)
                                    weighted_dict[key] = value
                                if position[0] == "6":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C0 * config.sixth)  
                                    weighted_dict[key] = value
                                if position[0] == "7":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C0 * config.seventh)
                                    weighted_dict[key] = value
                                if position[0] == "8":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C0 * config.eighth) 
                                    weighted_dict[key] = value
                            elif grade == "1":
                                if position[0] == "1":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1 * config.first)
                                    weighted_dict[key] = value
                                if position[0] == "2":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1 * config.second)   
                                    weighted_dict[key] = value
                                if position[0] == "3":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1 * config.third)
                                    weighted_dict[key] = value
                                if position[0] == "4":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1 * config.fourth)      
                                    weighted_dict[key] = value
                                if position[0] == "5":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1 * config.fifth)
                                    weighted_dict[key] = value
                                if position[0] == "6":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1 * config.sixth)  
                                    weighted_dict[key] = value
                                if position[0] == "7":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1 * config.seventh)
                                    weighted_dict[key] = value
                                if position[0] == "8":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1 * config.eighth)   
                                    weighted_dict[key] = value   
                            elif grade == "1/2":
                                if position[0] == "1":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1_2 * config.first)
                                    weighted_dict[key] = value
                                if position[0] == "2":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1_2 * config.second)   
                                    weighted_dict[key] = value
                                if position[0] == "3":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1_2 * config.third)
                                    weighted_dict[key] = value
                                if position[0] == "4":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1_2 * config.fourth)   
                                    weighted_dict[key] = value   
                                if position[0] == "5":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1_2 * config.fifth)
                                    weighted_dict[key] = value
                                if position[0] == "6":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1_2 * config.sixth)  
                                    weighted_dict[key] = value
                                if position[0] == "7":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1_2 * config.seventh)
                                    weighted_dict[key] = value
                                if position[0] == "8":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C1_2 * config.eighth)      
                                    weighted_dict[key] = value                    
                            elif grade == "2":
                                if position[0] == "1":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2 * config.first)
                                    weighted_dict[key] = value
                                if position[0] == "2":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2 * config.second)  
                                    weighted_dict[key] = value 
                                if position[0] == "3":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2 * config.third)
                                    weighted_dict[key] = value
                                if position[0] == "4":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2 * config.fourth)    
                                    weighted_dict[key] = value  
                                if position[0] == "5":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2 * config.fifth)
                                    weighted_dict[key] = value
                                if position[0] == "6":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2 * config.sixth)  
                                    weighted_dict[key] = value
                                if position[0] == "7":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2 * config.seventh)
                                    weighted_dict[key] = value
                                if position[0] == "8":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2 * config.eighth)   
                                    weighted_dict[key] = value   
                            elif grade == "2_3":
                                if position[0] == "1":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2_3 * config.first)
                                    weighted_dict[key] = value
                                if position[0] == "2":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2_3 * config.second)  
                                    weighted_dict[key] = value 
                                if position[0] == "3":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2_3 * config.third)
                                    weighted_dict[key] = value
                                if position[0] == "4":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2_3 * config.fourth)      
                                    weighted_dict[key] = value
                                if position[0] == "5":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2_3 * config.fifth)
                                    weighted_dict[key] = value
                                if position[0] == "6":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2_3 * config.sixth)  
                                    weighted_dict[key] = value
                                if position[0] == "7":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2_3 * config.seventh)
                                    weighted_dict[key] = value
                                if position[0] == "8":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C2_3 * config.eighth)       
                                    weighted_dict[key] = value     
                            if grade == "3":
                                if position[0] == "1":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3 * config.first)
                                    weighted_dict[key] = value
                                if position[0] == "2":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3 * config.second)   
                                    weighted_dict[key] = value
                                if position[0] == "3":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3 * config.third)
                                    weighted_dict[key] = value
                                if position[0] == "4":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3 * config.fourth) 
                                    weighted_dict[key] = value     
                                if position[0] == "5":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3 * config.fifth)
                                    weighted_dict[key] = value
                                if position[0] == "6":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3 * config.sixth) 
                                    weighted_dict[key] = value
                                if position[0] == "7":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3 * config.seventh)
                                    weighted_dict[key] = value
                                if position[0] == "8":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3 * config.eighth)    
                                    weighted_dict[key] = value  
                            elif grade == "3/4":
                                if position == "1":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3_4 * config.first)
                                    weighted_dict[key] = value
                                if position == "2":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3_4 * config.second)   
                                    weighted_dict[key] = value
                                if position == "3":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3_4 * config.third)
                                    weighted_dict[key] = value
                                if position == "4":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3_4 * config.fourth)  
                                    weighted_dict[key] = value    
                                if position == "5":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3_4 * config.fifth)
                                    weighted_dict[key] = value
                                if position == "6":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3_4 * config.sixth) 
                                    weighted_dict[key] = value 
                                if position == "7":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3_4 * config.seventh)
                                    weighted_dict[key] = value
                                if position == "8":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C3_4 * config.eighth)   
                                    weighted_dict[key] = value                       
                            elif grade == "4":
                                if position[0] == "1":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4 * config.first)
                                    weighted_dict[key] = value
                                if position[0] == "2":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4 * config.second)   
                                    weighted_dict[key] = value
                                if position[0] == "3":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4 * config.third)
                                    weighted_dict[key] = value
                                if position[0] == "4":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4 * config.fourth)  
                                    weighted_dict[key] = value    
                                if position[0] == "5":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4 * config.fifth)
                                    weighted_dict[key] = value
                                if position[0] == "6":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4 * config.sixth)  
                                    weighted_dict[key] = value
                                if position[0] == "7":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4 * config.seventh)
                                    weighted_dict[key] = value
                                if position[0] == "8":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4 * config.eighth)     
                                    weighted_dict[key] = value 
                            elif grade == "4_5":
                                if position[0] == "1":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4_5 * config.first)
                                    weighted_dict[key] = value
                                if position[0] == "2":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4_5 * config.second)   
                                    weighted_dict[key] = value
                                if position[0] == "3":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4_5 * config.third)
                                    weighted_dict[key] = value
                                if position[0] == "4":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4_5 * config.fourth)    
                                    weighted_dict[key] = value  
                                if position[0] == "5":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4_5 * config.fifth)
                                    weighted_dict[key] = value
                                if position[0] == "6":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4_5 * config.sixth)  
                                    weighted_dict[key] = value
                                if position[0] == "7":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4_5 * config.seventh)
                                    weighted_dict[key] = value
                                if position[0] == "8":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C4_5 * config.eighth)    
                                    weighted_dict[key] = value                             
                            elif grade == "5":
                                if position[0] == "1":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C5 * config.first)
                                    weighted_dict[key] = value
                                if position[0] == "2":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C5 * config.second)  
                                    weighted_dict[key] = value 
                                if position[0] == "3":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C5 * config.third)
                                    weighted_dict[key] = value
                                if position[0] == "4":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C5 * config.fourth)     
                                    weighted_dict[key] = value 
                                if position[0] == "5":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C5 * config.fifth)
                                    weighted_dict[key] = value
                                if position[0] == "6":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C5 * config.sixth)  
                                    weighted_dict[key] = value
                                if position[0] == "7":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C5 * config.seventh)
                                    weighted_dict[key] = value
                                if position[0] == "8":
                                    value = value * (1 + config.RECENT_WEIGHTING * config.rec_C5 * config.eighth)   
                                    weighted_dict[key] = value   
                            else:
                                value = value
                        except IndexError:
                            break
                    j += 1
                            
    return weighted_dict