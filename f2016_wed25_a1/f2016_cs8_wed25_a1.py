#The first input goal is to ask for the user about the system he/she want to use.
#I first assign 'USC' as a string to the variable 'a',
#and also assign 'Metric' as a string to the variable 'b' .
#Then I use the input function to ask user 'which system he or she use either a or b',
#and assign this answer to the variable 'original_unit'.
a = 'USC'
b = 'Metric'
original_unit = input('Which system you use either a or b: ')

#The second input goal is to ask for two basic quantities I need to use,
# which are distance and the amount of gasoline.
distance_quantity_original = float(input('Enter the distance driven: '))
gasoline_quantity_original = float(input('Enter the amount of gasoline was used: '))

#I use the if-else statement to
#convert the quantity provided by the user in the other units system,
#calculate the fuel consumption in both units,
#and get the rating information
if original_unit == a:
    distance_quantity_USC = distance_quantity_original
    gasoline_quantity_USC = gasoline_quantity_original
    distance_quantity_Metric = 1.60934 * distance_quantity_USC
    gasoline_quantity_Metric = 3.78541 * gasoline_quantity_USC
    consumption_quantity_USC = distance_quantity_USC / gasoline_quantity_USC
    consumption_quantity_Metric = 100 * gasoline_quantity_Metric / distance_quantity_Metric
else:
    distance_quantity_Metric = distance_quantity_original
    gasoline_quantity_Metric = gasoline_quantity_original
    distance_quantity_USC = 0.621371 * distance_quantity_Metric
    gasoline_quantity_USC = 0.264172 * gasoline_quantity_Metric
    consumption_quantity_USC = distance_quantity_USC / gasoline_quantity_USC
    consumption_quantity_Metric = 100 * gasoline_quantity_Metric / distance_quantity_Metric

#I use the if statement to get the rating categories
if consumption_quantity_Metric > 20:
    Rating = 'extremely poor'
elif consumption_quantity_Metric > 15 and consumption_quantity_Metric <= 20:
    Rating = 'poor'
elif consumption_quantity_Metric > 10 and consumption_quantity_Metric <= 15:
    Rating = 'average'
elif consumption_quantity_Metric > 8 and consumption_quantity_Metric <= 10:
    Rating = 'Good'
else:
    Rating = 'Excellent'

# format the quantities variables as float with 3 decimal)
c = format(distance_quantity_USC, '.3f')
d = format(distance_quantity_Metric, '.3f')
e = format(gasoline_quantity_USC, '.3f')
f = format(gasoline_quantity_Metric, '.3f')
g = format(consumption_quantity_USC, '.3f')
h = format(consumption_quantity_Metric, '.3f')

# print the final format output
print('                                       USC                     Metric')
print('Distance______________:         ' + c + ' miles                ' + d + ' km')
print('Gas___________________:         ' + e + ' gallons              ' + f + ' Liters')
print('Consumption___________:         ' + g + '   mpg                 ' + h + '  1/100KM')
print('Gas Consumption Rating:         ' + Rating)

