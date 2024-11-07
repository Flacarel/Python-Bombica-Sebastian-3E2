class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        raise IndexError("Matrix index out of range")

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Matrix index out of range")

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.data[i][j])
        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication")
        
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.get(k, j)
                result.set(i, j, total)
        return result

    def apply(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])