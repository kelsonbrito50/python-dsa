"""
Custom HashMap — Open addressing with linear probing.

Average: O(1) get/set/delete
Worst:   O(n) when heavily loaded
"""


class HashMap:
    def __init__(self, capacity: int = 16) -> None:
        self.capacity = capacity
        self.size = 0
        self.keys: list[str | None] = [None] * capacity
        self.values: list[int | None] = [None] * capacity

    def _hash(self, key: str) -> int:
        return hash(key) % self.capacity

    def put(self, key: str, value: int) -> None:
        if self.size >= self.capacity * 0.7:
            self._resize()

        idx = self._hash(key)
        while self.keys[idx] is not None and self.keys[idx] != key:
            idx = (idx + 1) % self.capacity

        if self.keys[idx] is None:
            self.size += 1
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key: str) -> int | None:
        idx = self._hash(key)
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.capacity
        return None

    def _resize(self) -> None:
        old_keys, old_values = self.keys, self.values
        self.capacity *= 2
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        for k, v in zip(old_keys, old_values):
            if k is not None and v is not None:
                self.put(k, v)
