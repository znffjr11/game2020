import random 

print("게임을 시작합니다")
##유저 정보 입력하기##
user_dict = []

for i in range (1) :
    user_dict.append({'name': input('이름을 입력하시오:'),  'age':input('나이를 입력하시오:')})



print("유저 정보 : ", user_dict)

block = ["ㄹ", "ㄱ", "ㄴ", "ㅁ", "ㅣ", "ㅜ"]


def game():

    blockList = random.choice(block)
    print("당신의 블록: " + blockList)
    print("1.오른쪽 2.왼쪽 3.블록 바꾸기 0.게임 종료")
    number = int(input("숫자를 입력하세요: "))
    print("당신이 입력한 숫자는",number)
    
    if number == 1:
        print("오른쪽으로 이동")
    if number == 2:
        print("왼쪽으로 이동")
    if number == 3:
        print("블록 바꾸기")
#####반복 종료#######
    
    if number == 0:
        return
        
    game()

game()
