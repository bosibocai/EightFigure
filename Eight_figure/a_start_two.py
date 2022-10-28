# A*算法
from Node import *
from math import *
from tool import *


def func(i):
    return i.f

class Astart_search_two:
    def __init__(self, originate, target, max):
        self.originate = originate  # 初始状态
        self.target = target  # 目标状态
        self.num = len(originate.state)  # 数码个数
        self.length = int(sqrt(self.num))  # 每行长度
        self.max = max  # 深度限制
        self.open = [self.originate]  # open表，已经生成但未被扩展
        self.closed = []  # close表，已经生成且被扩展
        self.move = [-self.length, self.length, -1, 1]

    # 判断是否有解
    def hasSolve(self):
        originateRev = getReverse(self.originate.state)
        targetRev = getReverse(self.target.state)
        if (originateRev % 2) != (targetRev % 2):
            return 0
        return 1

    # 数码不在位的距离和
    def h2(self, state):
        count = 0
        for i in range(len(state)):
            j = self.target.state.index(state[i])
            count += abs(floor(i / self.length) - floor(j / self.length))
            count += abs(i % self.length - j % self.length)
        return count

    def search(self):
        self.originate.f = self.originate.degree + self.h2(self.originate.state)
        while len(self.open) != 0:
            nowState = self.open[0]
            if '0' in nowState.state:
                move = nowState.state.index('0')  # 当前状态中，0数字所在位置
            if nowState.degree >= self.max:  # 如果超出深度限制，跳过
                node = self.open.pop(0)
                self.closed.append(node)
                continue
            else:
                for i in self.move:
                    if (abs(i) == 1 and (floor(move / self.length)) * self.length <= i + move < (
                            floor(move / self.length) + 1) * self.length) or (
                            abs(i) == self.length and 0 <= i + move < self.num):
                        state = copyArray(nowState.state)
                        temp = state[move + i]  # 变化
                        state[move + i] = '0'
                        state[move] = temp
                        nodeState = Node(nowState, state, nowState.degree + 1)  # 变化后状态
                        nodeState.f = nodeState.degree + self.h2(nodeState.state)
                        if state == self.target.state:
                            self.open.insert(0, nodeState)  # 找到路径
                            return True
                        else:
                            oldOpen = inTable(nodeState, self.open)
                            oldClose = inTable(nodeState, self.closed)
                            if (not oldClose) and (not oldOpen):
                                self.open.append(nodeState)
                            elif oldClose:  # 已经在closed表中，比较当前估值函数值和表中估值函数值，考虑是否更新
                                if nodeState.f < oldClose.f:
                                    self.closed.remove(oldClose)
                                    self.open.append(nodeState)
                            elif oldOpen:  # 已经在open表中，比较当前估值函数值和表中估值函数值，考虑是否更新
                                if nodeState.f < oldOpen.f:
                                    self.open.remove(oldOpen)
                                    self.open.append(nodeState)
                self.open.pop(0)
                self.open.sort(key=func) # 对open表升序排列
                self.closed.append(nowState)
        return False
