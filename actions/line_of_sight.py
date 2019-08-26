# class LineOfSight:
#     # def check_col(self, A, B):
#         # rise = ( B[0] - A[0] ) * - 1 # y coordinate must be inverted later
#         # run = B[1] - A[1]
#         # slope = rise / run
#         # b = y - slope * x
#         # return b
#     def __init__(self):
#         print('INIT')
#     def get_b(self, A, B):
#         self._invert_y(A)
#         self._invert_y(B)
#         rise = B[0] - A[0] # y coordinate must be inverted later
#         run = B[1] - A[1]
#         slope = rise / run
#         self.slope = slope
#         y, x = B[0], B[1]
#         b = y - slope * x

#         cols = []
#         if A[1] > B[1]:
#             for i in reversed(range(A[1], B[1] - 1)):
#                 print(i)
#         else:
#             for i in range(A[1], B[1] + 1):
#                 print(i)
#             # print(i + A[1])
#             # cols.append()
#         # return b
#     def _invert_y(self, point):
#         point[0] = point[0] * -1
#     def _get_y(self, x):
#         return self.slope * x + self.b

class LineOfSight:
    # def check_col(self, A, B):
        # rise = ( B[0] - A[0] ) * - 1 # y coordinate must be inverted later
        # run = B[1] - A[1]
        # slope = rise / run
        # b = y - slope * x
        # return b

    def __init__(self):
        print('INIT')
        self.array = []

    def get_line_of_sight(self, A, B):
        self.array = []
        equation = self._get_linear_equation(A,B)
        self._traverse(A, A, B, equation)
        return self.array

    def _get_linear_equation(self, A, B):
        rise = B[0] - A[0]
        run = B[1] - A[1]
        b = A[0] - (rise / run) * A[1]
        check_dir = []
        if rise > 0 :
            check_dir.append('up')
        else:
            check_dir.append('down')
        if run > 0 :
            check_dir.append('right')
        else:
            check_dir.append('left')

        return {"rise": rise, "run": run, "slope": rise/run, "b": b, "check_dir": check_dir}

    def _traverse(self, current_block, A, B, equation):
        print("this is the current block : ", current_block)
        # need to check if current block is in between the two points A and B
        # check that x or y are between x and y values for A & B
        while current_block != B:
            print('in the loop %s %s' %( current_block, B ))
            self.array.append(current_block)
            result = self._check_adjacent(current_block, A, B, equation)
            if result:
                self._traverse(result, A, B, equation)

    def _check_adjacent(self, current_block, A, B, equation):
        y = current_block[0]
        x = current_block[1]
        if 'up' in equation['check_dir']:
            if self._intercept_top(x, y, equation):
                return [y+1, x]
        if 'down' in equation['check_dir']:
            if self._intercept_bottom(x, y, equation):
                return [y-1, x]
        if 'right' in equation['check_dir']:
            if self._intercept_right(x, y, equation):
                return [y, x+1]
        if 'left' in equation['check_dir']:
            if self._intercept_left(x, y, equation):
                return [y, x-1]
        return False

    def _intercept_top(self, x, y, equation):
        edge = y+0.5
        low_boundry = x-0.5
        high_boundry = x+0.5
        intercept = self._get_y_intercept(edge, equation['b'], equation['slope'])
        if intercept >= low_boundry and intercept < high_boundry:
            return True
        else:
            return False

    def _intercept_bottom(self, x, y, equation):
        return self._intercept_top(x, y, equation)

    def _intercept_right(self, x, y, equation):
        edge = x+0.5
        low_boundry = y-0.5
        high_boundry = y+0.5
        intercept = self._get_x_intercept(edge, equation['b'], equation['slope'])
        if intercept >= low_boundry and intercept < high_boundry:
            return True
        else:
            return False

    def _intercept_left(self, x, y, equation):
        return self._intercept_top(x, y, equation)

    def _get_y_intercept(self, edge, b, slope):
        # returns x value
        # (y - b) / m
        return (edge - b) / slope

    def _get_x_intercept(self, edge, b, slope):
        # returns y value
        # (y - b) / m
        return slope * edge + b
