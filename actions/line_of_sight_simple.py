from linear_equation import LinearEquation

class LineOfSightSimple:
    def __init__(self):
        print("INIT line of sight simple")
    def set_equation(self, A, B):
        self.A = A
        self.B = B
        self.equation = LinearEquation(A, B)
    def check_path(self):
        current_block = self.A
        blocks = []
        blocks.append(current_block.copy())
        while current_block != self.B:
            print("current_block : " + str(current_block))
            print("B : " + str(self.B))
            up_result = self.check_up(current_block)
            right_result = self.check_right(current_block)
            if up_result:
                print("up is true\n")
                current_block[0] += 1
                blocks.append(current_block.copy())
            elif right_result:
                print("right is true\n")
                current_block[1] += 1
                blocks.append(current_block.copy())
        print(str(blocks))
        return blocks


    def check_up(self, current_block):
        print("check_up")
        block_to_check = current_block.copy()
        block_to_check[0] += 1
        edge_to_check = current_block[0] + 0.5
        min_bound = current_block[1] - 0.5
        max_bound = current_block[1] + 0.5
        intercept = self.equation.get_x(edge_to_check)
        print("block_to_check : " + str(block_to_check))
        print("edge_to_check : " + str(edge_to_check))
        print("min_bound : " + str(min_bound))
        print("max_bound : " + str(max_bound))
        print("intercept : " + str(intercept))
        print("in range : " + str(intercept > min_bound and intercept < max_bound))
        print("")
        if intercept > min_bound and intercept < max_bound:
            return True
        else:
            return False
    def check_right(self, current_block):
        print("check_right")
        block_to_check = current_block.copy()
        block_to_check[1] += 1
        edge_to_check = current_block[1] + 0.5
        min_bound = current_block[0] - 0.5
        max_bound = current_block[0] + 0.5
        intercept = self.equation.get_y(edge_to_check)
        print("block_to_check : " + str(block_to_check))
        print("edge_to_check : " + str(edge_to_check))
        print("min_bound : " + str(min_bound))
        print("max_bound : " + str(max_bound))
        print("intercept : " + str(intercept))
        print("in range : " + str(intercept > min_bound and intercept < max_bound))
        print("")
        if intercept > min_bound and intercept < max_bound:
            return True
        else:
            return False
