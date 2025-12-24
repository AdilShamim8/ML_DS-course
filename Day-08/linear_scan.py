def linear_scan(list_data, target):
    index = 0
    length = len(list_data)

    while index < length:
        current_value = list_data[index]
        if current_value == target:
            return True
        index += 1
    return False

print(linear_scan(list(range(1000000)), -5))