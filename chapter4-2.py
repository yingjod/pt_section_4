num1 = eval(input("enter a number1 : "))
num2 = eval(input("enter a number2 : "))
factor = 2
gcd = 1


while factor <= num1 and factor <= num2:
    if num1 % factor == 0 and num2 % factor == 0:
        gcd = factor
    factor += 1

print("the greatest common factor is %d" % gcd)
