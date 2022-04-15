class Stackk:
    def __init__(self):
        self.arr = []
    
    """
    데이터 추가
    """
    def pushh(self, data):
        self.arr.append(data)
        
    """
    데이터 제거
    """
    def popp(self):
        if len(self.arr) == 0:
            print("underflow")
            exit()
        else:
            self.arr.pop()
    
    """
    스택 포인터 위치
    """
    def print_pointer(self):
        return len(self.arr)
    
    
    """
    데이터 포함 여부 확인
    """
    def contain(self, data):
        if data in self.arr:
            return True
        else:
            return False
    
    """
    데이터 선택
    """
    def data_peek(self):
        if len(self.arr) == 0:
            print("underflow")
        else:
            return self.arr[-1]
        
    """
    반환 형식 지정
    """
    def __str__(self):
        return str(self.arr[::1])
        
s = Stackk()
s.pushh(3)
print(s)
s.popp()
print(s)
s.popp()