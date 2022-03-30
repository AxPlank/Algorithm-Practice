"""
버블 정렬(오름차순)
"""

arr = [4, 13, 1, 3, 6, 9, 12]

for i in range(len(arr)-1):
    print(f'loop {i+1}')
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    print(arr)