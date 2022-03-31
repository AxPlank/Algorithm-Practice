"""
버블 정렬(오름차순)
"""

# for 문 이용
arr = [4, 13, 1, 3, 6, 9, 12]

for i in range(len(arr)-1):
    print(f'loop {i+1}')
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    print(arr)
    
# while문 이용
arr = [4, 13, 1, 3, 6, 9, 12]

if_swap = True # 루프 진행 시, arr의 내부에서 위치변경이 한 번이라도 일어났는지 확인할 때 쓰임. 변경이 일어나지 않았다면 정렬이 끝난 것이므로 반복문을 종료함
start = 0 
while if_swap:
    if_swap = False
    
    for i in range(start, len(arr)-start-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            
    start += 1