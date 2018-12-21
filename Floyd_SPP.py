# -*- coding: utf-8 -*-
"""
@Created  : 2018/12/20 15:05
@Author   : brucefeng10
@Email    : fengxfcn@163.com
"""

import numpy as np



def floyd(adj_matr):
    """Using Floyd–Warshall algorithm to solve the general shortest path problem."""
    length = adj_matr.shape[0]
    # path is an array saving the transfer point from i to j, -1 if [i, j] or k if [i, k, j]
    path = np.zeros([length, length]) - 1

    for k in range(length):
        for i in range(length):
            for j in range(length):
                if i == j or k == i or k == j:
                    continue

                new_len = adj_matr[i, k] + adj_matr[k, j]
                if adj_matr[i, j] > new_len:
                    adj_matr[i, j] = new_len
                    path[i, j] = k

    return path



def get_entire_route(start_node, end_node):
    """Use a recursive function to get the complete route based on the floyd function result."""
    if start_node == end_node:
        print('From node and to node can not be the same.')
        return False
    elif path_array[start_node, end_node] == -1:  # directly goes from start_node to end_node
        return [[start_node, end_node]]
    else:
        return (get_entire_route(start_node, int(path_array[start_node, end_node])) +
                get_entire_route(int(path_array[start_node, end_node]), end_node))



if __name__ == '__main__':
    ini = float('inf')

    # Adjacency Matrix(邻接矩阵、距离矩阵)
    adj_mat0 = [[90, 1, 12, ini, ini, ini],
                  [ini, 90, 9, 3, ini, ini],
                  [ini, ini, 90, ini, 5, ini],
                  [ini, ini, 4, 90, 13, 15],
                  [ini, ini, ini, ini, 90, 4],
                  [ini, ini, ini, ini, ini, 90]]
    adj_mat1 = [[90, ini, 12, ini, ini, 1],
               [ini, 90, ini, ini, ini, ini],
               [ini, ini, 90, ini, 5, ini],
               [ini, 15, 4, 90, 13, ini],
               [ini, 4, ini, ini, 90, ini],
               [ini, ini, 9, 3, ini, 90]]
    adj_mat = adj_mat0
    adj_array = np.array(adj_mat)

    path_array = floyd(adj_array)

    start_node0, end_node0 = 0, 5  # the start and end node of the shortest path you want to return
    route = get_entire_route(start_node0, end_node0)

    shortest_dist = adj_array[start_node0, end_node0]  # shortest distance value

    print('Shortest path: ', route)
    print('Shortest distance: ', shortest_dist)




