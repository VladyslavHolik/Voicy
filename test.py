import Stream as St
   """Module which contains program's behaviour"""

class Test:
    """Class for creating tests"""
    def __init__(self):
        """Creating dictionary for test."""
        self.log = {}

    def assert_equal(self, x, y):
        """Adding assert_equal test to dictionary of tests."""
        self.log[str(x) + " == " + str(y)] = x == y

    def see_results(self):
        """Function for watching results."""
        for key in self.log:
            print(key + " => " + str(self.log[key]))

test = Test()

test.assert_equal(St.chunk, 1024)
test.assert_equal(St.channels, 2)
test.assert_equal(St.rate, 44100)

test.see_results()
