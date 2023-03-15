from map import BSTNode

bst = BSTNode(0,0)

bst.insert(1, 2)
bst.insert(2, 5)
bst.insert(3 ,10)

print(bst.GetDuo(1))
print(bst.GetDuo(2))
print(bst.GetDuo(3))

bst.delete(3); print()

print(bst.GetDuo(1))
print(bst.GetDuo(2))
print(bst.GetDuo(3))

print(bst.get_max())

bst.AllTreeNull()
print(bst.GetDuo(1))