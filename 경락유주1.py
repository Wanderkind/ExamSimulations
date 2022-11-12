
# translations from https://mediclassics.kr/books/184/volume/3

import random

L=[
    [
        '肺手太陰之脉',
        '起于中焦',
        '下絡大腸',
        '還循胃口',
        '上膈 屬肺',
        '從肺系',
        '橫出腋下',
        '下循臑內 行少陰心主之前 下肘中',
        '循臂內上骨下廉 入寸口',
        '上魚 循魚際 出大指之端',
        '其支者 從腕後 直出次指內廉 出其端'
    ],
    [
        '大腸手陽明之脉',
        '起于大指次指之端',
        '循指上廉 出合谷兩骨之間 上入兩筋之中',
        '循臂上廉 入肘外廉',
        '上臑外前廉 上肩 出髃骨之前廉',
        '上出于柱骨之會上',
        '下入缺盆',
        '絡肺',
        '下膈 屬大腸',
        '其支者 從缺盆 上頸 貫頰',
        '入下齒中 還出挾口 交人中 左之右 右之左 上挾鼻孔'
    ],
    [
        '胃足陽明之脉',
        '胃足陽明之脈 起於鼻之交頞中 旁納太陽之脈',
        '下循鼻外',
        '入上齒中 還出挾口環唇 下交承漿',
        '却循頤後下廉 出大迎 循頰車',
        '上耳前 過客主人',
        '循髮際 至額顱',
        '其支者 從大迎前 下人迎 循喉嚨 入缺盆',
        '下膈 屬胃 絡脾',
        '其直者 從缺盆 下乳內廉',
        '下挾臍 入氣街中',
        '其支者 起於胃口 下循腹裏 下至氣街中而合',
        '以下髀關 抵伏兎 下膝臏中',
        '下循脛外廉 下足跗',
        '入次趾外間',
        '其支者 下廉三寸而別 下入中指外間',
        '其支者 別跗上 入大趾間 出其端'
    ],
    [
        '脾足太陰之脉',
        '脾足太陰之脈 起於大指之端',
        '循趾內側白肉際 過核骨後 上內踝前廉',
        '上腨內 循脛骨後 交出厥陰之前',
        '上膝 股內前廉',
        '入腹 屬脾 絡胃',
        '上膈',
        '挾咽 連舌本 散舌下',
        '其支者 復從胃 別上膈 注心中'
    ]    
]

T=[
    [
        '수태음폐경맥은',
        '중완에서 시작되어',
        '아래로 내려가 대장에 연락되고',
        '다시 돌아나와 위의 하구, 상구를 쫒아',
        '횡격막을 뚫고 위로 올라가 폐에 속하고',
        '폐계를 쫒아',
        '비스듬히 겨드랑이 아래로 나오고',
        '상박의 내측을 따라 내려가 수소음경과 수궐음경의 전면을 행하여 주관절 가운데로 내려가고',
        '하박의 내측 상골의 아래 가생이를 따라 촌구맥에 들어가고',
        '어수로 올라가 어제를 따라 엄지손가락 끝에서 나온다',
        '그 지맥은 손목 뒤로부터 곧장 둘째 손가락 내측으로 나가 끝에서 나온다'
    ],
    [
        '수양명대장경맥은',
        '엄지손가락에서 두 번째에 해당하는 식지의 끝에서 시작되어',
        '식지의 위쪽을 따라 합곡혈의 양쪽 뼈 사이에서 나오고 위로 올라가 손목 위 양근의 사이(양계혈)로 들어가고',
        '하박의 위쪽을 따라 주관절 외측으로 들어가고',
        '상박의 외측 앞쪽 모서리를 타고 올라가 어깨로 올라가서 우골의 앞쪽 모서리로 나오고',
        '올라가서 대추혈에서 나와',
        '아래로 내려와 결분으로 들어와',
        '폐에 연락하고',
        '횡격막을 뚫고 내려가 대장에 속한다',
        '그 지맥은 결분으로부터 경부로 올라가 협부를 뚫고',
        '아래의 치은으로 들어가고 입을 끼고 돌아나와 인중에서 교차되어 좌맥은 우측으로 가고 우맥은 좌측으로 가며 비공을 끼고 올라간다'
    ],
    [
        '족양명위경맥은',
        '코 옆에서 시작되어 산근으로 가서 교차하여 옆에 있는 태양맥으로 들어가고',
        '코 외측을 따라 내려가',
        '윗니의 치은 속으로 들어가고 돌아나와 입을 끼고 입술을 돌아 아래로 내려와 승장혈에서 교차하고',
        '턱 뒤 아래 모서리를 따라 뒤로 갔다가 돌아나와 대영혈로 나오고 귀 아래의 협겨혈을 쫒아',
        '귀 앞에서 올라가고 객주인을 지나',
        '발제를 따라 액로에 이른다',
        '그 지맥은 대영혈로부터 앞 쪽에서 인영으로 내려가 후롱을 따라 결분에 들어가고',
        '횡격막을 뚫고 내려가 위에 속하고 비에 연락한다',
        '직행하는 경맥은 결분으로부터 젖의 내측으로 내려가고',
        '배꼽을 끼고 내려가 기충혈에서 들어간다',
        '그 지맥은 위의 하구에서 시작되어 뱃속을 따라 내려가 기충혈에 이르러 직행하는 경맥과 합하고',
        '비관으로 내려가 복토에 이르고 슬개골로 들어가',
        '경골의 외측을 따라 내려가 발등에 이르러',
        '가운데 발가락 안쪽으로 들어간다',
        '또 하나의 지맥은 슬하 3촌에서 나뉘어나가 내려가서 가운데 발가락 외측으로 들어간다',
        '또 하나의 지맥은 발등에서 나뉘어져 엄지발가락 사이로 들어가 엄지발가락의 끝에서 나온다'
    ],
    [
        '족태음비경맥은',
        '엄지발가락 끝에서 시작되어',
        '엄지발가락의 내측 백육제를 따라 핵골뒤를 따라 지나고 내과의 앞쪽 모서리로 올라가',
        '장딴지 내측으로 올라가 경골의 뒤를 따라 궐음경의 전면으로 교차하여 나오고',
        '무릎과 넓적다리 내측 앞 모서리를 따라 올라가',
        '배에 들어가 비에 속하고 위에 연락하며',
        '횡격막을 뚫고 올라가',
        '인후를 끼고 설근에 연결되고 설하에 흩어진다',
        '그 지맥은 다시 위로부터 갈라져서 횡격막위로 올라가 심중에 주입된다'
    ]    
]

while 1:
    
    while 1:
        try:
            print('\n1~4 중 입력 >',end=' ')
            n=int(input())
        except KeyboardInterrupt:
            exit()
        except:
            continue
        if 0<n<5:
            break
        else:
            continue
    
    l=L[n-1]
    t=T[n-1]
    k=len(l)
    
    cont=True
    i=0
    while cont and i<k:
        i+=1
        
        while 1:
            print(f'\n{i}/{k} 정답 확인하려면 엔터, 해석 보려면 Y >',end=' ')
            s=input()
            if s=='':
                print(f'\n{l[i-1]}')
                print('\n넘어가려면 엔터, 처음부터 다시 하려면 Y >',end=' ')
                q=input()
                if any(j in q for j in 'Yyㅛ'):
                    cont=False
                break
            
            elif any(j in s for j in 'Yyㅛ'):
                print(f'\n{t[i-1]}')
                continue
            
            else:
                continue
        
        continue
