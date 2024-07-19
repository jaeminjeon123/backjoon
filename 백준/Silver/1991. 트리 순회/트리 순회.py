def preorder(tree, node):
    if node == '.':
        return ''
    left, right = tree[node]
    return node + preorder(tree, left) + preorder(tree, right)

def inorder(tree, node):
    if node == '.':
        return ''
    left, right = tree[node]
    return inorder(tree, left) + node + inorder(tree, right)

def postorder(tree, node):
    if node == '.':
        return ''
    left, right = tree[node]
    return postorder(tree, left) + postorder(tree, right) + node

n = int(input())
tree = {}
for _ in range(n):
    item, left, right = input().split()
    tree[item]=(left,right) 

print(preorder(tree, 'A'))
print(inorder(tree, 'A'))
print(postorder(tree, 'A'))