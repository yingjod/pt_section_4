# import random
# for i in range(1,11):
#     randnum=random.randint(1,100)
#     print('%4d'%(randnum),end=' ')

# import random
# even=0
# odd=0
# for i in range(1,11):
#     randnum=random.randint(1,100)
#     print(randnum,end=' ')
#     if randnum % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(' \neven = %d , odd = %d'%(even,odd))


# import random
# times3=0
# times5=0
# times7=0
# other=0
# count=1
#
# for i in range (1,101):
#     flag=False
#     randnum=random.randint(1,100)
#     if count % 10 !=0:
#         print('%5d'%randnum,end=' ')
#     else:
#         print('%5d' % randnum)
#     count +=1
#
#     if randnum % 3 == 0:
#         times3 += 1
#         flag=True
#     if randnum % 5 == 0:
#         times5 += 1
#         flag = True
#     if randnum % 7 == 0:
#         times7 += 1
#         flag = True
#     if flag == False :
#         other += 1
# print('\n times3 = %d ,times5 = %d ,times7 = %d ,other = %d'%(times3,times5,times7,other))

# import random
# count=1
# while count <=10:
#     for i in range(1,7):
#         randnum= random.randint(1,49)
#         print('%3d'%(randnum),end = ' ')
#     print()
#     count+=1
# print('over')
#
#
# import random
# again=1
# while again ==1 :
#     for i in range(1,7):
#         randnum= random.randint(1,49)
#         print('%3d'%(randnum),end=' ')
#     print()
# #     again = eval(input('countinuw:1 or quit:0 ------->'))
# # print('over')
#
#
# import random
# while True:
#     for i in range(1,7):
#         randnum=random.randint(1,49)
#         print(randnum, end = ' ')
#     print()
#     again=eval (input('continue : 1 or quir ; 0 ------>'))
#     if again == 0 :
#         break
# print('over')

# import random
# num1=random.randint(1,100)
# num2=random.randint(1,100)
#
# while True:
#     solution=num1+num2
#     answer=eval(input('%d + %d = '%(num1,num2)))
#     if answer == solution:
#         print('correct, you are very good')
#         break
#     else:
#         print('wrong answer, try again')
# print('over')

total = 0
number = 1
while number <= 15 :
    if number % 5 == 0:
        number+=1
        continue
    print('%3d'%number,end=' ')
    total += number
    number+=1

print('\ntotal = %d'%total)