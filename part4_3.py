
def check(a,b):
    '''

    to show all the multiples of 4 and 9 from a to b

    '''
    count = total_sum = 0
    time = 10
    for i in range (a,b+1):
        if i % 4 == 0 or i % 9 == 0:
            print('%-4d'%i,end=' ')
            total_sum += i
            count += 1
            if count % time == 0 :
                print()

    if count > 0 and count % 10 != 0 :
        print()

    print('%d'%count)
    print(total_sum)

if __name__ == '__main__':
    a=eval(input())
    b=eval(input())
    check(a,b)
