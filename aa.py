pay=4
payda=1
top=0
kontrol=0

while True:
    if kontrol%2==1:
        bol=pay/ payda.__neg__()
    else:
        bol=pay/payda
    top=top+bol
    print(top)
    payda=payda+2
    kontrol=kontrol+1