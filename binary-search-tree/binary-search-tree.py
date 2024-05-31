# tree에서 두번째로 큰값
# 
# binary search tree
# 
# node
#     left
#     right
#     value
#      4
#     / \
#     3  5
#   /     \
#  2       6
# /       /
# 1     5.5


import random

class Node:
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return str(self.value)
    
    def __str__(self):
        return str(self.value)

def main():
    test()

def test():
    root = getRandomTree(10)
    answer = solution(root)

def getRandomTree(size = 10):
    s = list(range(size))
    root = Node()
    for _ in range(size):
        index = random.randrange(0, len(s))
        number = s.pop(index)
        node = root
        while True:
            if (node.value == None):
                node.value = number
                break
            elif (node.value <= number):
                if (node.right == None):
                    node.right = Node(number)
                    break
                else:
                    node = node.right
            elif (node.value > number):
                if (node.left == None):
                    node.left = Node(number)
                    break
                else:
                    node = node.left
    return root

def solution(root):
    result = []
    a = dfs_infix(result, root)
    print("infix", result)

    result = []
    b = dfs_prefix(result, root)
    print("prefix", result)

    result = []
    c = dfs_postfix(result, root)
    print("postfix", result)

    return result[-2].value

def dfs_infix(result, node):
    if (node.left != None):
        dfs_infix(result, node.left)
    result.append(node)
    if (node.right != None):
        dfs_infix(result, node.right)
    return result

def dfs_prefix(result, node):
    result.append(node)
    if (node.left != None):
        dfs_prefix(result, node.left)
    if (node.right != None):
        dfs_prefix(result, node.right)
    return result

def dfs_postfix(result, node):
    if (node.left != None):
        dfs_postfix(result, node.left)
    if (node.right != None):
        dfs_postfix(result, node.right)
    result.append(node)
    return result

if __name__ == "__main__":
    main()
