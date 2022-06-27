# 1158 요세푸스 

n, k = map(int, input().split())
queue = [i for i in range(1, n+1)] # 원형큐
result = [] # 수행결과 저장 
step = k-1

for i in range(n):
    if len(queue) > step:
        result.append(queue.pop(step)) # pop()은 element 를 return gka 
        step += k-1
    else: # len(queue) <= step 
        step = step % len(queue)
        result.append(queue.pop(step))
        
        step += k-1

print("<",", ".join(str(i) for i in result),">", sep="")
