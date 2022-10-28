# 节点类，属性（父节点、棋盘状态、深度、f(n)）
class Node:
    def __init__(self, parent, state, degree):
        self.parent = parent
        self.state = state
        self.degree = degree
