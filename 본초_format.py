from random import *

queue = []
count = 0

while True:
    
    count += 1
    q, c, a = choice(l)
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
        response = int(input(f"답 (1 ~ {x}) > "))
        if response == i:
            print("\n정답")
            break
        firsttry = False
        print("오답\n")
    
    queue.append(1 if firsttry else 0)
    print(f"지난 20개 정답률: {sum(queue[-20:])}/{min(count, 20)}\n")
