<h1 align="center">Arrays</h1>

## Overview
An array is a linear data structure that stores elements in contiguous memory locations. Each element in an array is identified by an index, allowing direct access to any element based on its position.

## Types:
1. **Static Arrays:** Fixed-size arrays where the length is determined at creation and cannot be changed.
2. **Dynamic Arrays:** Flexible-size arrays (like Python's `list` or C++'s `std::vector`) that automatically allocate more space as elements are added.

## Performance
1. Access: O(1) – Direct access to elements by index allows for constant-time retrieval.
2. Search: O(n) – Linear search is required for unsorted arrays, while binary search in sorted arrays takes O(logn).
3. Insertion: O(n) – Inserting at a specific position may require shifting elements. The exception is inserting at the end of an array, which is O(1), assuming there is still available space in the array.
4. Deletion: O(n) – Deleting an element at a specific position also requires shifting elements to fill the gap.

## Advantages
1. Accessing any element by index takes constant time, O(1), making arrays ideal for situations where fast access is needed.
2. Arrays are straightforward to use, with a predictable memory layout, and are supported in almost every programming language.
3. Contiguously stored elements benefit from cache locality. When a computer accesses an element in memory, it loads not just that element but also surrounding memory into the cache. Contiguous storage means that adjacent elements are likely loaded into the cache together, improving access times when iterating over or accessing nearby elements. This makes operations like loops or traversals faster.

## Disadvantages
1. Static arrays have a fixed size, making them unsuitable for datasets that grow or shrink dynamically.
2. Inserting or deleting an element in the middle requires shifting elements, resulting in an O(n) operation.
3. Dynamic array have some memory overhead (due to extra capacity) and can experience occasional slowdowns during resizing.

## How Dynamic Arrays Work
Dynamic arrays start with a certain capacity and grow by allocating additional contiguous memory when more space is needed. Common examples are Python’s `list` and C++’s `std::vector`.
1. **Growth Factor:** Dynamic arrays typically increase their capacity by a growth factor (often 2) when the current capacity is reached. This exponential growth strategy minimizes the frequency of resizing.
2. **Reallocation:** When a dynamic array reaches its capacity, it allocates a new, larger contiguous memory block and copies all existing elements into this new block. After copying, the old memory is deallocated. This reallocation step involves an O(n) time complexity due to copying, but by doubling the size, dynamic arrays keep the number of reallocations low. This allows most insertions to average O(1) over time, this is known as amortized time.

## Terminology
1. **Contiguous Memory:** Storage of array elements in consecutive memory addresses, allowing for direct access and cache efficiency.
2. **Shifting:** Moving elements to the left or right in response to insertions or deletions in the middle of the array to maintain order.
3. **Cache Locality:** This is the principle that suggests data close to recently accessed data is likely to be accessed soon. This principle is especially relevant in arrays due to their contiguous storage. When data is accessed sequentially— such as iterating through an array— the CPU cache (a small, fast memory storage) can load multiple elements at once, anticipating that nearby elements will be needed next.
	 - **Why Cache Locality Matters:** When the CPU accesses an element that’s not already in the cache (a cache miss), it retrieves that element from main memory. Along with that element, it loads a surrounding chunk of contiguous data into the cache as well. By loading chunks into the cache, the CPU reduces the number of times it has to access the slower main memory. This takes advantage of sequential access patterns to improve performance by maximizing cache usage.