# 각 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열

pos = [0] * 8 #각 열에서 퀸의 위치를 출력

def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """I열에 퀸을 배치"""
    for j in range(8):
        pos[i] = j
        if i == 7:
            put()
        else:
            set(i + 1) # 다음 열에 퀸을 배치

set(0) # 0 열에 퀸을 배치