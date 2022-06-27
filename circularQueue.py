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
    # 공백 상태를 front == rear로 구분한다. 
    def is_full(self):
        if (self.rerarr+1)%self.MAX_SIZE == self.front:
            return True
        return False

    # 데이터 삽입 
    def enqueue(self, x):
        if self.is_full():
            print("ERROR: FULL")
            return 
        self.rear = (self.rear + 1) % (self.MAX_SIZE)
        self.queue[self.rear] = x
    
    def dequeue(self):
        if self.is_empty():
            print("ERROR: EMPTY")
        self.front = (self.front -1) %(self.MAX_SIZE)
        return self.queue[self.front]

