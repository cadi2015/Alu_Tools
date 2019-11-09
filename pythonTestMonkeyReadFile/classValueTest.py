


class Monkey(object):
    temp = "" #看来temp作为类变量，同样可以用对象call，即self.xxx

    def __init__(self, input):
        self.temp = input
        print self.temp




