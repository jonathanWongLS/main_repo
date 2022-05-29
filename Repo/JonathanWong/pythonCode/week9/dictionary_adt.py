from typing import TypeVar, Generic
T = TypeVar('T')

class LinearProbeTable(Generic(T)):

    def __init__(self, size:int = 7919):
        self.count = 0
        self.table = ArrayR(size)

    def __len__(self) -> int:
        return self.count

    def hash(self, key:str) -> int:
        value = 0
        a = 31415
        b = 27183
        for char in word:
            value = (value*3 + ord(char)) % len(self.table) # 101 = tablesize
            a = a * b % (len(self.table)-1)
        return value



if __name__ == "__main__":
    print(hash("Aho",2))
    