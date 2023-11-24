## 내 솔루션
```python
class Solution(object):
    def twoSum(self, nums, target):
        # t = tail
        t = len(nums) - 1

        while target - nums[t] not in nums[:t]:
            t -= 1
        return [nums.index(target - nums[t]), t]
```

## 리뷰
오랜만에 풀어서 그런지 머리가 안 돌아가서 내가 이전에 했던 풀이를 보고 풀었다. (약간의 수정 사항은 있음: `nums[:t]` 부분으로 `t`가 동일한 인덱스를 가리키는 경우를 제외시킴)
처음에는 투 포인터 알고리즘으로 이해하고 접근했으나 포인터를 하나만 사용해도 충분히 풀 수 있었다. PS를 다시 풀기로 했다. 꾸준히 하는 것을 목표로 하자. 


## 문제 내용
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
> Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
> Input: nums = [3,2,4], target = 6  
Output: [1,2]


Example 3:
> Input: nums = [3,3], target = 6  
Output: [0,1]
 

Constraints:

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.