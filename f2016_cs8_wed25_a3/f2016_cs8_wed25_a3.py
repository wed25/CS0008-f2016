#
# MN: header with user, instructor and course info is missing
#
# Notes:
# MN: I strongly suggest to avoid globals and use argumnet passing in and out functions
# MN: A little bit more comments
#

#create the empty list and dictionary 
file_name_list = []
Max_run = []
Min_run = []
# MN: you should describe what is the structure of this variable
#     something like:
#     element 0 is the runs counter
#     element 1 is the total distance run by the participant
# MN: be careful to correctly initialize it once you start populating it
output_file = {}

#initialize the variables 
total_line = 0
total_distance = 0
total_file_read = 0
Total_Multiple_record = 0


#create the function to do the main processing 
def processFile(fh):
    # MN: I STRONGLY suggest to NOT use globals
    global total_line
    global total_distance
    global Total_Multiple_record


    #use for loop to calculate the total number of line and total distance 
    for line in file_object:
        if (line.split(",")[0] != "name"):
            file_line = line.split(",")
            total_line += 1
            total_distance += float(file_line[1].rstrip('\n'))

            # check if the name of participants is in the line
            if file_line[0] in output_file:
                #if it is in it and it is the first time in the record,
                #the number total_multiple will accumulate one time 
                # MN: you should test for 1, that's the value we initialize it to
                #if output_file[file_line[0]][0] == 0:
                if output_file[file_line[0]][0] == 1:
                    Total_Multiple_record += 1
                #if it is not the first time,
                # the number total_multiple will accumulate one time
                # the total distance will accumulate as well
                output_file[file_line[0]][0] += 1
                output_file[file_line[0]][1] += float(file_line[1].rstrip('\n'))
                file_line[1] = output_file[file_line[0]][1]
            else:
                # MN: when this branch is execute you have found the name once, so your counter should be initialize adequately
                output_file[file_line[0]] = [1, float(file_line[1])]
            
            # MN: if you execute this statement in every iteration
            #     you re-initialize it every time
            #     You should place it in a else branch of the previous if
            #output_file[file_line[0]] = [0, float(file_line[1])]

            #recall the function Max_Min to calculate the max and min number of distance in the list 
            Max_Min(file_line)
  
    return

#define the new function called Max_Min 
def Max_Min(file_line):
    # MN: I STRONGLY suggest to NOT use globals
    global Max_run
    global Min_run

    file_line[1] = float(str(file_line[1]).rstrip("\n"))
    if len(Max_run)>0 and len(Min_run)>0:
        if float(file_line[1]) > float(Max_run[1]):
            Max_run = file_line
        elif float(file_line[1]) < float(Min_run[1]):
            Min_run = file_line
        return
    Max_run = file_line
    Min_run = file_line
    return





#Define printKV function
def printKV(key,value,klen=0):
    #Initialize the variable of formatting values
    Value_format = 0
    #define the way of formatting key words in printKV function
    key_format = "{:<30}".format(key)
    #Since there are three types of values, I use if-elif to separate these three cases
    # and use isinistance function to write conditions
    if isinstance(value,str):
        Value_format = "{:<40}".format(value)
    elif isinstance(value,int):
        Value_format = "{:<40}".format(value)
    elif isinstance(value, float):
        Value_format = "{:<40.5f}".format(value)
    # I use print function to print these two format variables in one line
    print(key_format+':'+Value_format)
    return




# start the main process
# first open the file name list to read
# MN: why not ask user for the master list file? 
in_file = open("f2016_cs8_a3.data.txt", 'r')
for line in in_file:
    file_name_list.append(line.rstrip("\n"))
in_file.close()

while(len(file_name_list)>0):

    total_file_read +=1
    file_name = file_name_list.pop()
    # read the last name in the list each time and remove the name from the list after finishing reading 
    file_object = open(file_name,'r')
    processFile(file_name)
    file_object.close()

#create an output file reporting name of the participantn how many their name appears in the input files
#and total distance run 
f = open("f2016_cs8_wed25_a3.data.output.csv", 'w')
for item, value in output_file.items():
    f.write(str(item)+','+str(value[0])+','+str(value[1])+'\n')

f.close()

printKV("Number of input files read",total_file_read, 30 )
printKV("Total number of Lines read",total_line, 30)
printKV("Total distance run", total_distance, 30)
printKV("Max distance run", Max_run[1], 30)
printKV("    by participant", Max_run[0], 30)
printKV("Min distance run", Min_run[1], 30)
printKV("    by participant", Min_run[0],30)
printKV("Total number of participants", len(output_file), 30)
print("Number of participants")
printKV("with multiple record", Total_Multiple_record, 30)
