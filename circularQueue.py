class CircleQueue:
    rear = 0 
    front = 0 
    MAX_SIZE = 100
    queue = []

    def __init__(self) -> None:
        self.rear = 0 
        self.front = 0 
        self.queue = [0 for i in range(self.MAX_SIZE)]
    
    # 공백 상태 확인 
    def is_empty(self):
        if self.rear == self.front:
            return True 
        return False
