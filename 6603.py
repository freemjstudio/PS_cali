# 6603 로또

while True:
    data = map(int, input().split())
    if len(data) == 1 and data[0] == 0: # 중단 
        break 
    # 수를 고르는 방법 , 사전순으로 출력하기 

