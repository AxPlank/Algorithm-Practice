arr = [5, 9, 4, 3, 1, 9, 4, 6, 7, 2, 12, 10]

def x():
    def xx():
        arr[0], arr[1] = arr[1], arr[0]
        
    xx()
    arr[0], arr[1] = arr[1], arr[0]
    print(arr)

x()
arr[0], arr[1] = arr[1], arr[0]
print(arr)