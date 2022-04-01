"""
합병 정렬(오름차순)
"""

arr = [5, 11, 14, 3, 1, 9, 4, 6, 7, 2, 12, 10]
print(len(arr))

def mergesort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2 # 분할을 위한 중간지점
    
    left_arr = mergesort(arr[:mid])
    right_arr = mergesort(arr[mid:])
    
    merge_arr = []
    
    l = 0
    r = 0
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] > right_arr[r]:
            merge_arr.append(right_arr[r])
        else:
            merge_arr.append(left_arr[l])
            l += 1
            
    if l == len(left_arr):
        merge_arr += right_arr[r:]
        return merge_arr
    if r == len(right_arr):
        merge_arr += left_arr[l:]
        return merge_arr