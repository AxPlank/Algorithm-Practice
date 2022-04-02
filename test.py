arr = [5, 9, 4, 3, 1, 9, 4, 6, 7, 2, 12, 10]

start = 0
end = len(arr)
def testt(start, end):
    mid = (start + end) // 2
    print(arr[mid])
    
testt(start, end)