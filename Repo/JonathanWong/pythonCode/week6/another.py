class C1:
    m = 1
    l = 1
    def __init__(self) -> None:
        self.i = 1
        self.j = 1
        self.k = 1

class C2(C1):
    def __init__(self) -> None:
        C1.__init__(self)
        self.i = 2
        self.j = 2
        self.l = 2
        
class C3(C2):
    def __init__(self) -> None:
        self.i = 3
        C2.__init__(self)
        self.j = 3
        self.m = 3

a = C1()
b = C2()
c = C3()

print(a.i, b.i, c.i)
print(a.j, b.j, c.j)
print(a.k, b.k, c.k)
print(a.l, b.l, c.l)
print(a.m, b.m, c.m)