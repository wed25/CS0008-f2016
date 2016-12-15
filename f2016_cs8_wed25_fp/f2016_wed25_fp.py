import sys
import time
import subprocess

# define class
class Participants():

    # name of the participant
    name = "Notfound"
    # accumulator for total distance
    distance = 0.0
    #accumulator for total number of runs
    runs = 0

#method
    def __init__(self, Name, distance=0.0,run=0):
        #initialize the method
        self.name = Name
        if distance > 0:

           self.distance = distance
           self.runs = 1

    #get the name of the participants
    def getName(self):
        return self.name

    #get the current value of distance
    def getDistance(self):
        return self.distance

    #add single distnace to the distance accumulator
    def addDistance(self,distance):
        if distance > 0:
             self.distance += distance
             self.runs += 1

    #add an array of distance to distance accumulator
    def addDistances(self,distances):
        for distance in distances:
            if distance in distances:
              self.distance += distance
              self.runs += 1
        return



    #stringify method
    def _str_(self):
        name_format = "{:>20s}".format(self.name)
        distance_format = "{:>9.4f}".format(self.distance)
        runs_format = "{:<4d}".format(self.runs)
        return "Name : "+name_format+". Distance run : "+distance_format+". Runs : "+runs_format


# create the empty list 
Max_run = None
Min_run = None
file_name_list = []
participant_Arr = []

# initialize the variables
total_line = 0
total_distance = 0.0
total_file_read = 0
Total_Multiple_record = 0


# create the function to do the main processing
def processFile(fh):

    global total_line
    global total_distance


    # use for loop to calculate the total number of line and total distance
    for line in file_object:
        if (line.split(",")[0] != "name"):
            file_line = line.split(",")
            file_line[1] = file_line[1].rstrip('\n')
            total_line += 1
            total_distance += float(file_line[1])


            Max_Min(List(file_line))
    return

def List(file_line):
    global Total_Multiple_record

    if len(participant_Arr) >= 1:
        for item in participant_Arr:
            # check if the name of participants is in the line
            if file_line[0] == item.getName():
                
                if item.runs == 1:
                    Total_Multiple_record += 1
                   
                item.addDistance(float(file_line[1]))
                return item
    File = Participants(file_line[0], float(file_line[1]), 1)
    participant_Arr.append(File)
    return File

                   


# define the new function called Max_Min
def Max_Min(participant):
    
    global Max_run
    global Min_run

    if Max_run is not None and Min_run is not None:   
        if participant.getDistance() > Max_run.getDistance():
            Max_run = participant
        elif participant.getDistance() < Min_run.getDistance():
            Min_run = participant
        return

    Max_run = participant
    Min_run = participant
    return


# Define printKV function
def printKV(key, value, klen=0):
    # Initialize the variable of formatting values
    Value_format = 0
    # define the way of formatting key words in printKV function
    key_format = "{:<30}".format(key)
    # Since there are three types of values, I use if-elif to separate these three cases
    # and use isinistance function to write conditions
    if isinstance(value, str):
        Value_format = "{:<40}".format(value)
    elif isinstance(value, int):
        Value_format = "{:<40}".format(value)
    elif isinstance(value, float):
        Value_format = "{:<40.5f}".format(value)
    # I use print function to print these two format variables in one line
    print(key_format + ':' + Value_format)
    return


# start the main process
# first open the file name list to read

masterFile = input("Please provide master file : ")
in_file = open(masterFile, 'r')
for line in in_file:
    file_name_list.append(line.rstrip("\n"))
in_file.close()

while (len(file_name_list) > 0):
    total_file_read += 1
    file_name = file_name_list.pop()
    # read the last name in the list each time and remove the name from the list after finishing reading
    file_object = open(file_name, 'r')
    processFile(file_name)
    file_object.close()

# create an output file reporting name of the participantn how many their name appears in the input files
# and total distance run
f = open("f2016_cs8_wed25_a3.data.output.csv", 'w')
for item in participant_Arr:
    f.write(str(item.getName()) + ',' + str(item.runs) + ',' + str(item.getDistance) + '\n')

f.close()

printKV("Number of input files read", total_file_read, 30)
printKV("Total number of Lines read", total_line, 30)
printKV("Total distance run", total_distance, 30)
printKV("Max distance run", Max_run.getDistance(), 30)
printKV("    by participant", Max_run.getName(), 30)
printKV("Min distance run", Min_run.getDistance(), 30)
printKV("    by participant", Min_run.getName(), 30)
printKV("Total number of participants", len(participant_Arr), 30)
print("Number of participants")
printKV("with multiple record", Total_Multiple_record, 30)
