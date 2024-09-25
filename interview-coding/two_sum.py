def two_sum(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return f'Indices are {i} and {j}'
            
            
print(two_sum([3,6,7,34,89],10))

