def count(arr, m, n ):
    if (n == 0):
        return 1
    if (n < 0):
        return 0
    if (m <=0 and n >= 1):
        return 0
    return count(arr,m - 1,n) + count(arr,m,n-arr[m-1])
a = [1, 2, 3]
print(count(a, len(a), 4))
