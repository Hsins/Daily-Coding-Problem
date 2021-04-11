## 題目敘述

Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.

For example, given `[10, 15, 3, 7]` and `k` of `17`, return `true` since `10 + 7` is `17`.

**Bonus**: Can you do this in one pass?

## 題解

### 暴力搜索

一個十分直觀的做法，就是在使用兩層的 `for` 迴圈逐個檢查陣列 `nums` 中兩兩數字之合，是否滿足給定的數字 `target`。

```python
def two_sum(nums: List[int], target: int) -> bool:
    """Nested Iteration (brute force).
        The brute force way to use nested iteration checking for every pair of
        numbers.
        TIME    : O(n^2)
        SPACE   : O(1)
    Args:
        nums (List[int]): list of numbers
        target (int): expected sum of any two numbers
    Returns:
        bool: whether any two numbers from list `nums` add up to `target`.
    """
    for outer_idx, outer_num in enumerate(nums):
        for inner_idx, inner_num in enumerate(nums):
            if outer_idx != inner_idx and outer_num + inner_num == target:
                return True

    return False
```

### 預先排序

在離散幾何領域中，有一個被稱為 **掃描線（Sweep Line）** 的概念可以用來解決許多問題，其精神就是「先排序、再搜索」。許多題目都能夠透過預先排序的概念來簡化題目難度，甚至在許多題目中，必須預先排序才能夠獲得最佳的時間複雜度…

```python
from bisect import bisect_left
from typing import List


def two_sum(nums: List[int], target: int) -> bool:
    """Search After Sorting.

        Sort the original array to make the element in order. Then we can use
        searching to check remaing number added to be the target existed or
        not.

        TIME    : O(nlogn)
        SPACE   : O(1)

    Args:
        nums (List[int]): list of numbers
        target (int): expected sum of any two numbers

    Returns:
        bool: whether any two numbers from list `nums` add up to `target`.
    """
    # sort the original list
    nums.sort()

    # search the list in order
    for cur, num in enumerate(nums):
        add_num = target - num
        idx = binary_search(nums, add_num)

        # Check two more things:
        #   1. the binary search found the target
        #   2. the index should't be as same as current number
        #
        # We need to check lst[i + 1] and lst[i - 1] to see if there's another
        # number that's the same value as lst[i].
        if not idx:
            continue
        elif idx != cur:
            return True
        elif idx + 1 < len(nums) and nums[idx + 1] == add_num:
            return True
        elif idx - 1 >= 0 and nums[idx - 1] == add_num:
            return True

    return False


def binary_search(lst, ele):
    idx = bisect_left(lst, ele)
    if idx != len(lst) and lst[idx] == ele:
        return idx
    return None
```

在排序之後，我們在匹配 `target - num` 時就可以使用二分搜索法，這樣一來便時間複雜度可以從原先暴力搜索的 $\mathcal{O}(n^2)$ 降至 $\mathcal{O}(n\log{n})$。

### 輔助集合

如果寫過 [LeetCode](https://leetcode.com/) 上的題目，可能會發現這題與上面的題目有些差異，主要在於：

- LeetCode 上的題目是要求出兩數的索引位置，而 Daily Coding Problem 則要求判斷是否存在滿足的兩數
- LeetCode 上的題目給定陣列必定能夠找到兩數，而 Daily Coding Problem 則不一定

雖然略有不同，但依然可以使用輔助的雜湊結構來求解，唯一差別是在 LeetCode 上為了存放索引位置所以必須使用字典，而在此處我們只需要使用集合即可（當然，用字典也能求解）。

```python
def two_sum(nums: List[int], target: int) -> bool:
    """Hashing.
        Traverse the numbers and remember the nubmers we've seen. And what we
        should check is if there is another number added to be the target.
        Take [10, 15, 3, 7] for example:
            (1) num = 10, seen_num = ()         , target - num = 7
            (2) num = 15, seen_num = (10)       , target - num = 2
            (3) num = 3 , seen_num = (10, 15)   , target - num = 14
            (4) num = 7 , seen_num = (10, 15, 3), target - num = 10 (Match!)
        TIME    : O(n)
        SPACE   : O(n)
    Args:
        nums (List[int]): list of numbers
        target (int): expected sum of any two numbers
    Returns:
        bool: whether any two numbers from list `nums` add up to `target`.
    """
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False
```

## 參考資料

- [演算法筆記 | Sweep Line](http://web.ntnu.edu.tw/~algo/Point2.html)