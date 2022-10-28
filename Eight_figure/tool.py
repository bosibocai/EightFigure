# 求逆序数，初始状态和目标状态逆序数奇偶相同有解
def getReverse(state):
    sum = 0
    for i in range(0, len(state)):
        if state[i] == '0':
            continue
        else:
            for j in range(0, i):
                if int(state[j]) > int(state[i]):
                    sum += 1
    return sum


# 浅复制
def copyArray(state):
    copy = []
    return copy + state


# 判断当前节点状态是否在open表或closed表中
def inTable(node, table):
    for i in table:
        if node.state == i.state:
            return i
    return False
