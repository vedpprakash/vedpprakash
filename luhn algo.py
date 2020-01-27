def cal(num):
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+rem
        num=num//10
    return sum
def split(xl):
    return [char for char in xl] 
def validate_credit_card_number(card_number):
    sum=0
    lst=[]
    lst1=[]
    lst2=[]
    templ=[]
    final1=[]
    x=str(card_number)
    re=x[::-1]
    
    lst.append(re[1::2])
    
    xl=str(''.join(lst))
    sp=split(xl)
    
    for i in sp:
        lst1.append((int(i)*2))
    
    for num in lst1:
        if(num>9):
            lst2.append(cal(num))
        else:
            lst2.append(num)
    
    templ.append(re[0::2])
    
    
    wt=str(''.join(templ))
    p=split(wt)
    
    for i in p:
        final1.append((int(i)))
    for num in lst2:
        final1.append(num)
    
    for i in final1:
        sum=sum+i
    if(sum%10==0):
        return True
    else:
        return False
card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")