year_input = int(input('Enter the year of interest: '))
life_expectancies = []
life_expectancy2 = []
years = []

life_expectancy_sun = 0
count = 0
#opens up the csv file 
with open("life-expectancy.csv") as life:
    next(life)
#Iterate through the CSV file and Division in to Part
    for item in life:
        #print(item)
        part = item.strip().split(',')
        country_name = part[0]
        country_code = part[1]
        year = int(part[2])
        life_exp = float(part[3])
#finds the overall maximun and minimun life expectancy
        life_expectancies.append(life_exp)
        max_life_expectancy = max(life_expectancies)
        min_life_expectancy = min(life_expectancies)
#Tells  overall Year and Country of the maximun and minimun life expectancy
        if life_exp == max_life_expectancy:
            max_year_name = year
            max_country_name = country_name
        elif life_exp == min_life_expectancy:
            min_year_name = year
            min_country_name = country_name
# calculation for Average life Expectancy of the input
        if year == year_input:
            life_expectancy_sun += life_exp
            count +=1
# calculation of maximun life Expectancy of the input year
            life_expectancy2.append(life_exp)
            max_life_expectancy2 = max(life_expectancy2)
            min_life_expectancy2 = min(life_expectancy2)

            if life_exp == max_life_expectancy2:
                max_country_name2 = country_name
            elif life_exp == min_life_expectancy2:
                min_country_name2 = country_name

    if count > 0:
        average_life_expectancy = life_expectancy_sun / count

print(f'The overall max life expectancy is: {max_life_expectancy} from {max_country_name} in {max_year_name}')
print(f'The overall min life expectancy is: {min_life_expectancy} from {min_country_name} in {min_year_name}\n')

print(f'For the Year {year_input}:')
print(f'The average life expectancy across all countries was {average_life_expectancy:.2f}')
print(f'The max life expectancy was in {max_country_name2} with {max_life_expectancy2}')
print(f'The max life expectancy was in {min_country_name2} with {min_life_expectancy2}')
