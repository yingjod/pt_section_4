vote1 = vote2 = null_vote =0


for i in range(5):
     n=eval(input())
     if n == 1:
         vote1+=1
     elif n == 2:
        vote2+=1
     else:
        null_vote+=1
     print('Total votes of No.1: Nami = %d'% vote1 )
     print('Total votes of No.2: Chopper = %d'%vote2)
     print('Total null votes = %d'%null_vote)

if vote1>vote2:
    print('=> No.1 Nami won the election.')
elif vote1<vote2:
    print('=> No.2 Chopper won the election.')
else:
    print('=> No one won the election')


