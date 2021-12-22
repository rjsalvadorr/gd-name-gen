import random
from random import randrange
from datetime import datetime, timedelta

#/////////#/////////#/////////#/////////#/////////#/////////
#///////////   LOADING FILES

bandNames = open("band-names.txt", "r", encoding='utf-8')
albumNames = open("album-names.txt", "r", encoding='utf-8')
cityNames = open("city-names.txt", "r", encoding='utf-8')
countryNames = open("country-names.txt", "r", encoding='utf-8')
genreNames = open("genre-list.txt", "r", encoding='utf-8')


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
	
	
#/////////#/////////#/////////#/////////#/////////#/////////
#///////////    TEXT GENERATION

outStr = '\n////////////////////////////////////////////////////////////\n'
outStr += '//////   GENERATOR -- BUSINESS GRAPHIC BRIEF\n\n'

# outStr += f'BAND NAME: {random_line(bandNames).rstrip()}\n'
# bandNames.seek(0)
# outStr += f'ALBUM NAME: {random_line(bandNames).rstrip()}\n'
# bandGenres = 'GENRE(S): '
# for x in range(4):
#     genreNames.seek(0)
#     delim = (",", "")[x == 0]
#     bandGenres += f'{delim} {random_line(genreNames).rstrip()}'
# outStr += f'{bandGenres}\n'
# 
# outStr += '\nTRACKLIST: \n'
# numTracks = random.randint(6,13)
# 
# for x in range(numTracks):
#     bandNames.seek(0)
#     bName = random_line(bandNames).rstrip()
#     trackNum = x + 1
#     trackMinutes = random.randint(0,8)
#     trackSecs = random.randint(0,59)
# 	
#     outStr += f'{trackNum:02} - {bName} ({trackMinutes}:{trackSecs:02})\n'
# 
# bandNames.seek(0)
# albumNames.seek(0)
# tNames = random_line(bandNames).rstrip()
# tNames += f' - OR - {random_line(albumNames).rstrip()}'
# outStr += f'\nTOUR NAME:\n{tNames}\n'
# 
# outStr += '\nTOUR STOPS: \n'
# numCities = random.randint(6,20)
# tourStart = datetime.strptime('1/1/2032 1:30 PM', '%m/%d/%Y %I:%M %p')
# tourEnd = datetime.strptime('12/30/2099 4:50 AM', '%m/%d/%Y %I:%M %p')
# 
# for x in range(numCities):
#     cityNames.seek(0)
#     countryNames.seek(0)
#     eventDay = random_date(tourStart, tourEnd).strftime("%b %d, %Y")
#     outStr += f'{eventDay} - {random_line(cityNames).rstrip()}, {random_line(countryNames).rstrip()}\n'

print(outStr)