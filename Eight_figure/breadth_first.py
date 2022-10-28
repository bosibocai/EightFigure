# 宽度优先算法
from Node import *
from math import *
from tool import *


class breadth_search:
    def __init__(self, originate, target, max):
        self.originate = originate  # 初始状态
        self.target = target  # 目标状态
        self.num = len(originate.state)  # 数码个数
        self.length = int(sqrt(self.num))  # 每行长度
        self.max = max  # 深度限制
        self.open = [self.originate]  # open表，已经生成但未被扩展，队列，先入先出
        self.closed = []  # close表，已经生成且被扩展
        self.move = [-self.length, self.length, -1, 1]

    # 判断是否有解
    def hasSolve(self):
        originateRev = getReverse(self.originate.state)
        targetRev = getReverse(self.target.state)
        if (originateRev % 2) != (targetRev % 2):
            return 0
        return 1

    # 实现宽度优先搜索
    def search(self):
        # nodeCount = 1
        while len(self.open) != 0:
            nowState = self.open[-1]  # 先入先出，尾部出队列，头部入队
            if '0' in nowState.state:
                move = nowState.state.index('0')  # 当前状态中，0数字所在位置
            if nowState.degree >= self.max:  # 如果超出深度限制，跳过
                node = self.open.pop()
                self.closed.append(node)
                continue
            else:
                for i in self.move:
                    # 如果移动合理
                    if (abs(i) == 1 and (floor(move / self.length)) * self.length <= i + move < (
                            floor(move / self.length) + 1) * self.length) or (
                            abs(i) == self.length and 0 <= i + move < self.num):
                        state = copyArray(nowState.state)
                        temp = state[move + i]  # 变化
                        state[move + i] = '0'
                        state[move] = temp
                        nodeState = Node(nowState, state, nowState.degree + 1)  # 变化后状态，节点
                        if state == self.target.state:
                            self.open.insert(0, nodeState)  # 找到路径，入队，返回True
                            return True
                        # 当前孩子节点，未存在在open和closed表中
                        elif (not inTable(nodeState, self.closed)) and (not inTable(nodeState, self.open)):
                            self.open.insert(0, nodeState)
                        else:
                            continue
                self.open.pop()
                self.closed.append(nowState)
        return False
