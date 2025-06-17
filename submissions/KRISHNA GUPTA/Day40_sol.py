n=int(input("n:"))
memo={}
if n <= 1:
    print("Output:", n)
else:
    memo[0]=0
    memo[1]=1
    for i in range(2, n+1):
        memo[i]=memo[i-1]+memo[i-2]
    print("Output:", memo[n])
