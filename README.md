# Leetcode
Intend to solve problems in Python3 or C. 

# Solved Problems

`C`:

24. [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs)

`Python`:

23. [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)
24. [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs)
25. [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group)
26. [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)
27. [Remove Element](https://leetcode.com/problems/remove-element)
28. [Implement strStr()](https://leetcode.com/problems/implement-strstr)
29. [Divide Two Integers](https://leetcode.com/problems/divide-two-integers)
30. [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words)
31. (*a)[Next Permutation](https://leetcode.com/problems/next-permutation)
32. [Substring with Concatenation of All Words](https://leetcode.com/problems/longest-valid-parentheses)
33. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)
34. [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
35. [Search Insert Position](https://leetcode.com/problems/search-insert-position)
36. [Valid Sudoku](https://leetcode.com/problems/valid-sudoku)
37. [Sudoku Solver](https://leetcode.com/problems/sudoku-solver)
38. [Count and Say](https://leetcode.com/problems/count-and-say)
39. [Combination Sum](https://leetcode.com/problems/combination-sum)
40. [Combination Sum II](https://leetcode.com/problems/combination-sum-ii)
41. [First Missing Positive](https://leetcode.com/problems/first-missing-positive)
42. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)
43. [Multiply Strings](https://leetcode.com/problems/multiply-strings)
44. [Wildcard Matching](https://leetcode.com/problems/wildcard-matching)
45. [Jump Game II](https://leetcode.com/problems/jump-game-ii/)
46. [Permutations](https://leetcode.com/problems/permutations)
47. [Permutations II](https://leetcode.com/problems/permutations-ii)
48. [Rotate Image](https://leetcode.com/problems/rotate-image/)
49. [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
50. [Pow(x, n)](https://leetcode.com/problems/powx-n)
51. [N-Queens](https://leetcode.com/problems/n-queens)
52. [N-Queens II](https://leetcode.com/problems/n-queens-ii)

*a.* The difference between listA.reverse() and listA[::-1] 

# One Line Summary

`from 2019/10/18`

31. iterate from the very last, find the second-minima
32. (*difficult*)DP
33. Two Binary Search(one for seeking pivot point)
34. Binary Search
35. Binary Search, or iterate from the beginning
36. Check Row, Column, Block (Three loops)
37. Recursive
38. Recursive
39. Recursive, determine the same set?
40. Recursive, how to prevent repeated answer
41. (*difficult*) Time Complexity O(n), Space Complexity O(1), use the origin matrix as an index array
42. DP, Time Complexity O(n) ~= 3n
43. Use array representation to do multiplication
44. (*difficult*)DP, 
45. Greedy!
46. Recursive
47. for duplicate input, sort and targeting each unique number only once
```bash
 ^
[1,1,1,1,1,3,4]
           ^
[1,1,1,1,1,3,4]
             ^
[1,1,1,1,1,3,4]

```
48. transpose and reverse
49. sorted string, O = nmlogm, n=len(strs), m=len(str) 
50. (Not recommended) recursive
51. 8 queens, recursive
52. == 51

```python
# How to allocate a 2D array in python
# The following example gives you a 3*3 array
n = 3
arr = [[0 for i in range(n)] for j in range(n)]

# How to copy a 2D array in python
cp_arr = [row[:] for row in arr]

# ps. how to copy a 1D array in python
arr = [0] * n
cp_arr = arr[:]

```

	
`Updated on 2019/10/6`