def merge_sorted(A, B):
    i, j, out = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    out += A[i:]
    out += B[j:]
    return out

print(merge_sorted([1,3,5],[2,4,6]))  # [1,2,3,4,5,6]