<h1 align="center">Searching Algorithms (C++ & Python)</h1>

<p align="center">
	<a href="#"><img alt="C++" src="https://img.shields.io/badge/c++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white"></a>
	<a href="#"><img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a>
</p>

## Description
Highly optimized and performant search algorithms for binary search trees (BST), graphs, and arrays. Each algorithm is implemented in both **C++** and **Python** and is accompanied with clear explanations of the underlying logic and performance-optimizing techniques, along with their applications.

## Table of Contents
- [Arrays](#arrays)
- [Binary Search Tree (BST)](#binary-search-tree-bst)
- [Graphs](#graphs)
- [Additional](#additional)
- [Contributing](#contributing)

## Setting Up
To ensure Python can import modules correctly, add the following line to your shell configuration file (e.g., `.zshrc` or `.bashrc`):

```
export PYTHONPATH="[path_to_this_directory]"
```

This path allows python to know what the top-level directory is (in this case, searching-algorithms) so it can resolve these imports across the codebase.

## Arrays
- [x] Linear Search
- [x] Binary Search (Iterative)
- [x] Binary Search (Recursive)
- [x] Binary Search w/ Duplicates
- [ ] Ternary Search
- [ ] Jump Search (for sorted arrays)
- [ ] Exponential Search (for unbounded arrays)
- [ ] Interpolation Search (for uniformly distributed sorted arrays)
- [ ] Fibonacci Search

## Binary Search Tree (BST)
- [x] Binary Search (Iterative)
- [x] Binary Search (Recursive)
- [x] Inserting a Node (Iterative)
- [x] Inserting a Node (Recursive)
- [x] Deleting a Node (Recursive)
- [x] Find Minimum Node
- [x] Find Maximum Node
- [x] Depth-First Search (DFS):
  - [x] Pre-Order Traversal
  - [x] In-Order Traversal
  - [x] Post-Order Traversal
- [x] Breadth-First Search (BFS)
- [x] Find Successor/Predecessor
- [ ] Balancing BST (e.g., AVL Tree, Red-Black Tree)

## Graphs

### General Graph Algorithms
- [x] Depth-First Search (DFS)
  - [x] Pre-Order Traversal
  - [x] Post-Order Traversal
- [x] Breadth-First Search (BFS)
- [x] Cycle Detection (For Undirected Graphs)
  - [x] Union-Find (Disjoint Set Union)
  - [x] DFS
- [x] Connected Components (For Undirected Graphs w/ DFS)

### Shortest Path Algorithms
#### Unweighted Graphs
- [x] BFS for Shortest Path
- [x] DFS for Shortest Path
#### Weighted Graphs
- [x] Dijkstra's Algorithm (handles non-negative weights)
- [x] Bellman-Ford Algorithm (handles negative weights)
- [ ] Floyd-Warshall Algorithm (all-pairs shortest path)
- [ ] A* Search Algorithm (heuristic-based)

### Directed Graph Algorithms
- [x] Cycle Detection (For Directed Graphs)
  - [x] Directed DFS
  - [x] Topological Sort
- [x] Topological Sort (for Directed Acyclic Graphs)
- [ ] Strongly Connected Components (Kosaraju’s/Tarjan's algorithms)
- [ ] Transitive Closure (Warshall's Algorithm)

### Special Graph Problems (Might Not Do These)
- [x] Minimum Spanning Tree:
  - [x] Prim's Algorithm
  - [x] Kruskal's Algorithm
- [ ] Bipartite Graph Check (using BFS/DFS)
- [ ] Eulerian Path/Circuit
  - [ ] Check for Eulerian Path/Circuit
  - [ ] Find Eulerian Path (Hierholzer’s Algorithm)
- [ ] Hamiltonian Path and Cycle

## Additional
- [ ] Trie Search (prefix-based searching)

## Note
You need to add this project directory to your PYTHONPATH environmental variable for the imports to work correctly.

## Contributing
If you have suggestions to optimize an algorithm, identify any issues, or improve the documentation, please fork the repository and submit a pull request. Alternatively, you can also open an issue to start a discussion about the potential improvement.