
import random

print('\n★★ 한의학원론II 기말고사 대비 퀴즈모음 ★★')

while True:
    
    퀴즈선택 = input('\n1. 15종 약물 ①\n2. 15종 약물 ②\n3. 십제\n4. 내과 진료분야\n5. 구침\n\n1~5를 입력하여 퀴즈를 선택하세요> ')
    
    if 퀴즈선택 == '1':
        
        cease = 'no'
        while cease == 'no':
            
            약물 = ['甘菊', '藁本', '防風', '乾薑', '桂枝', '附子', '梔子', '黃芩', '黃栢', '茯笭', '山藥', '蒼朮', '當歸', '熟地黃', '烏梅']
            
            c = random.randrange(0, 15)
            
            정답 = str(c//3 + 1)
            
            print('\n1.風 2.寒 3.熱 4.濕 5.燥 중 어디에 해당? :', 약물[c])
            
            while True:
                답안 = input('\n답안 입력 (1 ~ 5) : ')
                
                if 답안 == '':
                    continue
                
                elif 답안 == 정답:
                    print('\n정답\n\n뒤로 돌아가려면 X를 입력하세요')
                    break
                    
                elif 답안 == 'X' or 답안 == 'x' or 답안 == 'ㅌ':
                    cease = 'yes'
                    break
                
                else:
                    print('\n오답')
                    continue
        
        continue
    
    elif 퀴즈선택 == '2':
    
        cease = 'no'
        while cease == 'no':
            
            약물 = ['甘菊', '藁本', '防風', '乾薑', '桂枝', '附子', '梔子', '黃芩', '黃栢', '茯笭', '山藥', '蒼朮', '當歸', '熟地黃', '烏梅']

            약성가 = [
            '味甘除熱風 頭眩眼赤收淚功', '氣溫祛風能 兼治寒濕巓頂疼', '甘溫骨節痺 諸風口噤頭暈類',
            '味辛解風寒 炮苦逐冷虛熱安', '小梗行手臂 止汗舒筋手足痺', '辛熱走不留 厥逆回陽宜急投',
            '性寒降小便 吐衄鬱煩胃火煽', '苦寒瀉肺火 子淸大腸濕熱可', '苦寒主降火 濕熱骨蒸下血可',
            '味淡利竅美 白化痰涎赤通水', '甘溫善補中 理脾止瀉益腎功', '甘溫能發汗 除濕寬中瘴可捍',
            '性溫主生血 補心扶虛逐瘀結', '微溫滋腎水 補血烏髭益精髓', '酸溫收斂肺 止渴生津瀉痢退']

            c = random.randrange(0, 15)

            print('\n"' + 약성가[c] + '"의 성질을 가지는 약물을 고르시오.')

            선지 = []

            정답 = 약물[c]
            선지.append(약물[c])
            del 약물[c]

            for i in range(4):
                x = random.randrange(0, 14 - i)
                선지.append(약물[x])
                del 약물[x]

            random.shuffle(선지)
            print('\n선지 :', 선지)

            while True:
                답안 = input('\n답안 입력 (1 ~ 5) : ')
                
                if 답안 == '':
                    continue
                
                elif 답안 == 'X' or 답안 == 'x' or 답안 == 'ㅌ':
                    cease = 'yes'
                    break
                
                elif len(답안) == 1:
                    if 49 <= ord(str(답안)) < 54:
                        if 선지[int(답안) - 1] == 정답:
                            print('\n정답\n\n뒤로 돌아가려면 X를 입력하세요')
                            break
                        
                        else:
                            print('\n오답')
                            continue
                    
                    else:
                        print('\n오답')
                        continue
                
                else:
                    print('\n오답')
                    continue
        
        continue
    
    elif 퀴즈선택 == '3':
        
        cease = 'no'
        while cease == 'no':
            
            정답 = ['宣劑', '通劑', '補劑', '泄劑', '輕劑', '重劑', '澁劑', '滑劑', '燥劑', '濕劑', '寒劑', '熱劑']

            설명 = [
            '막힌 것을 소통시키는 처방, 기혈 운행 막히고 정체되어 흩어지지 않을 때 사용',
            '머물러 있는 것을 뚫어주는 처방, 기혈이나 수액 등이 유통되지 않을 때 소통시켜 운행되게끔 사용',
            '허약한 것을 보충하는 처방, 기혈이 부족하거나 쇠약한 것을 보충할 때 사용',
            '막혀 있는 것을 빠져나가게 하여 소통시키는 처방, 기혈이나 대소변 등이 막혀 있는 것을 빠져나가게 할 때 사용',
            '實한 것을 제거하는 처방, 邪氣가 체표부에 침범한 것을 흩어서 제거할 때 사용',
            '눌러서 진정시키는 처방, 기가 위로 떠오르거나 정신작용이 안정을 유지하니 못할 때 사용',
            '빠져나가는 것을 방지하는 처방, 기혈, 수액, 精 등이 새어나가는 것을 거두어들일 때 사용',
            '부착되어 운행되지 않는 것을 소통시키는 처방, 기혈·수액·대소변 등을 매끄럽게 운행, 빠져나가도록 할 때 사용',
            '지나치게 습윤할 것을 건조하게 하는 처방, 수액대사의 이상으로 체내 수분이 정체, 배설되지 않을 대 사용',
            '메마른 것을 윤택하게 하는 처방, 혈·진액·精 등이 부족하여 신체 내외가 건조할 때 사용',
            '더운 것을 서늘하게 하는 처방, 熱을 제거하고자 할 때 사용',
            '차가운 것을 따뜻하게 하는 처방, 寒을 제거하고자 할 때 사용']

            c = random.randrange(0, 12)

            print('\n"' + 설명[c] + '" 이 설명에 맞는 처방을 한자로 쓰시오.')

            while True:
                답안 = str(input('\n답안 입력 : '))
                
                if 답안 == '':
                    continue
                
                elif 답안 == 정답[c]:
                    print('\n정답\n\n뒤로 돌아가려면 X를 입력하세요')
                    break
                
                elif 답안 == 'X' or 답안 == 'x' or 답안 == 'ㅌ':
                    cease = 'yes'
                    break
                
                else:
                    print('\n오답')
                    continue
        
        continue
    
    elif 퀴즈선택 == '4':
        
        cease = 'no'
        while cease == 'no':
            
            분야 = [
            '黃疸', '脇痛', '積聚', '脹滿', '勞倦傷', '酒傷', '頭痛', '眩暈', '風病',
            '胸痛', '驚悸', '怔忡', '浮腫', '喘證', '血證',
            '胸痺', '腹痛', '癨亂', '嘔吐', '噎膈', '反胃', '便祕', '泄瀉', '痢疾', '吐血', '便血', '積聚', '食鬱', '脹滿', '腸癰',
            '發熱', '喀痰', '喀血', '胸痛', '感冒', '哮喘', '虛勞', '燥病', '痎瘧',
            '遺尿', '尿血', '尿濁', '淋證', '癃閉', '水腫', '關格', '遺精', '陽痿', '消渴', '疝氣']

            c = random.randrange(0, 50)

            if 0 <= c < 9:
                정답 = '1'

            elif 9 <= c < 15:
                정답 = '2'

            elif 15 <= c < 30:
                정답 = '3'

            elif 30 <= c < 39:
                정답 = '4'

            else:
                정답 = '5'

            print('\n1.肝 2.心 3.脾 4.肺 5.腎 중 어디에 해당? :', 분야[c])

            while True:
                답안 = input('\n답안 입력 (1 ~ 5) : ')
                
                if 답안 == '':
                    continue
                
                elif 답안 == 'X' or 답안 == 'x' or 답안 == 'ㅌ':
                    cease = 'yes'
                    break
                
                elif len(답안) == 1:
                    if 49 <= ord(str(답안)) < 54:
                        if 선지[int(답안) - 1] == 정답:
                            print('\n정답\n\n뒤로 돌아가려면 X를 입력하세요')
                            break
                        
                        else:
                            print('\n오답')
                            continue
                    
                    else:
                        print('\n오답')
                        continue
                
                else:
                    print('\n오답')
                    continue
        
        continue
    
    elif 퀴즈선택 == '5':
        
        cease = 'no'
        while cease == 'no':
        
            정답 = ['鑱鍼', '圓鍼', '鍉鍼', '鋒鍼', '鈹鍼', '圓利鍼', '毫鍼', '長鍼', '大鍼']

            설명 = ['열이 머리와 몸에 있을 때', '肌肉에 氣가 충만할 때', '脈氣가 허약하고 부족할 때', '열 제거하고 출혈시키거나 痼疾 빠져나가게 할 때', '癰腫 제거하거나 膿血 빼낼 때', '음양 조절하고 暴痺 제거할 때', '경락의 통증·痺症 치료할 때', '痺症이 뼈 사이나 허리·척추 관절 깊은 곳에 있을 때', '虛風이 뼈·피부 사이에 침범했을 때']

            c = random.randrange(0, 9)

            print('\n"' + 설명[c] + '" 사용하는 침의 종류를 한자로 쓰시오.')

            while True:
                답안 = str(input('\n답안 입력 : '))
                
                if 답안 == '':
                    continue
                
                elif 답안 == 정답[c]:
                    print('\n정답\n\n뒤로 돌아가려면 X를 입력하세요')
                    break
                
                elif 답안 == 'X' or 답안 == 'x' or 답안 == 'ㅌ':
                    cease = 'yes'
                    break
                
                else:
                    print('\n오답')
                    continue
        
        continue
    
    else:
    
        continue
