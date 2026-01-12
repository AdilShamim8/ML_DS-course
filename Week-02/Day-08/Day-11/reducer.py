from functools import reduce
from operator import mul

numbers = [1, 2, 3, 4]
product = reduce(mul, numbers)
print(product)  # 24