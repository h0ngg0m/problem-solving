## 내 솔루션 (Beats 91.82%)
```python
class Solution(object):
    def plusOne(s, ds):
        return [int(i) for i in str(int("".join(map(str, ds))) + 1)]
```
배열을 형변환 후 1을 더하고 다시 형변환하는 방식으로 풀었다.

## 다른 사람 솔루션 (Beats ~~99.5%~~ > 66.14%)
```python
class Solution:
    def plusOne(self, digits):
        strings = ""
        for number in digits:
            strings += str(number)

        temp = str(int(strings) +1)

        return [int(temp[i]) for i in range(len(temp))]
```
처음에는 위 풀이를 보고 내 풀이가 더 빠를 것이라 생각했기에 의아했는데, 해당 코드로 다시 테스트를 해보니 66프로 정도가 나왔다. join() 함수를 쓰지 않고 
문자열을 더하는 과정에서 시간이 오래 걸리는 것 같다.


## 문제 내용
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:
> Input: digits = [1,2,3]  
Output: [1,2,4]  
Explanation: The array represents the integer 123.  
Incrementing by one gives 123 + 1 = 124.  
Thus, the result should be [1,2,4].


Example 2:
> Input: digits = [4,3,2,1]  
Output: [4,3,2,2]  
Explanation: The array represents the integer 4321.  
Incrementing by one gives 4321 + 1 = 4322.  
Thus, the result should be [4,3,2,2].  

Example 3:
> Input: digits = [9]  
Output: [1,0]  
Explanation: The array represents the integer 9.  
Incrementing by one gives 9 + 1 = 10.  
Thus, the result should be [1,0].
 

Constraints:
- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's.