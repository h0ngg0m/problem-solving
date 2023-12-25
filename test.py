import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    dp = [[0] * 1000000 for _ in range(2)]
    for i in range(2):
        nums = list(map(int, input().split()))
        for j in range(n):
            dp[i][j] = nums[j]
    dp[0][1] = dp[1][0] + dp[0][1]
    dp[1][1] = dp[0][0] + dp[1][1]

    for i in range(2, n):
        dp[0][i] = dp[0][i] + max(dp[0][i - 2], dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = dp[1][i] + max(dp[0][i - 1], dp[0][i - 2], dp[1][i - 2])

    print(max(dp[0][n - 1], dp[1][n - 1]))