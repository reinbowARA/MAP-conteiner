from map import BSTNode

bst = BSTNode(0,0)

bst._insert(1, 2)
bst._insert(2, 5)
bst._insert(3 ,10)

print(bst.exists(3))
