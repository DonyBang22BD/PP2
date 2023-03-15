import time
import math

num = int(input())
duration=int(input())

time.sleep(duration/1000)

sqrt_num = math.sqrt(num)

print(f'Square root of {num} after {duration} milliseconds is {sqrt_num}')