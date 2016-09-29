= 'USC'
b = 'Metric'
original_unit = input('Which system you use either a or b: ')
distance_quantity_original = float(input('Enter the distance driven: '))
gasoline_quantity_original = float(input('Enter the amount of gasoline was used: '))

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

if consumption_quantity_Metric > 20:
    Rating = input('extremely poor')
elif consumption_quantity_Metric > 15 and consumption_quantity_Metric <= 20:
    Rating = input('poor')
elif consumption_quantity_Metric > 10 and consumption_quantity_Metric <= 15:
    Rating = input('average')
elif consumption_quantity_Metric > 8 and consumption_quantity_Metric <= 10:
    Rating = input('Good')
else:
    Rating = input('Excellent')

c = format(distance_quantity_USC, '15.3f')
d = format(distance_quantity_Metric, '15.3f')
e = format(gasoline_quantity_USC, '15.3f')
f = format(gasoline_quantity_Metric, '15.3f')
g = format(consumption_quantity_USC, '15.3f')
h = format(consumption_quantity_Metric, '15.3f')


print(distance_quantity_USC)
print(distance_quantity_Metric)
print(gasoline_quantity_USC)
print(gasoline_quantity_Metric)
print(consumption_quantity_USC)
print(consumption_quantity_Metric)
print(Rating)

print('USC''Metric')
print("'Distance____', format(distance_quantity_USC, '.3f'), format(distance_quantity_Metric,'.3f')")
print("'Gas____', format(gasoline_quantity_USC, '.3f'), format(gasoline_quantity_Metric,'.3f')")
print("'Consumption____' + format(consumption_quantity_USC, '.3f') + format(consumption_quantity_Metric,'.3f')")
print('Gas Consumption Rating: ', Rating)

format(width.3f)
x = format)()