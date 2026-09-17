n = int(input())
ans1 = []
ans2 = []
if n == 2 or n == 3:
    print("NO SOLUTION")
else:
    for i in range(1 , n+1):
        if i % 2 == 0:
            ans1.append(i)
        else:
            ans2.append(i)
    ans1.extend(ans2)
    print(* ans1)           

