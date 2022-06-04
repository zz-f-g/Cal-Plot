#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Zizhan Guo'

from scipy.io import savemat

class Least_square_data:
    def __init__(self, m: int, n: int) -> None:
        '''init a data instance with:
        m: quantity of data
        n: dimension of the solution
        '''
        self._m = m
        self._n = n
        self._B = [0] * m
        self._A = [[0] * n] * m
    def get_a_data(self, data_str: str) -> tuple:
        '''read data from string in file in certain format
        '''
        A = [0] * self._n
        i, j = 0, 0
        while (data_str[i] != ' '):
            i += 1
        j = i
        b = float(data_str[0:i])
        for k in range(self._n):
            while (data_str[i] != ':'):
                i += 1
            j = i
            i += 1
            while (data_str[j] != ' '):
                j += 1
            A[k] = float(data_str[i:j])
        return (b, A)
    def get_data(self, data_list: list) -> None:
        '''get data from file
        data_str: file read
        '''
        for i in range(self._m):
            self._B[i], self._A[i] = self.get_a_data(data_list[i])
    def print_data(self) -> None:
        '''print data A & B
        '''
        print("---------- A ----------")
        for i in range(self._m):
            print(self._A[i])
        print("---------- B ----------")
        print(self._B)
    def savemat_data(self) -> None:
        savemat('bodyfat_scale.mat', {'A': self._A, 'B': self._B})

def main():
    with open(r'.\bodyfat_scale.txt', 'r', encoding='utf-8') as data:
        data_str = data.readlines()
    data = Least_square_data(len(data_str), 14)
    data.get_data(data_str)
    data.savemat_data()
    # data.print_data()
    return

if __name__ == '__main__':
    main()
