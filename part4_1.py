

def min(min_num):
    '''

    enter 10 numbers and print out the minimum one.

    '''
    total = 10
    for i in range (total-1):
        num=eval(input())
        if num < min_num :
            min_num = num

if __name__ == '__main__':
    min_num=eval(input())
    min(min_num)
    print(min_num)

