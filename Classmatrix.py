#!/usr/bin/python3

class matrix():

    def CreateMatrix(Column, Lines, data):
        matrix = []
        for i in range(Lines):
            rowList = []
            for n in range (Column):
                if (Column * i + n < len(data)):
                    rowList.append(ord(data[Column * i + n]))
                else:
                    rowList.append(0)
            matrix.append(rowList)
        return matrix

    def matrix_multiply(Mat1, Mat2):
        n = len(Mat1); p = len(Mat1[0]);  q = len(Mat2[0])
        result = [[sum([Mat1[i][k]*Mat2[k][j] for k in range(p)]) for j in range(q)] for i in range(n)]
        return result

    def matrix_inversed(Matrix):
        if (len(Matrix) == 2):
            a = Matrix[0][0]
            b = Matrix[0][1]
            c = Matrix[1][0]
            d = Matrix[1][1]
            det = (a * d) - (b * c)
            if (det == 0):
                sys.exit(84)
            print (a)
        if (len(Matrix) == 3):
            a = Matrix[0][0]
            b = Matrix[0][1]
            c = Matrix[0][2]
            d = Matrix[1][0]
            e = Matrix[1][1]
            f = Matrix[1][2]
            g = Matrix[2][0]
            h = Matrix[2][1]
            i = Matrix[2][2]
            det = (a*e*i) + (b*f*g) + (c*d*h) - (c*e*g) - (f*h*a) - (i*b*d)
            print ("mdrlol")
