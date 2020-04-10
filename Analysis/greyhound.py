# greyhound.py

# Need to add in sprint speed variable.
class Greyhound:

    def __init__(self, name, age, breeding, grade, comment, fastest, owners, performance, 
    scratched, number, all_stat, track_stat, track_and_distance_stat, sprint_stat, middle_stat, 
    distance_stat, box_1_stat, box_2_stat, box_3_stat, box_4_stat, box_5_stat, box_6_stat, box_7_stat, box_8_stat, 
    prize, trainer, trainer_district, win_record, barrier):
        self.name = name
        self.age = age
        self.breeding = breeding
        self.grade = grade
        self.comment = comment
        self.fastest = fastest
        self.owners = owners
        self.performance = performance
        self.scratched = scratched
        self.number = number
        self.all_stat = all_stat
        self.track_stat = track_stat
        self.track_and_distance_stat = track_and_distance_stat
        self.sprint_stat = sprint_stat
        self.middle_stat = middle_stat
        self.distance_stat = distance_stat
        self.box_1_stat = box_1_stat
        self.box_2_stat = box_2_stat
        self.box_3_stat = box_3_stat
        self.box_4_stat = box_4_stat
        self.box_5_stat = box_5_stat
        self.box_6_stat = box_6_stat
        self.box_7_stat = box_7_stat
        self.box_8_stat = box_8_stat    
        self.prize = prize
        self.trainer = trainer
        self.trainer_district = trainer_district
        self.win_record = win_record
        self.barrier = barrier

    def break_up_performance(self):
        """ Sort the performance text into sensibleness. """
        race_tuple = tuple()
        performance_tuple_array = []
        performance_list = self.performance.split('},{')
        for performance_line in performance_list:
            breakup = performance_line.split(' ')

            box = breakup[1] 
            box = box[0] # Box number is first element of second array string.

            track = breakup[1]
            track = track[22:26]

            position = breakup[5]
            position = position[0]

            runners = breakup[7]
            runners = runners[0]

            grade = breakup[7]
            grade = grade[4:]

            distance = breakup[8]
            distance = distance[:-1]

            race_tuple = (box, track, position, runners, grade, distance)
            performance_tuple_array.append(race_tuple)
        
        return performance_tuple_array

    def sort_win_record(self):
        """Put into sense the win record line. """
        # For now:
        return self.win_record

    def ret_all_stat(self):
        """ Assign their all stat win and place ratios. """
        val_list = self.all_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2]) + int(val_list[3])) / int(val_list[0]))

        return win_rate, place_rate

    def ret_track_stat(self):
        """ Assign their track stat win and place ratios. """   
        val_list = self.track_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate

    def ret_track_and_distance_stat(self):
        """ Assign their track and distance stat win and place ratios. """     
        val_list = self.track_and_distance_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate

    def ret_sprint_stat(self):
        """ Assign their sprint stat win and place ratios. """   
        val_list = self.sprint_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate   

    def ret_middle_stat(self):
        """ Assign their middle stat win and place ratios. """  
        val_list = self.middle_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate

    def ret_distance_stat(self):
        """ Assign their distance stat win and place ratios. """
        val_list = self.distance_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate    

    def ret_box_1_stat(self):
        """ Assign their box 1 stat win and place ratios. """
        val_list = self.box_1_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate
    
    def ret_box_2_stat(self):
        """ Assign their box 2 stat win and place ratios. """
        val_list = self.box_2_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate

    def ret_box_3_stat(self):
        """ Assign their box 3 stat win and place ratios. """
        val_list = self.box_3_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate

    def ret_box_4_stat(self):
        """ Assign their box 4 stat win and place ratios. """
        val_list = self.box_4_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate

    def ret_box_5_stat(self):
        """ Assign their box 5 stat win and place ratios. """
        val_list = self.box_5_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate

    def ret_box_6_stat(self):
        """ Assign their box 6 stat win and place ratios. """
        val_list = self.box_6_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate

    def ret_box_7_stat(self):
        """ Assign their box 7 stat win and place ratios. """
        val_list = self.box_7_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate

    def ret_box_8_stat(self):
        """ Assign their box 8 stat win and place ratios. """
        val_list = self.box_8_stat.split(':')
        win_rate = float(int(val_list[1]) / int(val_list[0]))
        place_rate = float((int(val_list[1]) + int(val_list[2])) / int(val_list[0]))

        return win_rate, place_rate


        
