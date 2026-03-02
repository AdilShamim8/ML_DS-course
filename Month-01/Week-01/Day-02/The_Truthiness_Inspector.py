data = []

if data: 
    print("Data Found")
else:
    print("No Data")

test_values = [
    [],           
    [1, 2, 3],    
    "",           
    "Hello",      
    0,            
    42,           
    None,        
    {},           
    {"a": 1},     
]

print("\n Truthiness Table:")
for val in test_values: 
    status = "Truthy" if val else "Falsy"
    print(f"{str(val):15} → {status}")