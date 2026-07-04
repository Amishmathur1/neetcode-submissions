class MyHashSet:

    def __init__(self):
        self.pika = set()

    def add(self, key: int) -> None:
        self.pika.add(key)

    def remove(self, key: int) -> None:
        if key in self.pika:
            self.pika.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.pika:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)