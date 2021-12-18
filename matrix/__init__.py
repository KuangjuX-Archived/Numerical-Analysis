import numpy as np


class Matrix:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector
        self.m = len(self.matrix)
        self.n = self.m

    def _swap_matrix_row(self, i: int, j: int):
        temp = self.matrix[i]
        self.matrix[i] = self.matrix[j]
        self.matrix[j] = temp

    def _swap_vector_row(self, i: int, j: int):
        temp = self.vector[i]
        self.vector[i] = self.vector[j]
        self.vector[j] = temp

    def _gaussian_elimination(self):
        for i in range(0, self.m):
            # 从第 0 行 至最后一行进行消元
            max_element = self.matrix[i][i]
            max_pos = i
            for j in range(i + 1, self.m):
                # 从当前行向后寻找最大的主元
                if self.matrix[j][i] > max_element:
                    max_element = self.matrix[j][i]
                    max_pos = j 
            if max_pos != i:
                # 如果最大的列元素不在当前行，则交换当前行与列元素最大所在行
                self._swap_matrix_row(i, max_pos)
                self._swap_vector_row(i, max_pos)
            
            # 交换行之后进行高斯消元
            for k in range(i + 1, self.m):
                # 计算消元系数
                a_k = self.matrix[k][i] / self.matrix[i][i]
                self.matrix[k] -= a_k * self.matrix[i]
                self.vector[k] -= a_k * self.vector[i]
        
        # 消元后进行回代
        res = []
        for i in range(0, self.m):
            index = self.m - i - 1
            x = self.vector[index]
            for j in range(0, i):
                yindex = self.m - j - 1
                x -= res[j] * self.matrix[index][yindex]
            x = x / self.matrix[index][index]
            res.append(x)
        res = list(reversed(res))
        return res

    def gaussian_slove(self):
        return self._gaussian_elimination()

    def slove(self):
        res = np.linalg.solve(self.matrix, self.vector)
        return res



