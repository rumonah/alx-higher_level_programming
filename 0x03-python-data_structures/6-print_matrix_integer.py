#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for square in range(len(matrix)):
            for shape in range(len(matrix[square])):
                if shape != len(matrix[square]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[square][shape]), end=endspace)
            print()
