'''
import time

# 开始时间
start_1 = time.time()
list1 = [x for x in range(1000000)]
print(list(map(lambda x: x*x, list1)))
stop_1 = time.time()
interval_1 = stop_1 - start_1

start_2 = time.time()
result = []
for x in range(1000000):
    result.append(x**2)
print(result)
stop_2 = time.time()
interval_2 = stop_2 - start_2

start_3 = time.time()
# 优化后
result = [x**2 for x in range(1000000)]
print(result)
stop_3 = time.time()
interval_3 = stop_3 - start_3

print('map耗时', interval_1)
print('append耗时', interval_2)
print('推导式耗时', interval_3)

#  1000次耗时统计
# map耗时 0.019947528839111328
# append耗时 0.02048635482788086
# 推导式耗时 0.01996636390686035

#  100000次耗时统计
# map耗时 0.04386448860168457
# append耗时 0.06184720993041992
# 推导式耗时 0.062021732330322266

#  1000000次耗时统计
# map耗时 0.46984243392944336
# append耗时 0.6598665714263916
# 推导式耗时 0.6201913356781006
'''


# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         a = []
#         for i in range(n):
#             if 2**i ==n:
#                 a.append(i)
#         if 2**(a[0])==n:
#             return True
#         else:
#             return False
