class BSTNode():

    def __init__(self, val, data, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        self.data = data

    # добавление пары
    def insert(self, val, data):
        if val == self.val:
            self.data = data
        elif val < self.val:
            if self.left is None:
                self.left = BSTNode(val, data)
            else:
                self.left.insert(val, data)
        else:
            if self.right is None:
                self.right = BSTNode(val, data)
            else:
                self.right.insert(val, data)

    # удаляет пару по её ключу
    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    # дает пару по её ключу
    def GetDuo(self, val):
        if val == self.val:
            return self.val, self.data

        if val < self.val:
            if self.left == None:
                return "Такого ключа не существует"
            return self.left.GetDuo(val)

        if self.right == None:
            return "Такого ключа не существует"
        return self.right.GetDuo(val)

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    
    def AllTreeNull(self):
        MaxElement = BSTNode.get_max(self)
        for i in range (0, MaxElement+1):
            BSTNode.delete(self,i)