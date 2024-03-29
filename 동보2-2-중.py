
import random

print('\n☆☆ 외경편 목차 순서 퀴즈 ☆☆\n')

while True:

    L = [
    ['眼爲臟腑之精', '五輪之圖', '八廓之圖', '眼睛屬五臟', '眼有內外唢', '諸脉屬目', '脉法', '目者肝之竅', '眼病無寒', '眼 無火不病', '眼病所因', '內障', '外障', '啬膜', '眼花', '眼疼', '眼昏', '老人眼昏', '不能遠視不能近視', '目不得開合', '眼生፭糞', '視一物爲兩', '讀書損目', '哭泣喪明', '眼病當分表裏虛實', '眼病易治難治辨', '眼中生火', '眼病禁忌', '眼病 調養', '目視凶證', '點眼藥', '洗眼藥', '通治眼病藥', '單方', '鍼灸法'],
    ['耳目受陽氣以聰明', '耳者腎之竅', '脉法', '耳鳴', '耳聾', '耳重聽', '宎耳', '耳痛成膿耳', '耳痒', '透關通氣藥', '修養法', '不治證', '諸蟲入耳', '單方', '鍼灸法'],
    ['鼻曰神廬', '鼻爲玄牝之門戶', '鼻爲肺之竅', '脉法', '鼻淵', '鼻ἳ', '鼻ᤆ', '鼻塞', '鼻痔', '鼻瘡', '鼻痛', '鼻ἵ', '面 鼻紫黑', '鼻涕', '鼻࢛', '鼻色占病', '修養法', '單方', '鍼灸法'],
    ['口曰玉池', '舌屬心', '口脣屬脾', '脉法', '口舌主五味', '口臭', '口糜', '脣腫脣瘡', '繭脣', '舌腫', '重舌', '木舌', ' 舌ᤆ', '舌長舌短', '舌上生胎', '舌生芒刺', '口舌寸數', '失欠脫毭', '自㾘舌頰', '口流涎', '口ࢎ不開', '視脣舌占病', '小兒口舌病', '口舌瘡夘付藥', '口舌瘡外治法', '酒客喉舌生瘡', '諸蟲入口', '補舌斷方', '單方', '鍼灸法'],
    ['齒者骨之餘', '上下熐屬手足陽明', '齒病惡寒惡熱', '牙齒盛衰', '牙齒異名', '脉法', '牙齒痛有七', '牙齒動搖', '塞耳鼻止牙痛 方出牙蟲殺蟲法', '牙齒疳㋾瘡', '齒黃黑', '消齒壅法', '牙齒漸長', '鬪齒', '齒ᤆ', '熂齒', '去痛齒不犯手方', '落齒 重生方', '食酸齒熦齒病塗擦方', '齒病含漱方', '修養固齒法', '齒病禁忌', '視齒色占病', '單方', '鍼灸法'],
    ['咽與喉各異', '咽喉會厭與舌其用不同', '咽喉度數', '脉法', '咽喉之病皆屬火', '咽喉病名', '單乳蛾雙乳蛾喉痺', '急喉痺', '纏喉風', '懸雍垂', '梅核氣', '尸咽', '穀賊', '咽喉痛', '傷寒咽痛', '咽喉瘡', '喉痺失音', '天行喉痺', '咽喉急閉宜鍼', '咽喉急閉宜吐', '咽 喉閉通治', '咽喉不治證', '魚骨溩', '魚骨溩', '獸骨淎', '誤呑諸物', '誤呑諸物', '誤呑諸物', '誤 呑諸蟲', '單方', '鍼灸法'],
    ['頸項寸數', '頸項部位', '項强', '項軟', '風府宜護', '單方', '鍼灸法', '背脊骨節有數', '背有三關', '脉法', '背爲胸府', '背寒', '背熱', '背痛', '脊强', '背㯾㰊', '龜背', '單方', '鍼灸法'],
    ['胸膈之名有義', '胸膈度數', '胸膈部位', '臟腑經脉皆貫膈', '脉法', '心痛與胃脘痛病因不同', '心痛有九種', '心痛亦 有六', '心腹幷痛', '七情作心痛, 食積痰飮瘀血, 皆作胃脘痛', '心胃痛當分虛實', '心胃痛治法', '諸痛不可用補氣 藥', '心胃痛劫藥', '心胃痛宜吐', '心胃痛宜下', '飮食禁忌', '龜胸', '胸ዴ', 'ዴ有寒熱', 'ዴ有虛實', 'ዴ宜吐下', 'ዴ 證治法', '!ዴ氣法', 'ᆩዴ 氣法', '結胸', '!結胸法', 'ᆩ結胸法', '結胸不治證', '單方', '鍼灸法'],
    ['乳間度數', '男女乳腎爲根本', '産後乳汁不行有二', '下乳汁', '産前乳出', '無兒則當消乳', '吹乳妬乳', '乳癰', '乳癰 治法', '結核久成䊜巖', '乳癰年高不治', '䊜頭破裂', '乳懸證', '男女乳疾不同', '單方', '鍼灸法'],
    ['腹圍度數', '腹有大小', '腹痛有部分', '脉法', '腹痛有六', '腹痛有虛實', '積冷腹痛', '腹痛嘔泄', '腹中窄狹', '腹皮麻  痺或痛', '腹中鳴', '涌水證', '腹痛諸證', '腹痛宜通利', '腹痛通治', '腹痛凶證', '單方', '鍼灸法'],
    ['臍居一身之中', '臍下有丹田', '煉臍延壽', '臍宜溫煖', '臍築證', '臍凶證', '小兒臍瘡'],
    ['腰圍度數', '腰爲腎府', '脉法', '腰痛有十', '腎着證', '腰痛通治', '腰痛凶證', '導引法', '單方', '鍼灸法'],
    ['脇腋度數', '脇腋屬肝膽', '脉法', '脇痛有五', '乾脇痛', '脇痛有虛實', '脇痛分左右', '腎邪上薄爲脇痛', '息積證', '肥  氣證', '腋臭', '漏腋', '單方', '鍼灸法']
    ]

    order = [
    [[0, 1, 3, 2, 4], [0, 2, 1, 3, 4], [0, 2, 3, 1, 4], [0, 3, 1, 2, 4], [0, 3, 2, 1, 4]],
    [[0, 1, 2, 4, 3], [0, 1, 4, 2, 3], [0, 2, 1, 4, 3], [0, 2, 4, 1, 3]],
    [[1, 0, 2, 3, 4], [1, 0, 3, 2, 4], [1, 2, 0, 3, 4], [1, 3, 0, 2, 4]]]

    c13 = random.randrange(13)
    cx = random.randrange(len(L[c13]) - 4)

    선지 = []
    정답 = []
    for i in range(5):
        정답.append(L[c13][cx + i])
    선지.append(정답)

    c2a = random.randrange(1, 3)
    for i in range(c2a):
        
        오답 = []
        x = random.randrange(0, 5 - i)
        for j in range(5):
            오답.append(정답[order[0][x][j]])
            
        선지.append(오답)
        del order[0][x]

    c2b = random.randrange(1, 3)
    for i in range(4 - c2a):
        
        오답 = []
        x = random.randrange(0, 4 - i)
        for j in range(5):
            오답.append(정답[order[c2b][x][j]])
        
        선지.append(오답)
        del order[c2b][x]

    random.shuffle(선지)

    for i in range(5):
        print(선지[i])

    while True:
        답안 = input('\n순서가 옳은 것을 고르시오 (1 ~ 5) : ')
        
        if 답안 == '':
            continue
        
        elif len(답안) == 1:
            if 49 <= ord(str(답안)) < 54:
                if 선지[int(답안) - 1] == 정답:
                    print('\n정답\n')
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
