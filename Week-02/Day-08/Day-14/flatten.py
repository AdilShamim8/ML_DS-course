def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, [3, 4]]]
print(list(flatten(nested)))  # [1,2,3,4]