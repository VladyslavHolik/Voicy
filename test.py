import Stream as St

class Test:
    def __init__(self):
        self.log = {}

    def assert_equal(self, x, y):
        self.log[str(x) + " == " + str(y)] = x == y

    def see_results(self):
        for key in self.log:
            print(key + " => " + str(self.log[key]))

test = Test()

test.assert_equal(St.chunk, 1024)
test.assert_equal(St.format, pyaudio.paInt16)
test.assert_equal(St.channels, 2)
test.assert_equal(St.rate, 44100)

test.see_results()
