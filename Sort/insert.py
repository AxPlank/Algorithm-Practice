"""
삽입 정렬(오름차순)
"""

arr = [4, 13, 1, 3, 6, 9, 12]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
        else:
            break