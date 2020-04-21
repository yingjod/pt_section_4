
def check():

    '''

    will count how many odd and even in these 10 numbers
    '''
    even = odd = 0
    for i in range (10):
        a = int (input())
        if a % 2 == 0:
            even += 1
        else:
            odd += 1

    print('even numbers:',even)
    print('odd numbers:',odd)


check()