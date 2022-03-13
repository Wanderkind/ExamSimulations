
A=['알켄','알코올','에터','아민','싸이올','알데하이드','케톤','카복실산','에스터','아마이드','인산에스터','인산무수물']
B=['이중결합','수산기','에터기','아미노기','설프하이드릴기','카보닐기','카보닐기','카복실기','에스터기','아마이드기','인산에스터기','인산무수물기']

print('\n화합물의 분류를 하나씩 입력하시오\n')

while 1:
    L=[]
    for i in range(12):
        x=input()
        if ' ' in x:
            x=x.replace(' ','')
        L.append(x) 
    if L==A:
        print('\nClear!')
        break
    else:
        print('\n응 틀렸어 첨부터 다시\n')
        continue

print('\n각 화합물의 분류에 대응되는 작용기의 명칭을 입력하시오\n')

while 1:
    L=[]
    for i in range(12):
        x=input(f'{A[i]}: ')
        if ' ' in x:
            x=x.replace(' ','')
        L.append(x)
                
    if L==B:
        for i in range(5000):
            print('\nAll clear!')
        break
    else:
        print('\n응 틀렸어 첨부터 다시\n')
        continue
        continue
