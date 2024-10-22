<h1 align="center">Binary Search (Recursive)</h1>

## Performance
- **Time Complexity**: O(logn) - Binary search with recursion remains efficient, as each recursive call reduces the search space by half.
- **Space Complexity**: O(logn) - Unlike the iterative version, the this implementation uses additional space proportional to the depth of the recursion, known as the **call stack**. This is log(n) in the worst case.

## How It Works
Binary search with recursion works on a sorted array and follows a similar pattern as the iterative approach.
1. Find the middle element of the current search interval.
2. If the target value matches the middle element, the search is complete.
3. If the target value is less than the middle element, make a recursive call to search the left half.
4. If the target value is greater than the middle element, make a recursive call to search the right half.
5. The process continues until the target is found or the length of the search interval becomes 1.

## Advantages
1. Recursion simplifies the implementation and can be more intuitive for some people.
2. Similar to the iterative approach, it's highly efficient for large sorted datasets.

## Disadvantages
1. The recursion uses extra space proportional to the call stack depth (O(log n)), which is higher than the iterative version.
2. Like all binary search implementations, it only works on sorted data.
3. For very large datasets, this can lead to very deep recursion levels. Because of this, some languages may run into stack overflow errors if the call stack limit is exceeded.

## Stack Overflow Tendencies in C++ and Python
- In C++, the call stack size is fixed and depends on the system and compiler settings. Recursive calls in binary search (or any other deep recursion) can quickly exceed this fixed size, leading to a stack overflow error.
- In Python, the default call stack limit is typically set to 1000 recursive calls. This limit is set to prevent programs from crashing due to infinite recursion.
- For both these languages, it’s recommended to use an iterative approach to avoid the risk of **stack overflow**.

## Terminology
- **Recursion** - A method of solving a problem where the solution depends on solutions to smaller instances of the same problem.
- **Stack Overflow** - An error that occurs when the call stack exceeds its maximum size.
- **Call Stack** - A limited region of memory used for recursive function calls.