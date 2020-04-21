


def reverse(number):
    '''

   reversal the digit of number

    '''
    if number == 0:
        print(number)
    else:
        while number != 0:
            print(number % 10 , end = ' ')
            number //= 10

if __name__ == '__main__':
    number = eval(input())
    reverse(number)
