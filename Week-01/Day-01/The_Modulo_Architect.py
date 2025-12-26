X = (int(input("Enter total seconds: ")))
    
hours = X // 3600          
remaining = X % 3600      
minutes = remaining // 60              
seconds = remaining % 60               
    
print(f"{X} seconds = {hours}h {minutes}m {seconds}s")