"""
힙 정렬(내림차순)
"""

arr = [5, 11, 14, 3, 1, 9, 4, 6, 7, 2, 12, 10]

for i in range(len(arr)):
    d = i
    while d != 0:
        u = (d-1) // 2
        
        if arr[u] > arr[d]:
            arr[u], arr[d] = arr[d], arr[u]
        
        d = u
        
for i in range(len(arr)-1, -1, -1):
    arr[0], arr[i] = arr[i], arr[0]
    
    u = d = 0
    while d < i:
        d = 2 * u + 1
        if d < i - 1 and arr[d] > arr[d+1]:
            d += 1
            
        if d < i and arr[u] > arr[d]:
            arr[u], arr[d] = arr[d], arr[u]
            
        u = d

print(arr)