from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.connections = None
        self.result_dict = None
        self.labels = None
        self.visited_nodes = set()

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.labels = labels
        # Create a dictionary going from a starting node to a list of end nodes.
        self.connections = {node: list() for node in range(n)}
        for start_node, end_node in edges:
            # print(start_node)
            self.connections[start_node].append(end_node)
            self.connections[end_node].append(start_node)

        # Create a dictionary to store the result count
        self.result_dict = {node: None for node in range(n)}

        # Start at 0 node
        self.explore_node(calling_node=0)
        result = [self.result_dict[node] for node in range(n)]
        return result

    def explore_node(self, calling_node):
        self.visited_nodes.add(calling_node)
        descendants = self.connections[calling_node]
        descendants = [descendant for descendant in descendants if descendant not in self.visited_nodes]
        if descendants:
            desc_dicts = list()
            for descendant in descendants:
                desc_dict = self.explore_node(descendant)
                desc_dicts.append(desc_dict)
            this_dict = combine_dicts(desc_dicts)
        else:
            this_dict = defaultdict(int)
        this_dict[self.labels[calling_node]] += 1
        self.result_dict[calling_node] = this_dict[self.labels[calling_node]]
        return this_dict


def combine_dicts(dict_list: List[dict]):
    result_dict = defaultdict(int)
    for this_dict in dict_list:
        for key in this_dict.keys():
            result_dict[key] += this_dict[key]
    return result_dict


for n, edges, labels, ans in (
    (
        7,
        [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
        "abaedcd",
        [2,1,1,1,1,1,1],
    ),
    (
        1,
        [],
        "a",
        [1, ],
    ),
    (
        4,
        [[0, 2], [0, 3], [1, 2]],
        "aeed",
        [1, 1, 2, 1],
    ),
):
    my_answer = Solution().countSubTrees(n, edges, labels)
    print(my_answer, ans)
