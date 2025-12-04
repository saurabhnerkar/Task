import time 

def log_executions(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        
        print("time take",end -start)
        return result
    return wrapper  


@log_executions
def calculate_total(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

print(calculate_total(100000000))
    
      