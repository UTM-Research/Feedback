def pos_neg(num1, num2):
    sum=0
    if float(num1) < 0 and float(num2) < 0:
        sum = float(num1) + float(num2)
    elif float(num1) > 0 and float(num2) > 0:
        sum = float(num1) + float(num2)
    elif float(num1) < 0 and float(num2) > 0:
        num2=float(num2) *(-1)
        sum = float(num1) + float(num2)
    elif float(num1) > 0 and  float(num2) < 0:
        num1=float(num1) *(-1)
        sum = float(num1) + float(num2)
    return sum
def calc(taggedList):
    flag = 0
    sent=0
    notf=0
    for i in range(0,len(taggedList)-1):

        if (taggedList[i]['POS'] in ('r')) and  (taggedList[i]['word'] in ('no', 'NOT', 'not', 'don', "n't", 'won')):
            notf=1
        if (taggedList[i]['POS'] in ('a')) and  ((taggedList[i+1]['POS'] in ('a')) or (taggedList[i+1]['POS'] in ('n'))):
            num1=float(taggedList[i]['scor'])
            num2=float(taggedList[i+1]['scor'])
            sum= pos_neg(num1, num2)
            if notf==1 :
                sum=sum * (-1)
                sent=float(sent)+float(sum)
                notf=0
                flag=1
            else:
                sent = float(sent) + float(sum)
        else:
            if(flag==1):
                flag=0
                continue
            if notf==1 and  (not (taggedList[i]['word'] in ('no', 'NOT', 'not', 'don', "n't", 'won'))):
                num3 = float(taggedList[i]['scor'])
                num3=num3 * (-1)
                sent=float(sent)+ float(num3)
                notf=0
            else:
                sent = float(sent) + float(taggedList[i]['scor'])

            if(i==len(taggedList)-2):

                if notf==1 and (i==len(taggedList)-2) and ((taggedList[i]['word'] in ('no', 'NOT', 'not', 'don', "n't", 'won'))):
                    num3 = float(taggedList[i + 1]['scor'])
                    num3 = num3 * (-1)
                    sent=float(sent)+ float(num3)
                    notf=0
                else:
                    sent = float(sent) + float(taggedList[i+1]['scor'])
    return sent