<h1 align="center">Binary Search with Duplicates (Iterative)</h1>

## Performance
- **Time Complexity**: O(logn) - It divides the array in half with each iteration until it finds the first or last occurrence of the target value.
- **Space Complexity**: O(1) - Only a constant amount of space is used, as no additional data structures are required.

## How It Works
In binary search with duplicates, even when you adjust the boundaries by middle + 1 or middle - 1 after finding the target value the first time, you’re still dividing the array in half with each iteration. This keeps the time complexity at O(logn).

## Advantages
1. Binary search is very fast for large datasets due to its logarithmic time complexity.
2. Low memory usage.

## Disadvantages
1. Requires a sorted array.