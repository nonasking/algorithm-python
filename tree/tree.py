# 트리 선언
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회(pre-order traverse)
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node !== None:
        pre_order(tree[node.left_node])
    if node.right_node !== None:
        pre_order(tree[node.right_node])

# 중위 순회(in-order traverse)
def in_order(node):
    if node.left_node !== None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node !== None:
        in_order(tree[node.right_node])

# 중위 순회(post-order traverse)
def post_order(node):
    if node.left_node !== None:
        post_order(tree[node.left_node])
    if node.right_node !== None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')