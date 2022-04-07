"""
퀵 정렬(오름차순)
"""

arr_input = [3, 1, 9, 10, 14, 1, 6, 4, 5, 2, 7, 8, 12, 0]

def quicksort(arr):
    def sort(minn, maxx):
        if minn >= maxx:
            return

        pivott = (minn + maxx) // 2
        l = minn
        r = maxx
        while r >= l:
            print(l, r)
            if arr[r] <= arr[pivott] and arr[l] >= arr[pivott]:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
                
            if arr[l] < arr[pivott]:
                l += 1
            if arr[r] > arr[pivott]:
                r -= 1
            print(arr)
            
        sort(minn, l-1)
        sort(l, maxx)
    
    sort(0, len(arr)-1)

quicksort(arr_input)