
class HomeCase(object):

    def __init__(self,driver):
        self.driver = driver


    def slideRightToLeft(self):
        self.driver.swipe(1000,500,0,500,500)

    def slideLeftToRight(self):
        self.driver.swipe(0,500,1000,500,500)

    def slideTimes(self,times,slideRightToLeft):
        for item in range(times):
            if slideRightToLeft:
                slideRightToLeft()
            else:
                slideLeftToRight()
    
    def clickBtn(self):
        pass
