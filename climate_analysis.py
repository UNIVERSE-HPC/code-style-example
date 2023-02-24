import string


shift = 3
comment = '#'
climate_data = open('data/sc_climate_data_10.csv', 'r')

def FahrToCelsius(fahr):
    celsius = ((fahr - 32) * (5/9)) 
    return celsius
def FahrToKelvin(fahr):
    kelvin = FahrToCelsius(fahr) + 273.15
    return kelvin



for line in climate_data:
    data = line.split(',')
    if data[0][0] != comment:
        fahr = float(data[3])
        celsius = FahrToCelsius(fahr)
        kelvin = FahrToKelvin(fahr)
        print('Max temperature in Celsius', celsius, 'Kelvin', kelvin)
