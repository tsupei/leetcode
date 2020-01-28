# Leetcode
Intend to solve problems in Python3 or C. 

# Solved Problems

`C`:

24. [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs)
53. (*important*) O(n) solution is subtle. Remember it.


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
53. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray)
54. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix)
55. [Jump Game](https://leetcode.com/problems/jump-game)
56. [Merge Intervals](https://leetcode.com/problems/merge-intervals)
57. [Insert Interval](https://leetcode.com/problems/insert-interval)
58. [Length of Last Word](https://leetcode.com/problems/length-of-last-word)
59. [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii)
60. [Permutation Sequence](https://leetcode.com/problems/permutation-sequence)
61. [Rotate List](https://leetcode.com/problems/rotate-list)
62. [Unique Paths ](https://leetcode.com/problems/unique-paths)
63. [Unique Paths II](https://leetcode.com/problems/unique-paths-ii)
64. [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum)

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

54. (*interesting*) 

	- transpose, divide and conquer, resursive
	- directly spiral iteration

55. .= 45
56. merge, extend the upper bound
57. insert and merge(56.)
58. Trival
59. Trival
60. Calculate fatorial
61. Linked List
62. Trival
63. dp?
64. dp?
65.
66. Trival
67. Binary addition
68. Trival but a lot of traps
69. Binary Search
70. Don't use recursive, try combination

=== From now on, only focus on problems whose likes more than dislikes ===

73. Try to use less space: Optimal O(1), but mine is O(m+n)
74. Binary Search in two dimension
75. Trival
76. (not-complete)
77. Recursive, (Is there a better solution?)
78. Recursive (faster than 71.13%)
79. Recursive (faster than 96.68%)
80. Trival
81. (compare to 33) (faster than 33.34%, O(n)) Is there a O(log(n)) solution?
82. Linked List
83. Linked List
84. (*difficult*)(Need to be recoded!) Not A very elegant solution
85. (*difficult*)
86. (*Again*)Partition, (using an buffer to store require space O(n), try not to use?)
88. Replace in place. (faster than 63.xx%)
90. Recursive
92. pick, reverse, and concatenate
93. Calculate all combination First
94. (Trival) What is inorder(LVR) / postorder(LRV) / preorder(VLR) 
95. (faster than 94.83%) Similar to 96. Recursive
96. (Trival) Divide and Conquer
97. (*difficult, important*) dp, manage 2D array
98. (*important*) Validate BST

101. (*slow*) simply recursively compare
102. (faster than 8.18%) simple recursion (faster than  81.35%) loop solution
103. (faster than 97.37%) similar to 102.
104. (faster than 93.69%) simple recursion
105. (faster than 9.18%) divide and conquer, recursion (Find root node)
106. (faster than 8.03%) similar to 105. 
107. (faster than 6.35%) divide and conquer



`Updated on 2019/12/1`
