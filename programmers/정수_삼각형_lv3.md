## 내 솔루션
```python
def solution(t):
    for i in range(1, len(t)):
        for j in range(len(t[i])):
            if j == 0:
                t[i][j] += t[i - 1][j]
            elif j == len(t[i]) - 1:
                t[i][j] += t[i - 1][j - 1]
            else:
                t[i][j] += max(t[i - 1][j], t[i - 1][j - 1])
    
    return max(t[-1])
```
dp 문제다. 정수 삼각형 꼭대기에서 아래로 내려가면서 최대값을 누적해 가면서 값을 구한다.

## 다른 사람 솔루션
```python
def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(0, len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

    return max(dp[-1])
```
나도 처음에는 위 풀이처럼 dp 배열을 따로 선언했는데, 사실 해당 배열 없이 파라미터 triangle로만으로도 해결할 수 있다.

## 문제 내용

### 문제 설명

위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

### 제한사항
- 삼각형의 높이는 1 이상 500 이하입니다.
- 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

### 입출력 예
- triangle: `[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]`	
- result: `30`