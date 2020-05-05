def factor(num, i):
    while i <= num:
        if num % i == 0:
            break
        i += 1

    print("the smallest factor is %d" % (i))


if __name__ == "__main__":
    num = eval(input())
    i = 2
    factor(num, i)
