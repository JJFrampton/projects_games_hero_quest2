class LineOfSight:
    # def check_col(self, A, B):
        # rise = ( B[0] - A[0] ) * - 1 # y coordinate must be inverted later
        # run = B[1] - A[1]
        # slope = rise / run
        # b = y - slope * x
        # return b
    def __init__(self):
        print('INIT')
    def get_b(self, A, B):
        self._invert_y(A)
        self._invert_y(B)
        rise = B[0] - A[0] # y coordinate must be inverted later
        run = B[1] - A[1]
        slope = rise / run
        self.slope = slope
        y, x = B[0], B[1]
        b = y - slope * x

        cols = []
        if A[1] > B[1]:
            for i in reversed(range(A[1], B[1] - 1)):
                print(i)
        else:
            for i in range(A[1], B[1] + 1):
                print(i)
            # print(i + A[1])
            # cols.append()
        # return b
    def _invert_y(self, point):
        point[0] = point[0] * -1
    def _get_y(self, x):
        return self.slope * x + self.b
