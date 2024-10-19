<h1 align="center">Linear Search</h1>

## Table of Contents
- [Performance](#performance)
- [How It Works](#how-it-works)
- [Advantages](#advantages)
- [Disadvantages](#disadvantages)

## Performance
- **Time Complexity**: O(n) - Scans all elements one by one, so in the worst case it has to scan all `n` elements.
- **Space Complexity**: O(1) - No other data structures are needed for storage.

## How It Works
Iterates through a collection one element at a time until the target value is found.

## Advantages
- Simple to implement.
- Fast for small to medium data sets.
- Data sets don't need to be sorted, this is a big advantage over **binary search** and **interpolation search** (which is a better version of binary search).
- Useful for data structures that don't have *random access* (like linked lists).

## Disadvantages
- Slow for large data sets due to O(n) time complexity.
- For sorted data, other searching algorithms like **binary search** are significantly faster.

## Terminology
- **Random Access** - Ability to access any element in a data structure in constant time, or O(1), given it's index or position. For example, arrays have random access as the elements are stored in *continguous* memory locations. In an array `arr`, you can access the 5th element using `arr[4]` instantly.
- **Contiguous** - Things that are stored in adjacent memory locations, in an unbroken sequence.