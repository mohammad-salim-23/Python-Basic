
a=2
if a>5:
    print('a er value 5 er besi')
    print('KENO besi ke jane')
elif a==2:
    print('ekdom 2 er soman soman')

boss=False
if boss is not True:
    print('lunch er pore asen')
else:
    print('tel er bakso niye asteci')

# nested conditions

coin='head'
if boss==True:
    print('Boss you are a Joss')
    if coin=='tail':
        print('batting')
    else:
        print('bowling')
else:
    if 5>2 and boss!=True:
        print('sob jaygay bossgiri cole na')
    else:
        print('Boss is everything')