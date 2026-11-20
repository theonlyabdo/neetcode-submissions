class MyHashSet:

    def __init__(self):
        self.myset = [False] * 1000001
        
    def add(self, key: int) -> None:
        self.myset[key] = True

    def remove(self, key: int) -> None:
        self.myset[key] = False

    def contains(self, key: int) -> bool:
        return self.myset[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)