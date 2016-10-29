#initialize values
total_total_counter = 0
total_total_distance = 0

#Define file processing function
def processFile(fh):
    global total_total_counter
    global total_total_distance
    file_object = open(file_name, 'r')
    printKV("File to b e read", fh, 25)
    #initialize values
    partial_total_counter = 0
    partial_total_distance = 0
    for line in file_object:
        partial_total_counter += 1
        partial_total_distance += float(line.split(",")[1].rstrip('\n'))
    file_object.close()

    total_total_counter += partial_total_counter
    total_total_distance += partial_total_distance

    return partial_total_counter, partial_total_distance

#Define print function
def printKV(key,value,klen=0):
    Value_format = 0
    key_format = "{:<25}".format(key)
    if isinstance(value,str):
        Value_format = "{:<20}".format(value)
    elif isinstance(value,int):
        Value_format = "{:<10}".format(value)
    elif isinstance(value, float):
        Value_format = "{:<10.3f}".format(value)

    print(key_format+':'+Value_format)
    return

# Since the goal is to ask users to enter file name indefinitely, I use while loop
while(True):
    file_name = input('Please type the file name\n')

    condition1 = " "
    condition2 = "quit"
    condition3 = 'q'
    if file_name == condition1 or file_name == condition2 or file_name == condition3:
       printKV("File to be read", "quit",25)
       print("\nTotals")
       printKV("Total # of lines", total_total_counter, 25)
       printKV("Total distance run", total_total_distance, 25)

# call back file processing function and print function
    else:
        result = processFile(file_name)
        printKV('Partial Total # of Lines', result[0], 25)
        printKV('Partial Total distance run', result[1], 25)




