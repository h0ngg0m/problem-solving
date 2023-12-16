from copy import deepcopy


def solution(t):
    dp = deepcopy(t)

    for i in range(1, len(t)):
        for j in range(len(t[i])):
            if j == 0:
                dp[i][j] += dp[i - 1][j]
            elif j == len(t[i]) - 1:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j] + dp[i][j], dp[i - 1][j - 1] + dp[i][j])

    return max(dp[-1])