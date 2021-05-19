from typing import Optional, NamedTuple, Any, List

from linked_list import Node


class Entry(NamedTuple):
    key: str
    value: Any


class HashMap:

    def __init__(self, load_factor: float = 0.75):
        self.bucket_count = 2
        self.count = 0
        self.load_factor = load_factor
        self.buckets: List[Optional[Node]] = [None for _ in range(self.bucket_count)]
        pass

    def put(self, key: str, value: str, inside=False):

        # if not inside:
        #     print("asd")
        current_load_factor = (self.count + 1) / self.bucket_count
        if current_load_factor > self.load_factor:
            # print(f'Need to rehash, current_load_factor: {current_load_factor}')
            # print("Rehashing...")
            self._rehash()
        #
        # print(f"Putting {key}: {value}")
        # print("Current topology")
        # self.print_topology()
        key_hash = hash(key)
        bucket_index = key_hash & (self.bucket_count - 1)
        key_and_value = Entry(key, value)
        if self.buckets[bucket_index] is None:
            self.buckets[bucket_index] = Node(key_and_value)
            self.count += 1
        else:
            new_root, removed_value = self.buckets[bucket_index].remove_by(lambda v: v.key == key)
            self.buckets[bucket_index] = new_root

            if removed_value:
                self.count -= 1
            if self.buckets[bucket_index] is None:
                self.buckets[bucket_index] = Node(key_and_value)
                self.count += 1
            else:
                self.buckets[bucket_index].append(key_and_value)
                self.count += 1

    def get(self, key: str) -> Optional[str]:
        key_hash = hash(key)
        bucket_index = key_hash & (self.bucket_count - 1)
        bucket = self.buckets[bucket_index]
        if bucket is None:
            return None
        entry = bucket.get_by(lambda v: v.key == key)
        if entry is None:
            return None

        return entry.value

    def _rehash(self):
        self.bucket_count *= 2
        # print(f"New bucket count: {self.bucket_count}")
        old_buckets = self.buckets
        self.buckets = [None for _ in range(self.bucket_count)]
        self.count = 0
        bucket: Optional[Node]
        for bucket in old_buckets:
            if bucket is None:
                continue
            bucket.for_each(lambda e: self.put(e.key, e.value, inside=True))

    def print_topology(self):
        bucket: Optional[Node]
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket-{i:03} -> ", end="")
            if bucket is None:
                print("Empty")
                continue
            bucket.for_each(lambda entry: print(f"({entry.key}, {entry.value}) -> ", end=""))
            print()
