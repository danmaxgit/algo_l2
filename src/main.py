

class Node:
    def __init__(self):
        self.exp = 1
        self.value = 0
        self.next = 0
    def __init__(self, exp, value):
        self.exp = exp
        self.value = value
        self.next = 0

class CList:
    def __init__(self, polymon:list):
        if len(polymon) < 1:
            raise Exception("invalide len")
        self.node = Node(0, polymon[0])
        if len(polymon) > 1:
            for i in range(1, len(polymon)):
                t = Node(i, polymon[i])
                j = self.node
                while j.next != 0:
                    j = j.next
                j.next = t
            t.next = self.node
if __name__ == "__main__":
    c = CList([1,2,3])
    a = c.node
    for i in range(6):
        print(a.value)
        a = a.next