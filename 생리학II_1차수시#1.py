
a=['승발 조달 오억울','소설','체음용양','간오풍']
b=['기혈순환 보조','수액대사 보조','정신활동 기초','소화기능 보조','생식기능 보조','간장혈','장혼 주노']
c=['목','근','조갑','루','협']
d=['담즙분비','담주결단']

e=['심주양기','심오열','오장육부지대주']
f=['심주혈맥','장신 주희']
g=['면','설','한','흉']
h=['수성화물','비별청탁','소장주액']

t=['간의 생리특성','간의 생리기능','간의 기능발현계','담의 생리기능','심의 생리특성','심의 생리기능','심의 기능발현계','소장의 생리기능']
w=[a,b,c,d,e,f,g,h]

for q in range(8):
    print(f'\n###### {t[q]} ######\n')
    while 1:
        W=w[q]
        s=[]
        for i in range(len(W)):
            s.append(input(str(i+1)+' ').strip())
        if set(s)==set(W):
            print('\nㅇㅇㅇㅇㅇ')
            break
        else:
            for _ in range(50):print('ㄴㄴㄴ\n')
            continue
