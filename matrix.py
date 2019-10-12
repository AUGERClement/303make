#!/bin/python3

class matrix:
    def __init__(self, size_x = 13, size_y = 13, data = None, names = None):
        self.size_x = size_x
        self.size_y = size_y
        self.matrix = []
        self.data = data
        self.names = names
        self.init_matrix()

    def init_matrix(self):
        i = 0
        j = 0
        while (i < self.size_x):
            self.matrix.append([])
            while (j < self.size_y):
                self.matrix[i].append(0)
                j += 1
            i += 1
            j = 0

    def fill_list(self):
        for name in self.names :
            for element in self.data :
                if (name in element[0]):
                    self.matrix[self.names.index(name)][self.names.index(element[1])] = 1
                if (name in element[1]):
                    self.matrix[self.names.index(name)][self.names.index(element[0])] = 1

    #Warning. Matrix A's X must be the same than Matrix B's Y
    def multiply_matrix(self, other):
        result = matrix(self.size_x, other.size_y)
        i = 0
        j = 0
        k = 0

        while i < self.size_y:
            while j < other.size_x:
                while k < other.size_y:
                    result.matrix[j][i] += (self.matrix[k][i] * other.matrix[j][k])
                    k += 1
                j += 1
                k = 0
            i += 1
            j = 0
        return result


    #Print formatted for Automatics tests.
    def print_matrix(self):
        for line in self.matrix:
            [print(elem, end=' ') for elem in line[:-1]]
            print(line[-1]) #for newline


    def replace(self, to_add, prox):
        i = 0
        j = 0
        while (i < self.size_x):
            while (j < self.size_y):
                if (to_add.matrix[i][j] >= 1 and self.matrix[i][j] == 0):
                    self.matrix[i][j] = prox
                j = j + 1
            i = i + 1
            j = 0
