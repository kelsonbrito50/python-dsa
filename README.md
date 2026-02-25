# 🧠 Python DSA — Data Structures & Algorithms

[![Tests](https://github.com/kelsonbrito50/python-dsa/actions/workflows/ci.yml/badge.svg)](https://github.com/kelsonbrito50/python-dsa/actions) ![Algorithms](https://img.shields.io/badge/algorithms-30+-blue) ![Tests](https://img.shields.io/badge/tests-56%20passed-brightgreen)

Interview prep implementations with tests and complexity analysis.

## Implementations

| Category | Algorithm | Complexity | File |
|----------|-----------|------------|------|
| 📦 Arrays | Two Sum (hash map + two-pointer) | O(n) | [`arrays/two_sum.py`](src/arrays/two_sum.py) |
| 📦 Arrays | Sliding Window (max sum, unique substr) | O(n) | [`arrays/sliding_window.py`](src/arrays/sliding_window.py) |
| 📦 Arrays | Kadane's Algorithm (max subarray) | O(n) | [`arrays/kadane.py`](src/arrays/kadane.py) |
| 📦 Arrays | Two Pointers (sorted sum, dedup, palindrome) | O(n) | [`arrays/two_pointers.py`](src/arrays/two_pointers.py) |
| 🔤 Strings | Anagram, Reverse Words, First Unique, LCP | O(n) | [`strings/manipulation.py`](src/strings/manipulation.py) |
| 🔗 Linked Lists | Singly (push, pop, find, reverse) | O(1)/O(n) | [`linked_lists/singly.py`](src/linked_lists/singly.py) |
| 📚 Stacks | Stack + Valid Parentheses | O(1) | [`stacks/stack.py`](src/stacks/stack.py) |
| 📬 Queues | Queue (deque-based) | O(1) | [`queues/queue.py`](src/queues/queue.py) |
| #️⃣ Hash Maps | Custom HashMap (open addressing) | O(1) avg | [`hashmaps/hashmap.py`](src/hashmaps/hashmap.py) |
| 🌳 Trees | BST (insert, search, in-order) | O(log n) | [`trees/bst.py`](src/trees/bst.py) |
| ⛰️ Heaps | Kth Largest, Top K Frequent, Merge K Sorted | O(n log k) | [`heaps/priority_queue.py`](src/heaps/priority_queue.py) |
| 🌐 Graphs | BFS, DFS iterative + recursive | O(V+E) | [`graphs/traversals.py`](src/graphs/traversals.py) |
| 📊 Sorting | Quick Sort (in-place + functional) | O(n log n) | [`sorting/quick_sort.py`](src/sorting/quick_sort.py) |
| 📊 Sorting | Merge Sort (divide & conquer) | O(n log n) | [`sorting/merge_sort.py`](src/sorting/merge_sort.py) |
| 📊 Sorting | Heap Sort (in-place) | O(n log n) | [`sorting/heap_sort.py`](src/sorting/heap_sort.py) |
| 🔍 Searching | Binary Search (iterative + recursive) | O(log n) | [`searching/binary_search.py`](src/searching/binary_search.py) |
| 🧮 Matrix | Rotate 90°, Spiral Order | O(n²) | [`matrix/operations.py`](src/matrix/operations.py) |
| 🔄 Dynamic Programming | Fibonacci (memo + bottom-up), Climbing Stairs | O(n) | [`dynamic_programming/fibonacci.py`](src/dynamic_programming/fibonacci.py) |
| 🔙 Backtracking | Permutations, Subsets (power set) | O(n!/2^n) | [`backtracking/permutations.py`](src/backtracking/permutations.py) |

## Running

```bash
python -m pytest tests/ -v
```

## What I Learned

- **Two pointers** eliminates O(n²) brute force on sorted arrays — always ask "is it sorted?"
- **Sliding window** replaces nested loops for subarray/substring problems
- **Kadane's** is just a clever rolling max — once you see it, you can't unsee it
- **BFS = shortest path** in unweighted graphs, **DFS = explore everything**
- **Dynamic programming** = recursion + memoization — start top-down, optimize bottom-up
- **Backtracking** = DFS on a decision tree — add, recurse, undo
- **Heaps** solve any "top K" problem efficiently — `heapq` in Python is a min-heap
- **Valid parentheses** is the canonical stack problem — learn the pattern, solve 10 variants

## License

MIT
