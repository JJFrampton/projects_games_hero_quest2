class LinearEquation:
    def __init__(self, A, B):
        print('INIT LinearEquation')
        self.A = A
        self.B = B
        self.m = self.get_m()
        self.b = self.get_b(A[0],A[1])
    def get_m(self):
        self.rise = self.get_rise()
        self.run = self.get_run()
        return self.rise / self.run
    def get_rise(self):
        return self.B[0] - self.A[0]
    def get_run(self):
        return self.B[1] - self.A[1]
    def get_b(self,y,x):
        return y - self.m * x
    def get_y(self,x):
        return self.m * x + self.b
    def get_x(self,y):
        return (y - self.b) / self.m
