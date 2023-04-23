from random import *

z = [*range(116)]
shuffle(z)

while z:
    
    for h in z:
        
        q, c, a = l[h]
        x = len(c)
        print("Q.", q)
        s = c[:]
        shuffle(s)
        for i in range(x):
            print(f"{i + 1}. {s[i]}")
        print()
        i = s.index(a) + 1
        firsttry = True
        
        while True:
            try:
                response = int(input(f"답 (1 ~ {x}) > "))
                if response == i:
                    print("\n정답")
                    break
                firsttry = False
                print("오답\n")
            except ValueError:
                True
        
        if firsttry:
            z.remove(h)
        print(f"맞힌 개수: {116 - len(z)}/116\n")
    
    print(f"아직 {len(z)}개 틀렸음\n이제 틀린 거 다시 풀어보자\n")
