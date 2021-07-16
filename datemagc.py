''' magic dates'''

def date():
    month = int(input('M: '))
    day = int(input('D: '))
    year = int(input('Y(2-digits): '))    
    
    if month * day == year:
        print(f'\nDate: {month}/{day}/{year} is a magic!')
    else:
        print(f'\nDate: {month}/{day}/{year} is not magic!')
date()