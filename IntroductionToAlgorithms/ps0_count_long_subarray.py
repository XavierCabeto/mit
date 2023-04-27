def count_long_subarray(A):
    n = len(A)
    current = 1
    length = 1
    count = 1
    for i in range(1, n):
        if A[i - 1] < A[i]:
          current = current + 1
        else :
          current = 1
        if current == length:
          count = count + 1
        elif current > length:
          length = current
          count = 1
    return count

A = (1,3,4,2,7,5,6,9,8)
print(count_long_subarray(A))