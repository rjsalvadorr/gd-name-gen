import random
from random import randrange
from datetime import datetime, timedelta

#/////////#/////////#/////////#/////////#/////////#/////////
#///////////   LOADING FILES

businessNames = open("data/business-names.txt", "r", encoding='utf-8')
businessIndustryList = open("data/business-industry-list.txt", "r", encoding='utf-8')

countryNames = open("data/country-names.txt", "r", encoding='utf-8')
countryCodes = open("data/country-codes.txt", "r", encoding='utf-8')
cityNames = open("data/city-names.txt", "r", encoding='utf-8')
streetNames = open("data/street-names.txt", "r", encoding='utf-8')

personNames = open("data/person-names.txt", "r", encoding='utf-8')


#/////////#/////////#/////////#/////////#/////////#/////////
#///////////    UTILITY FUNCTIONS

def random_line(afile, default=None):
    line = default
    for i, aline in enumerate(afile, start=1):
        if randrange(i) == 0:  # random int [0..i)
            line = aline
    return line

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def random_num_string():
    rNum = random.randint(1, 9999)
    return f'{rNum:04}'
	
#/////////#/////////#/////////#/////////#/////////#/////////
#///////////    TEXT GENERATION

f = open("output-business-prompt.txt", "w", encoding='utf-8')
numPrompts = 12

outStr = '\n////////////////////////////////////////////////////////////\n'
outStr += '//////   GENERATOR -- BUSINESS GRAPHIC BRIEF\n\n'

print(outStr)
f.write(outStr)

for x in range(numPrompts):
    loopStr = f'\n\n\n//////   CLIENT {(x + 1):03}   //////////////////////////////\n\n'

    businessNames.seek(0)
    loopStr += f'BUSINESS NAME: {random_line(businessNames).rstrip()}\n'

    busIndustries = '\nINDUSTRIES/BUSINESS SECTORS: \n\n'
    for x in range(3):
        businessIndustryList.seek(0)
        busIndustries += f'- {random_line(businessIndustryList).rstrip()}\n'
    loopStr += f'{busIndustries}\n'

    loopStr += 'HEAD OFFICE: \n\n'
    streetNames.seek(0)
    cityNames.seek(0)
    countryNames.seek(0)

    addrNum = random.randint(1, 3999)
    addrStreet = random_line(streetNames).rstrip()
    addrCity = random_line(cityNames).rstrip()
    addrCountry = random_line(countryNames).rstrip()
    addrPhone = f'{random_num_string()}-{random_num_string()}{random_num_string()}'

    headOfficeLocation = f'{addrNum} {addrStreet}\n{addrCity}, {addrCountry}\n{addrPhone}'
    loopStr += f'{headOfficeLocation}\n\n'

    numLocations = random.randint(0,4)
    loopStr += ('', 'OTHER LOCATIONS: \n\n')[numLocations > 0]
    for x in range(numLocations):
        streetNames.seek(0)
        cityNames.seek(0)
        countryNames.seek(0)

        sattNum = random.randint(1, 3999)
        sattStreet = random_line(streetNames).rstrip()
        sattCity = random_line(cityNames).rstrip()
        sattCountry = random_line(countryNames).rstrip()
        sattPhone = f'{random_num_string()}-{random_num_string()}{random_num_string()}'

        satelliteLocation = f'{sattNum} {sattStreet}\n{sattCity}, {sattCountry}\n{sattPhone}'
        loopStr += f'{satelliteLocation}\n\n'

    numPersonnel = random.randint(2, 8)
    loopStr += 'PERSONNEL: \n\n'
    for x in range(numPersonnel):
        personNames.seek(0)
        pName = random_line(personNames).rstrip()
        pPhone = f'{random_num_string()}-{random_num_string()}{random_num_string()}'
        loopStr += f'{pName}\n{pPhone}\n\n'

    print(loopStr)
    f.write(loopStr)

f.close()
