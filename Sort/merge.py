"""
합병 정렬(오름차순)
"""

arr = [5, 11, 14, 3, 1, 9, 4, 6, 7, 2, 12, 10]

def mergesort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2 # 분할을 위한 중간지점을 가지는 변수
    
    # 어레이 분할 시작
    left_arr = mergesort(arr[:mid])
    right_arr = mergesort(arr[mid:])
    
    # 정렬하면서 합친 어레이를 담을 변수
    merge_arr = []
    
    # 인덱스 변수
    l = 0
    r = 0
    # 정렬 반복문. 두 요소를 비교하여 더 작은 값을 저장하고, 더 작은 값을 저장하고 있던 어레이의 인덱스를 1 증가시킴.
    # 만약 두 값이 같다면 right_arr의 값을 저장하고 해당 어레이의 인덱스 1 증가
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] > right_arr[r]:
            merge_arr.append(right_arr[r])
            r += 1
        else:
            merge_arr.append(left_arr[l])
            l += 1
            
    # 만약 한쪽의 인덱스 변수가 해당 변수가 가리키고 있는 어레이의 길이와 크기가 같다는 것은 다음을 의미함
    # 1. 다른 어레이에 값이 남아 있음
    # 2. 남아있는 모든 원소는 merge_arr에 저장되어 있는 최댓값보다 크다.
    # 그렇기 때문에 남아있는 값들을 슬리이싱을 이용해 잘라내고, merge_arr 뒷부분에 붙임
    if l == len(left_arr):
        merge_arr += right_arr[r:]
        return merge_arr
    if r == len(right_arr):
        merge_arr += left_arr[l:]
        return merge_arr
    
print(mergesort(arr))