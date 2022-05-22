import random

S=[
['敷和','發生','委和'],
['升明','赫曦','伏明'],
['備化','敦阜','卑監'],
['審平','堅成','從革'],
['靜順','流衍','涸流']]

while 1:
    a=random.randrange(5)
    b=random.randrange(3)
    print(f"{['木','火','土','金','水'][a]}의 {['平氣','太過','不及'][b]}")
    while 1:
        if input()==S[a][b]:
            print('정답')
            break
        else:
            print('ㄴㄴ')
            continue
