#initialize global values
total_total_counter = 0
total_total_distance = 0

#Define file processing function
def processFile(fh):
    #Declare global values
    global total_total_counter
    global total_total_distance
    file_object = open(file_name, 'r')
    printKV("File to b e read", fh, 25)
    #initialize values
    partial_total_counter = 0
    partial_total_distance = 0
    #Use for loop to accumulate the total counter and total distance for every lines in each files
    for line in file_object:
        partial_total_counter += 1
        partial_total_distance += float(line.split(",")[1].rstrip('\n'))
    file_object.close()
    #accumulate global values for all files
    total_total_counter += partial_total_counter
    total_total_distance += partial_total_distance

    return partial_total_counter, partial_total_distance

#Define printKV function
def printKV(key,value,klen=0):
    #Initialize the variable of formatting values
    Value_format = 0
    #define the way of formatting key words in printKV function
    key_format = "{:<25}".format(key)
    #Since there are three types of values, I use if-elif to separate these three cases
    # and use isinistance function to write conditions
    if isinstance(value,str):
        Value_format = "{:<20}".format(value)
    elif isinstance(value,int):
        Value_format = "{:<10}".format(value)
    elif isinstance(value, float):
        Value_format = "{:<10.3f}".format(value)
    # I use print function to print these two format variables in one line
    print(key_format+':'+Value_format)
    return

# This is the main process to execute files
# Since the goal is to ask users to enter file name indefinitely, I use while loop
while(True):
    #I use input function to ask users to enter file names indefinitely
    file_name = input('Please type the file name\n')
    #There are three types of ways users will write to declare they want to quit processing file
    condition1 = " "
    condition2 = "quit"
    condition3 = 'q'
    #If file name satisfies one of these three condtions, it will print the total global values by using printKV function
    if file_name == condition1 or file_name == condition2 or file_name == condition3:
       printKV("File to be read", "quit",25)
       print("\nTotals")
       printKV("Total # of lines", total_total_counter, 25)
       printKV("Total distance run", total_total_distance, 25)

    #If file name does not satisfy any of these conditions, I call back file processing function to accumulate the data in each files
    #and call back print function to print partial total number of lines and partial total distance run
    else:
        result = processFile(file_name)
        printKV('Partial Total # of Lines', result[0], 25)
        printKV('Partial Total distance run', result[1], 25)




