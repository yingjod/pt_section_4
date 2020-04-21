
def BMIcheck(height):
    '''

    to count the BMI

    '''
    state = ' '
    while height != -9999:
        weight = eval (input())
        bmi = weight / (height/100)**2
        if weight == -9999:
            break
        elif bmi >= 30:
            state='fat'
        elif bmi >=25 and bmi <30:
            state='over weight'
        elif bmi >=18.5 and bmi <25:
            state='normal'
        elif bmi <18.5:
            state='under weight'
        print('BMI: %.2f '%bmi)
        print('State:%s'%state)

        height=eval(input())

if __name__ == '__main__':
    height = eval(input())
    BMIcheck(height)
