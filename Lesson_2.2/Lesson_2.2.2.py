en = "AaBCcEeHKMOoPpTXxy"
ru = "АаВСсЕеНКМОоРрТХху"
d1, d2, d3 = input(), input(), input()
if d1 in en and d2 in en and d3 in en:
    print('en')
elif d1 in ru and d2 in ru and d3 in ru:
    print('ru')
else:
    print('mix')
