# Гена


def flipflop(n):
    if n % 5 == 0 and n % 7 == 0:
        return "FlipFlop"
    if n % 5 == 0:
        return "Flip"
    if n % 7 == 0:
        return "Flop"

    return "%s" % n


class FlippaFloppa:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def test(self, n):
        if n % self.a1 == 0 and n % self.a2 == 0:
            return "FlipFlop"
        if n % self.a1 == 0:
            return "Flip"
        if n % self.a2 == 0:
            return "Flop"

        return "%s" % n


print(__name__)
# ff = FlippaFloppa(a1=3, a2=5)
# arr = [1, 3, 5, 7, 10, 15, 35, 2]
# for n in arr:
#     print("function: %s\nclass: %s" % (flipflop(n), ff.test(n)))
