class MyHashMap:

    def __init__(self):
        self.map = []


    def put(self, key: int, value: int) -> None:
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                self.map[i][1] = value
                return

        self.map.append([key, value])


    def get(self, key: int) -> int:
        for k, v in self.map:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
         for i in range(len(self.map)):
            if self.map[i][0] == key:
                self.map.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)