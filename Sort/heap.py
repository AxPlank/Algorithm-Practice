"""
힙 정렬(내림차순)
"""

arr = [5, 11, 14, 3, 1, 9, 4, 6, 7, 2, 12, 10]

# 최소 힙으로 만들기
for i in range(len(arr)):
    d = i
    while d != 0:
        u = (d-1) // 2
        
        if arr[u] > arr[d]:
            arr[u], arr[d] = arr[d], arr[u]
        else:
            break
        d = u

# 힙 정렬 과정 
for i in range(len(arr)-1, -1, -1):
    # 맨 끝값과 첫 번째 값 바꾸기
    arr[0], arr[i] = arr[i], arr[0]
    
    # 위에서부터 시작해 최소 힙으로 만들기
    u = d = 0   
    while d < i:
        d = 2 * u + 1
        if d < i - 1 and arr[d] > arr[d+1]:
            d += 1
            
        if d < i and arr[u] > arr[d]:
            arr[u], arr[d] = arr[d], arr[u]
        else:
            break
            
        u = d

print(arr)