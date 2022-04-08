"""
퀵 정렬(오름차순)
"""

arr_input = [3, 1, 9, 10, 14, 1, 6, 4, 5, 2, 7, 8, 12, 0]

def quicksort(arr): # 퀵 정렬을 위한 함수
    def sort(minn, maxx):
        if minn >= maxx: # 최소 단위까지 어레이가 나뉘어졌을 때, 함수 중단.
            return

        pivott = (minn + maxx) // 2 # pivot의 값 설정
        # l, r의 시작지점 설정
        l = minn
        r = maxx
        while r > l:
            # l, r의 변화조건. 조건에 맞다면 값을 변화시킴
            if arr[l] < arr[pivott]: #
                l += 1
            if arr[r] > arr[pivott]:
                r -= 1
                
            # arr[r], arr[l]의 값 교환조건. 조건을 충족한다면 두 값을 교환함
            if arr[r] <= arr[pivott] and arr[l] >= arr[pivott]:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        # 다음 단계 돌입
        sort(minn, l-1)
        sort(l, maxx)
    
    sort(0, len(arr)-1)

quicksort(arr_input)
print(arr_input)