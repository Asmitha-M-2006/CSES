n = int(input())
arr = list(map(int , input().split()))

c = 0 

for i in range(1 , len(arr)):

    if arr[i-1] <= arr[i]:
        pass

    else:
        c += arr[i-1] - arr[i] 
        arr[i] = arr[i-1]
        # print(arr)

print(c)
