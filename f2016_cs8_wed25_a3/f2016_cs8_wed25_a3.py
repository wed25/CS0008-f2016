

file_name_list = []
Max_run = []
Min_run = []
output_file = {}

total_line = 0
total_distance = 0
total_file_read = 0
Total_Multiple_record = 0



def processFile(fh):
    global total_line
    global total_distance
    global Total_Multiple_record


    file_object = open(fh,'r')
    for line in file_object:
        if (line.split(",")[0] != "name"):
            file_line = line.split(",")
            total_line += 1
            total_distance += float(file_line[1].rstrip('\n'))


            if file_line[0] in output_file:
                if output_file[file_line[0]][0] == 0:
                    Total_Multiple_record += 1
                output_file[file_line[0]][0] += 1
                output_file[file_line[0]][1] += float(file_line[1].rstrip('\n'))

            output_file[file_line[0]] = [0, float(file_line[1].rstrip('\n'))]

            Max_Min(file_line)


    file_object.close()
    return

def Max_Min(file_line):
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




# start
in_file = open("f2016_cs8_a3.data.txt", 'r')
for line in in_file:
    file_name_list.append(line.rstrip("\n"))
in_file.close()

while(len(file_name_list)>0):

    total_file_read +=1
    file_name = file_name_list.pop()

    processFile(file_name)


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
