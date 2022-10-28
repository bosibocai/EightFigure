# 深度优先算法
from Node import *
from math import *
from tool import *


class depth_search:
    def __init__(self, originate, target, max):
        self.originate = originate  # 初始状态
        self.target = target  # 目标状态
        self.num = len(originate.state)  # 数码个数
        self.length = int(sqrt(self.num))  # 每行长度
        self.max = max  # 深度限制
        self.open = [self.originate]  # open表，已经生成但未被扩展，栈，先入后出
        self.closed = []  # close表，已经生成且被扩展
        self.move = [-self.length, self.length, -1, 1]

    # 判断是否有解
    def hasSolve(self):
        originateRev = getReverse(self.originate.state)
        targetRev = getReverse(self.target.state)
        if (originateRev % 2) != (targetRev % 2):
            return 0
        return 1

    def search(self):
        while len(self.open) != 0:
            nowState = self.open[-1]  # 先入后出，尾部为栈顶
            if '0' in nowState.state:
                move = nowState.state.index('0')  # 当前状态中，0数字所在位置
            if nowState.degree >= self.max:  # 如果超出深度限制，跳过
                node = self.open.pop()
                self.closed.append(node)
                continue
            else:
                for i in self.move:
                    # 移动是否合理
                    if (abs(i) == 1 and (floor(move / self.length)) * self.length <= i + move < (floor(move / self.length) + 1) * self.length) or (abs(i) == self.length and 0 <= i + move < self.num):
                        state = copyArray(nowState.state)
                        temp = state[move + i]  # 变化
                        state[move + i] = '0'
                        state[move] = temp
                        nodeState = Node(nowState, state, nowState.degree + 1)  # 变化后状态
                        if state == self.target.state:
                            self.open.append(nodeState)
                            self.open.reverse()
                            return True
                        # 当前孩子节点未在open和closed表中
                        elif (not inTable(nodeState, self.closed)) and (
                                not inTable(nodeState, self.open)):
                            self.open.append(nodeState)
                        else:
                            continue
                self.open.remove(nowState)
                self.closed.append(nowState)
        return False
