

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
    def copy(self):
        res = [self.node.value]
        a = self.node.next
        while(a != self.node):
            res.append(a.value)
            a = a.next
            #print(res)
        return CList(res)
    def remove_by_exp(self, exp):
        node = self.node.next
        prev = self.node
        flag = false
        while (node != self.node):
            if (node.exp == exp):
                flag = true
                break
            prev = node
            node = node.next
        if(flag == True):
            prev.next = node.next
            if node == self.node:
                self.node = node.next
        return flag
    def remove_by_value(self, exp):
        node = self.node.next
        prev = self.node
        flag = False
        while (node != self.node):
            if (node.value == value):
                flag = True
                break
            prev = node
            node = node.next
        if(flag == True):
            prev.next = node.next
            if node == self.node:
                self.node = node.next 
    def add(self, value, exp):
        node = Node(exp, value)
        t = self.node.next
        self.node.next = node
        node.next = t 
    def __str__(self):
        i = self.node.next
        res = ""#f"{i.value}"
        while(i != self.node):
            if(i.exp > 1):
                res += f"{i.value} * x ˆ {i.exp} + "
            if(i.exp == 1):
                res += f"{i.value} * x + "
            i = i.next
        res += f"{i.value}"
        return res

def derivative(polynom):
    res = polynom.copy()
    res.remove_by_exp(0)
    i = res.node.next
    prev = res.node
    while(i != res.node):
        if(i.exp > 0):
            i.value = i.exp * i.value
            i.exp = i.exp - 1
        prev = i
        i = i.next
    return res    

if __name__ == "__main__":
    c = CList([1,2,3])
    print(c)
    res = derivative(c)
    print(res)