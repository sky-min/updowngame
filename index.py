import random as r

print("숫자 범위를 입력해주세요. ex) 4 ~ 70")
a, b = map(int, input().split('~'))

ran = r.randrange(a, b+1, 1)

print("UP&DOWN 게임 시작!")
num = int(input("숫자를 입력하세요:  "))
if num>ran:
    print("Down")
elif num<ran:
    print("Up")
count = 1

while ( ran != num ):
    num = int(input("숫자를 입력하세요:  "))
    if num>ran:
        print("Down")
    elif num<ran:
        print("Up")
    count +=1
    
print("축하합니다.")
print(count, "번 만에 정답을 맞추셨습니다.")