<h1 align="center">Binary Search</h1>

## Performance
- **Time Complexity**: O(logn) - Binary search is highly efficient because it eliminates half of the elements from consideration with each iteration.
- **Space Complexity**: O(1) - A constant amount of space is used as it doesn’t require any additional data structures.

## Why log(n)?
1. We start with n elements.
2. We divide the search space by 2 in each iteration. So to get to 1 element in the end, we need x iterations of divisions of 2.
3. Solving for x:
```
n/2^x = 1
n=2^x
x = log2(n)
```
4. Hence the time complexity is log(n) in logarithm base 2.

## How It Works
Binary search works on a sorted array and repeatedly divides the search interval in half.
1. Find the middle element of the current search interval.
2. If the target value matches the middle element, the search is complete.
3. If the target value is less than the middle element, narrows the search to the left half.
4. If the target value is greater than the middle element, narrows the search to the right half.
5. Repeat steps 1-4 until the target is found or the interval is empty.

## Finding The Middle Index
When implementing binary search, it’s important to calculate the middle index of the current search interval correctly. There are two common ways to do this:

1. Option 1: `(left + right) // 2`
2. Option 2: `left + (right - left) // 2`

- Option 1 works well in Python because Python’s int type can handle arbitrarily large numbers. However, in programming languages with fixed-size integers like C++ or Java, the sum of left and right could exceed the maximum integer value, causing **integer overflow**.

- Option 2 avoids this overflow issue by computing the distance between left and right and dividing it by 2 before adding it to left. This approach ensures the value always stays within a safe range:
	- `(right - left)` is always smaller or equal to right.
	- Dividing `(right - left)` by 2 before being added to left ensures mid remains within left & right.

There is a mathematical proof for this but we don't need to know this in detail.

## Advantages
1. Binary search is very fast for large datasets due to its logarithmic time complexity.
2. Low memory usage.

## Disadvantages
1. Requires a sorted array.
2. Requires random access to elements, so it won't work on data structures like linked lists where the elements aren't stored contiguously.

## Terminology
- **Integer Overflow** - When an operation results in a value larger than the maximum that the integer type can store. In languages like C++ or Java, this can cause incorrect behavior or wrap the value around to a negative number.
- **Search Interval** - The range within the array that is currently being considered for the target value. Initially, it spans the entire array, but it shrinks by half with each iteration.
- **Sign Bit**: In signed integers, the most significant bit (leftmost bit) is used to indicate whether the number is positive or negative.
	- 0 indicates the number is positive or zero.
	- 1 indicates the number is negative.
	- The remaining bits represent the magnitude (absolute value). For example, in a 32-bit signed integer, one bit is reserved for the sign, leaving 31 bits for the 	magnitude. This setup results in a range from -2^31 to 2^31 - 1.
	- The reason it’s 2^31 on both the positive and negative sides instead of 2^16 for 32 bit integers is that the sign bit decides whether the values is positive or negative. This maximizes the usage of the available bits.