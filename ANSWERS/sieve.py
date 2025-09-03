import sys

limit = 101
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1

flags = [True] * limit

for num in range(2, limit):  
    if flags[num]:
        print(num, end=' ')  # current num is prime
        for multiple_of_num in range(num, limit, num):
            flags[multiple_of_num] = False
    
    # 2: 4 6 8 10 12
    # 3: 6 9 12 15 18
    # 5: 10 15 20 25
