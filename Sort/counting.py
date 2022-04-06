"""
카운팅 정렬(오름차순)
"""

arr_input = [5, 11, 14, 3, 10, 2, 3, 13, 12, 7, 6, 9, 8, 2, 14, 3, 1, 9, 4, 6, 7, 2, 12, 10]

def countingsort(arr_input):
    arr_output = [0] * len(arr_input)
    arr_count = [0] * (max(arr_input) + 1)
    
    for i in arr_input:
        arr_count[i] += 1
    
    for i in range(1, len(arr_count)):
        arr_count[i] += arr_count[i-1]
        
    for i in range(len(arr_input)-1, -1, -1):
        arr_output[arr_count[arr_input[i]]-1] = arr_input[i]
        arr_count[arr_input[i]] -= 1
        
    return arr_output