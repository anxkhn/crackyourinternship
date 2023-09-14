class MyHashMap:

    def __init__(self):
        self.dict = {}
        

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value

    def get(self, key: int) -> int:
        if key in self.dict:
            return self.dict[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        self.dict[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)