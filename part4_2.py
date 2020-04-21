

def min(num):
    '''

    from all of numbers to show the minimum one ,if enter 9999 will finish the program.

    '''
    min_mum=num
    while num != 9999:
        num=eval(input())
        if num < min_mum:
            min_mum = num
    return min_mum



if __name__ == '__main__':
    num = eval(input())
    y=min(num)
    print(y)
