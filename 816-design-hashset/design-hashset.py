class MyHashSet:

    def __init__(self):
        self.dict={}

    def add(self, key: int) -> None:
        self.dict[key]=True

    def remove(self, key: int) -> None:
        self.dict[key]=False

    def contains(self, key: int) -> bool:
        if key in self.dict:
            return self.dict[key]
        else:
            return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)