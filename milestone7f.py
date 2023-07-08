tem_input = float(input('What is the Temperature? '))
unit_input = input('Fahrenheit or Celsius (F/C)? ').upper()


def cal_wind_chill(v, tem):
        wind_chill = 35.74 + 0.6215 * tem - 35.75 * v**0.16 + 0.4275*tem*v**0.16
        return wind_chill
    
def unit_convert (u):
    cen_convert = u * 9/5 + 32 
    return cen_convert

while True:
    if unit_input.upper() == 'F':
        for i in range(5,65,5):
            print(f'At temperature {tem_input:.1f}{unit_input}, and wind speed {i} mph, the windchill is: {cal_wind_chill(i,tem_input):.2f}{unit_input}')
        break
    elif unit_input.lower() == 'c':
        for i in range(5,65,5):
            print(f'At temperature {unit_convert(tem_input):.1f}F, and wind speed {i} mph, the windchill is: {cal_wind_chill(i,unit_convert(tem_input)):.2f}F')
        break
    else:
        print('\nWrong Alphabet, Please input C or F')
        unit_input = input('Fahrenheit or Celsius (F/C)? ').upper()
