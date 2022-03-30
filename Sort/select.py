"""
선택 정렬(오름차순)
"""

arr = [4, 13, 1, 3, 6, 9, 12]

for i in range(len(arr)-1):
    print(f'loop {i+1}')
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    print(arr)