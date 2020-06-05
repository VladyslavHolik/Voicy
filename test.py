import Stream as St

class Test:

    """class for creating tests"""
    def __init__(self):
        self.log = {}

    def assert_equal(self, x, y):
        """adding assert_equal test to dictionary of tests"""
        self.log[str(x) + " == " + str(y)] = x == y

    def see_results(self):
        """function for watching results"""
        for key in self.log:
            print(key + " => " + str(self.log[key]))

test = Test()

test.assert_equal(St.chunk, 1024)
test.assert_equal(St.channels, 2)
test.assert_equal(St.rate, 44100)

test.see_results()
