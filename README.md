# 🧠 Python DSA — Data Structures & Algorithms

[![Tests](https://github.com/kelsonbrito50/python-dsa/actions/workflows/ci.yml/badge.svg)](https://github.com/kelsonbrito50/python-dsa/actions) ![Algorithms](https://img.shields.io/badge/algorithms-20+-blue) ![Tests](https://img.shields.io/badge/tests-40%2B%20passed-brightgreen)

My study notes and implementations while preparing for technical interviews.

## Implementations

| Category | Structure/Algorithm | Complexity | File |
|----------|-------------------|------------|------|
| 📦 Arrays | Two Sum (hash map + two-pointer) | O(n) | [`arrays/two_sum.py`](src/arrays/two_sum.py) |
| 📦 Arrays | Sliding Window (max sum, unique substr) | O(n) | [`arrays/sliding_window.py`](src/arrays/sliding_window.py) |
| 📦 Arrays | Kadane's Algorithm (max subarray) | O(n) | [`arrays/kadane.py`](src/arrays/kadane.py) |
| 🔗 Linked Lists | Singly (push, pop, find, reverse) | O(1)/O(n) | [`linked_lists/singly.py`](src/linked_lists/singly.py) |
| 📚 Stacks | Stack + Valid Parentheses | O(1) | [`stacks/stack.py`](src/stacks/stack.py) |
| 📬 Queues | Queue (deque-based) | O(1) | [`queues/queue.py`](src/queues/queue.py) |
| #️⃣ Hash Maps | Custom HashMap (open addressing) | O(1) avg | [`hashmaps/hashmap.py`](src/hashmaps/hashmap.py) |
| 🌳 Trees | BST (insert, search, in-order) | O(log n) | [`trees/bst.py`](src/trees/bst.py) |
| 🌐 Graphs | BFS, DFS iterative + recursive | O(V+E) | [`graphs/traversals.py`](src/graphs/traversals.py) |
| 📊 Sorting | Quick Sort (in-place + functional) | O(n log n) | [`sorting/quick_sort.py`](src/sorting/quick_sort.py) |
| 📊 Sorting | Merge Sort (divide & conquer) | O(n log n) | [`sorting/merge_sort.py`](src/sorting/merge_sort.py) |
| 📊 Sorting | Heap Sort (in-place) | O(n log n) | [`sorting/heap_sort.py`](src/sorting/heap_sort.py) |
| 🔍 Searching | Binary Search (iterative + recursive) | O(log n) | [`searching/binary_search.py`](src/searching/binary_search.py) |

## Running

```bash
python -m pytest tests/ -v
```

## What I Learned

- **Hash maps** solve most "find pair" problems in O(n) — always consider them first
- **Sliding window** eliminates nested loops for subarray problems
- **Kadane's** is just a clever rolling max — once you see it, you can't unsee it
- **BFS = shortest path** in unweighted graphs, **DFS = explore everything**
- **Quick sort** is faster in practice than merge sort despite same Big O (cache locality)
- **Valid parentheses** is the canonical stack problem — learn the pattern, solve 10 variants

## License

MIT
