"""
칵테일 정렬(오름차순)
"""

arr = [4, 13, 1, 3, 6, 9, 12]

if_swap = True # 정렬 과정 중 변경된 것이 있으면 True, 없으면 False로 두어 반복문을 바로 종료시킴
direction_swap = True # 정렬 방향 결정 시 사용

loop = 1
start = 0 # 첫 루프에서의 시작 인덱스
end = len(arr) - 1 # 첫 루프에서의 마지막 인덱스
while if_swap:
    if_swap = False
    print(f'loop: {loop}')
    if direction_swap:
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                if_swap = True
                
        direction_swap = False
        end -= 1 # end 값을 1 감소시키면서 방향이 바뀔 때, 시작 인덱스를 지정함.
        print(arr)
    else:
        for i in range(end, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                if_swap = True
                
        direction_swap = True
        start += 1 # start 값을 1 증가시키면서 방향이 바뀔 때, 시작 인덱스를 지정함.
        print(arr)
        
    loop += 1