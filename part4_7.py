

def leapyear(year):
    '''

    check the year is leap year or not

    '''

    while year != -9999:
        if year %400 ==0 or (year %4 ==0 and year %100 != 0 ):
            print(year,'is a leap year.')
        else :
            print(year, 'is not a leap year.')
        year=eval(input())


if __name__ == '__main__':
    year = eval(input())
    leapyear(year)