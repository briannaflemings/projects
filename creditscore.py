
ExcellentCredit = 750
GoodCredit = 650
OkayCredit = 550
BadCredit = 500

credit_score = int(input("Enter your credit score:" ))

if credit_score >= ExcellentCredit:
    print ('You have Excellent Credit!')
else:
    if credit_score >= GoodCredit:
        print ('You have Good Credit!')
    else:
        if credit_score >= OkayCredit:
             print ('You have Okay Credit')
        else:
            if credit_score >= BadCredit:
                print ('You have Bad Credit')
6
