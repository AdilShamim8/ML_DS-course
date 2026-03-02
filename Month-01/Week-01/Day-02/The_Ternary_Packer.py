score = 85

status = "Pass" if score > 70 else "Fail"

print(f"Score:  {score} → Status: {status}")  


grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"

print(f"Grade: {grade}") 


if score > 70:
    status_traditional = "Pass"
else:
    status_traditional = "Fail"

status_ternary = "Pass" if score > 70 else "Fail"