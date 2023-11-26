## 내 솔루션 (Beats 21.42% 😇)
```python
class Solution(object):
    def searchInsert(self, ns, t):
        if t in ns:
            return ns.index(t)
        else:
            ns.append(t)
            return sorted(ns).index(t)
```
문제 내용 그대로 풀었다. 배열에 target이 있으면 index를 반환하고, 없으면 배열에 target을 추가한 후 정렬하여 index를 반환했다.

## 다른 사람 솔루션 (Beats 66.21%)
```python
class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l
```
이진 탐색을 사용한 풀이다. 이진 탐색을 사용하면 시간복잡도를 O(log n)으로 줄일 수 있다. 이진 탐색을 생각하긴 했는데, 오랜만이라 구현이 쉽게 떠오르지는 않았다. 잘 기억하자..


## 문제 내용
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:
> Input: nums = [1,3,5,6], target = 5  
> Output: 2  

Example 2:
> Input: nums = [1,3,5,6], target = 2  
> Output: 1

Example 3:
> Input: nums = [1,3,5,6], target = 7  
> Output: 4
 

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4