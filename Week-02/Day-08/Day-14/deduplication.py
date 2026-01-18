def dedupe(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            out.append(x)
            seen.add(x)
    return out

lst = [1,2,2,3,3,3,4]
print(dedupe(lst))  # [1,2,3,4]