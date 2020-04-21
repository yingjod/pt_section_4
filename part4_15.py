def prime(number):
    '''

    to print out "number" different numbers of prime

    '''

    a = 2
    count = 0
    while count < number:
        isprime=1
        divisor=2
        while divisor <= a/2:
            if a % divisor ==0:
                isprime = 0
                break
            divisor += 1
        if isprime == 1:
            count += 1
            print(a,end=" ")
        a+=1

if __name__ == '__main__':
    number = eval(input())
    print('The first %d prime numbers are : ' % (number))
    prime(number)
