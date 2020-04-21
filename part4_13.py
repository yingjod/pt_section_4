
def hcf(a,b,c):
    '''

    highest common factor in these three numbers

    '''
    gcd=1
    k=2
    while k <= a and k <= b and k <= c:
        if a % k == 0 and b % k == 0 and c % k == 0 :
            gcd=k
        k += 1
    print('gcd(%d,%d,%d)=%d'%(a,b,c,gcd))

if __name__ == '__main__':

    a=eval(input())
    b=eval(input())
    c=eval(input())
    hcf(a,b,c)