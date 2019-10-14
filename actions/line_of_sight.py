from linear_equation import LinearEquation

class LineOfSight:
    def __init__(self):
        print('INIT LineOfSight')
        self.array = []
    def set_equation(self, A, B):
        self.A = A
        self.B = B
        self.equation = LinearEquation(A, B)
        self.set_directions()
    def set_directions(self):
        self.directions = []
        # need to catch 0
        if self.equation.rise > 0:
            self.directions.append([.5,0]) # up
        elif self.equation.rise < 0:
            self.directions.append([-.5,0]) # down
        if self.equation.run > 0:
            self.directions.append([0,.5]) # right
        elif self.equation.run < 0:
            self.directions.append([[0,-.5]]) # left
        self.equation.run
    def check_path(self):
        self.current_block = self.A
        while self.current_block != self.B:
            self.current_block = self.check_block()
            # if not self.current_block:
            #     return "failed to find path"
    def check_block(self):
        for direction in self.directions:
            edge = self.get_edge(direction)
            min_bound, max_bound = self.get_boundaries(direction)
            intercept = self.get_intercept(edge, direction)
            # check if in bounds
            if intercept > min_bound and intercept < max_bound:
                print("made it to here")
                self.current_block = self.current_block[
                         self.current_block[0] + direction[0] * 2,
                         self.current_block[1] + direction[1] * 2
                        ]
    def get_edge(self, direction):
        print("this is current block" + str(self.current_block))
        if direction[0] == 0:
            return self.current_block[1] + direction[1]
        else:
            return self.current_block[0] + direction[0]
    def get_boundaries(self, direction):
        i = 0 if direction[0] == 0 else 1
        return [
            self.current_block[i] + .5,
            self.current_block[i] - .5
        ]
    def get_intercept(self, edge, direction):
        i = 0 if direction[0] == 0 else 1
        if i == 0:
        # find y intercept
            return self.equation.get_y(edge)
        else:
            return self.equation.get_x(edge)



    # def get_line_of_sight(self, A, B):
    #     self.array = []
    #     equation = self._get_linear_equation(A,B)
    #     self._traverse(A, A, B, equation)
    #     return self.array

    # def _get_linear_equation(self, A, B):
    #     rise = B[0] - A[0]
    #     run = B[1] - A[1]
    #     b = A[0] - (rise / run) * A[1]
    #     check_dir = []
    #     if rise > 0 :
    #         check_dir.append('up')
    #     else:
    #         check_dir.append('down')
    #     if run > 0 :
    #         check_dir.append('right')
    #     else:
    #         check_dir.append('left')

    #     return {"rise": rise, "run": run, "slope": rise/run, "b": b, "check_dir": check_dir}

    # def _traverse(self, current_block, A, B, equation):
    #     print("this is the current block : ", current_block)
    #     # need to check if current block is in between the two points A and B
    #     # check that x or y are between x and y values for A & B
    #     while current_block != B:
    #         print('in the loop %s %s' %( current_block, B ))
    #         self.array.append(current_block)
    #         result = self._check_adjacent(current_block, A, B, equation)
    #         if result:
    #             self._traverse(result, A, B, equation)

    # def _check_adjacent(self, current_block, A, B, equation):
    #     y = current_block[0]
    #     x = current_block[1]
    #     if 'up' in equation['check_dir']:
    #         if self._intercept_top(x, y, equation):
    #             return [y+1, x]
    #     if 'down' in equation['check_dir']:
    #         if self._intercept_bottom(x, y, equation):
    #             return [y-1, x]
    #     if 'right' in equation['check_dir']:
    #         if self._intercept_right(x, y, equation):
    #             return [y, x+1]
    #     if 'left' in equation['check_dir']:
    #         if self._intercept_left(x, y, equation):
    #             return [y, x-1]
    #     return False

    # def _intercept_top(self, x, y, equation):
    #     edge = y+0.5
    #     low_boundry = x-0.5
    #     high_boundry = x+0.5
    #     intercept = self._get_y_intercept(edge, equation['b'], equation['slope'])
    #     if intercept >= low_boundry and intercept < high_boundry:
    #         return True
    #     else:
    #         return False

    # def _intercept_bottom(self, x, y, equation):
    #     return self._intercept_top(x, y, equation)

    # def _intercept_right(self, x, y, equation):
    #     edge = x+0.5
    #     low_boundry = y-0.5
    #     high_boundry = y+0.5
    #     intercept = self._get_x_intercept(edge, equation['b'], equation['slope'])
    #     if intercept >= low_boundry and intercept < high_boundry:
    #         return True
    #     else:
    #         return False

    # def _intercept_left(self, x, y, equation):
    #     return self._intercept_top(x, y, equation)

    # def _get_y_intercept(self, edge, b, slope):
    #     # returns x value
    #     # (y - b) / m
    #     return (edge - b) / slope

    # def _get_x_intercept(self, edge, b, slope):
    #     # returns y value
    #     # (y - b) / m
    #     return slope * edge + b
