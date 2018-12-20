# -*- coding: utf-8 -*-
"""
@Created  : 2018/12/20 15:05
@Author   : brucefeng10
@Email    : fengxfcn@163.com
@FileName : Floyd_SPP.py
"""


def floyd(adj_matr):
    """Using Floyd–Warshall algorithm to solve the general shortest path problem."""
    length = len(adj_matr)
    # path is a dict saving the way from i to j, either from i directly to j or through i, k, j
    path = {}

    for i in range(length):
        path[i] = {}
        for j in range(length):
            if i == j:
                continue

            path[i][j] = [i, j]
            new_node = None

            for k in range(length):
                if k == j:
                    continue

                new_len = adj_matr[i][k] + adj_matr[k][j]
                if adj_matr[i][j] > new_len:
                    adj_matr[i][j] = new_len
                    new_node = k
            if new_node:
                path[i][j].insert(-1, new_node)

    return path


def get_entire_route(start_node, end_node):
    """Use a recursive function to get the complete route based on the floyd function result."""
    if start_node == end_node:
        print('From node and to node can not be the same.')
        return False
    elif len(path_dict[start_node][end_node]) <= 2:
        return [[start_node, end_node]]
    else:
        return (get_entire_route(path_dict[start_node][end_node][0], path_dict[start_node][end_node][1]) +
                get_entire_route(path_dict[start_node][end_node][1], path_dict[start_node][end_node][2]))



if __name__ == '__main__':
    ini = float('inf')

    # Adjacency Matrix(邻接矩阵、距离矩阵)
    adj_mat = [[0, 1, 12, ini, ini, ini],
                  [ini, 0, 9, 3, ini, ini],
                  [ini, ini, 0, ini, 5, ini],
                  [ini, ini, 4, 0, 13, 15],
                  [ini, ini, ini, ini, 0, 4],
                  [ini, ini, ini, ini, ini, 0]]


    path_dict = floyd(adj_mat)

    start_node, end_node = 0, 5  # the start and end node of the shortest path you want to return
    route = get_entire_route(start_node, end_node)

    shortest_dist = 0  # shortest distance value
    for route0 in route:
        shortest_dist += adj_mat[route0[0]][route0[1]]

    print('Shortest path: ', route)
    print('Shortest distance: ', shortest_dist)




