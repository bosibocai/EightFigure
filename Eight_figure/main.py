# 实现多种算法解决八数码问题

from Node import *
from breadth_first import *
from depth_first import *
from a_start import *
from a_start_two import *
from tool import *
import time


# 输出路径
def printPath(answer):
    end = answer.open[0]
    road = [end]
    while end.parent:
        end = end.parent
        road.append(end)
    road.reverse()
    for i in road:
        for j in range(0, answer.length):
            print(i.state[j*answer.length:(j+1)*answer.length])
        if i != road[-1]:
            print("--->")


if __name__ == '__main__':
    originate = input("请输入初始状态：").split(' ')
    target = input("请输入目标状态：").split(' ')
    max = int(input("请输入深度限制："))
    originateNode = Node(None, originate, 0)
    targetNode = Node(None, target, 0)
    breadth = breadth_search(originateNode, targetNode, max)
    depth = depth_search(originateNode, targetNode, max)
    a_start = Astart_search(originateNode, targetNode, max)
    a_start_two = Astart_search_two(originateNode, targetNode, max)
    # 判断是否有解
    if breadth.hasSolve() == 1:

        # 宽度优先搜索
        print("breadth_first search.")
        start_time = time.perf_counter()
        if breadth.search():
            printPath(breadth)
        else:
            print("NOT FIND")
        end_time = time.perf_counter()
        print("共耗时：", str(end_time-start_time), "S")

        # 深度优先搜索
        print("\n depth_first search.")
        start_time = time.perf_counter()
        if depth.search():
            printPath(depth)
        else:
            print("NOT FIND")
        end_time = time.perf_counter()
        print("共耗时：", str(end_time - start_time), "S")

        # A*算法，h1
        print("\n a_start search.")
        start_time = time.perf_counter()
        if a_start.search():
            printPath(a_start)
        else:
            print("NOT FIND")
        end_time = time.perf_counter()
        print("共耗时：", str(end_time - start_time), "S")

        # A*算法，h2
        print("\n a_start_two search.")
        start_time = time.perf_counter()
        if a_start_two.search():
            printPath(a_start_two)
        else:
            print("NOT FIND")
        end_time = time.perf_counter()
        print("共耗时：", str(end_time - start_time), "S")
    else:
        print("NO PATH")
