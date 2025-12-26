# import math

# result = 0.1 + 0.2 == 0.3
# print(f"0.1 + 0.2 == 0.3 → {result}")  

# print(f"Actual value: {0.1 + 0.2}")    
# print(f"Expected:      {0.3}")           

# epsilon = 1e-9
# result_fixed = abs((0.1 + 0.2) - 0.3) < epsilon
# print(f"Using epsilon: {result_fixed}")  

# result_isclose = math.isclose(0.1 + 0.2, 0.3)
# print(f"Using isclose: {result_isclose}")  

result_rounded = round(0.1 + 0.2, 10) == round(0.3, 10)
print(f"Using round:    {result_rounded}")