class X:
    x:int
    y:int

    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.callback = c
        

    def xMethod(self):
        if self.x == self.y:
            print(True)
        else:
            print(False)


class Y:
    def yMethod(self):
        print("this can only be called from an instance of y")

if __name__ == "__main__":
    y: Y = Y()
    x: X = X(1, 2, y.yMethod)
    print(x.callback)
    x.callback()