

def check(year1,year2):
    '''

    print out all of the leap year from year1 to year2

    '''
    for i in range(year1,year2+1):
        if i % 400 ==0 or ( i % 4 ==0 and i % 100 != 0 ):
            print('%5d'%(i),end = '')


if __name__ == '__main__':
    year1,year2=eval (input())
    check(year1,year2)