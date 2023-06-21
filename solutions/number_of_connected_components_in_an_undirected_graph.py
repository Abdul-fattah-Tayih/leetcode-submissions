"""  
    323. Number of Connected Components in an Undirected Graph
    
    Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

    Example 1:
        0          3
        |          |
        1 --- 2    4
    Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

    Example 2:
        0           4
        |           |
        1 --- 2 --- 3
    Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

    Note:
    You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

    https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""

def components_count_in_graph(n, edges):
    """
        Union find solution

        Initially, all nodes are their own parent, which means we have n components

        We iterate over the edges, for each node in the edge we need to find the parent of that node (this is the find part)

        Then we attach the parent of 1 node to the parent of the other node (this is the union part)

        To find the parent of a node:
            we start at the index of the node

            we keep moving to the value of the index we're at until we find an index that is equal to the value (a node that is its own parent)

            and then we return that node

        To union 2 nodes:
            we find the parents of the 2 nodes

            If node 1 has more children (higher rank), then it should be the parent of node 2
            Otherwise node 2 is the parent of node 1

        The total number of components within the graph are the total number of parents we can:
            1. convert the parents into a set to find that number (takes n)
            2. as we do union find, decrement n if a union operation occurs

    """
    
    parents = [i for i in range(n)]
    rank = [1] * n

    def find(node):
        result = node
        while result != parents[result]:
            parents[result] = parents[parents[result]] # path compression
            result = parents[result]

        return result
    
    def union(node1, node2):
        parent1, parent2 = find(node1), find(node2)
        if parent1 == parent2:
            return 0
        
        if rank[parent1] > rank[parent2]:
            parents[parent1] = parent2
            rank[parent2] += rank[parent1]
        else:
            parents[parent2] = parent1
            rank[parent1] += rank[parent2]

        return 1

    result = n
    for parent, child in edges:
        result -= union(parent, child)

    return result

print(components_count_in_graph(10, [[0,2],[2,3],[4,5],[5,6],[7,8],[8,9]]))