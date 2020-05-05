def check(start, end):
    for i in range(start, end + 1):
        isprime = 1
        divisor = 2
        while divisor <= i / 2:
            if i % divisor == 0:
                isprime = 0
                break
            divisor += 1
        if isprime == 1:
            print(i, end=" ")


if __name__ == "__main__":
    start = eval(input())
    end = eval(input())
    check(start, end)
