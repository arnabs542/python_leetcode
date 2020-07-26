from typing import List
import collections


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


# 入度(indegree): 若G为有向图，则把以节点/顶点node为终点的边的数目称为「入度」
def get_indegree(graph: List[DirectedGraphNode]):
    pass


def topological_sorting_bfs(graph: List[DirectedGraphNode]) -> List[DirectedGraphNode]:
    """
    将一个无向图节点数组以拓补排序的方式排序，起点是(没有其他节点指向它的节点)，也就是起点的入度=0，终点的入度>0
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    if not graph:
        return graph
    # step.1 初始化每个节点的入度
    # key: node, value: indegree of node
    indegree_map = dict()
    for node in graph:
        for neighbor in node.neighbors:
            indegree_map[neighbor] = indegree_map.get(neighbor, 0) + 1
    start_nodes = []
    for node in graph:
        if node not in indegree_map:
            indegree_map[node] = 0
            start_nodes.append(node)
    queue = collections.deque(start_nodes)
    topological_order = []
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for neighbor in node.neighbors:
            # 核心部分
            indegree_map[neighbor] -= 1
            if indegree_map[neighbor] == 0:
                queue.append(neighbor)
    return topological_order
