<h1 align="center">Priority Queues</h1>

## Overview
A priority queue is an abstract data type that operates like a regular queue except elements are dequeued based on their priority rather than their insertion order. Higher-priority elements are popped before lower-priority ones. If two elements have the same priority, they are typically dequeued in their order of insertion. They are implemented by heaps, sorted arrays, or sorted linked lists under the hood.

## Types of Priority Queues
1. Max-Priority Queue: The element with the highest priority is dequeued first.
2. Min-Priority Queue: The element with the lowest priority is dequeued first.

## Use Cases
1. Task scheduling (e.g., CPU job scheduling) - Tasks with higher priority (e.g., shorter runtime or higher importance) are executed first.
2. Dijkstra’s algorithm for shortest paths - A priority queue is used to repeatedly extract the vertex with the smallest tentative distance, which is a key component of the algorithm to ensure we always are focusing on the shortest path at any point.
3. Event handling in simulations- Simulations (e.g., airport takeoffs or stock market behavior) often involve a sequence of events, each with a timestamp. Priority queues handle these events in chronological order.

## Implementation Techniques

### Binary Heap
A binary heap is a complete binary tree where each node satisfies the heap properties:
1. Max-Heap Property: Parent nodes are greater than or equal to their children.
2. Min-Heap Property: Parent nodes are less than or equal to their children.
3. All levels are fully filled except possibly the last, which is filled from left to right.

#### Time Complexities:
1. Insert: O(logn)
2. Delete max/min: O(log n)
3. Peek (get max/min): O(1)

### Sorted Array/Linked List
Keep elements sorted by priority.

#### Time Complexities:
1. Insert: O(n) (to find the right position to maintain order).
2. Delete max/min: O(1).
3. Peek (get max/min): O(1).

## Advantages
1. Great for prioritizing elements dynamically.
2. Efficient operations (like insert, delete max/min, and peek max/min) for implementations like heaps allow for fast operations on large datasets.

## Disadvantages
1. Maintaining the heap property during insertions or deletions adds computational overhead.

## Is A Heap Considered An Abstract Data Type, What About A Priority Queue?
A heap is not considered an abstract data type (ADT) because it specifies a concrete implementation rather than just the behaviors or operations. While heaps are implemented using arrays (or other structures) under the hood, they describe a specific organization of data (e.g., maintaining the heap property in a complete binary tree). In contrast, an ADT like a priority queue focuses solely on operations such as insertion, deletion, and access, without defining how those operations must be implemented.

## How To Use An In-Built Priority Queue In Python?
The heapq module in Python provides a simple way to implement priority queues using a min-heap. To implement a max-heap, you can negate the priorities.

### Key Functions:
1. heapq.heappush(heap, item) - O(log n)
2. heapq.heappop(heap) - O(log n)
3. heapq.heapify(iterable) - Time Complexity: O(n)

## Terminology
1. **Abstract Data Type (ADT):** An ADT is a theoretical concept in computer science that defines a data structure purely by its behavior (operations and properties), rather than its implementation. Example: Stacks, queues, priority queues, and sets are all ADTs.
2. **Complete Binary Tree:** A binary tree where all levels are fully filled except possibly the last, which is filled from left to right.