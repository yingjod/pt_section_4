def prime(a):
    '''

    to check the number is prime or not

    '''
    isprime=1
    divisor=2
    while divisor <= a/2 :
        if a % divisor == 0 :
            isprime = 0
            break
        divisor += 1
    if isprime == 1 :
        print('%d is a prime number.'%(a))
    else:
        print('%d is not a prime number.'%(a))

if __name__ == '__main__':

    a=eval(input())
    prime(a)
