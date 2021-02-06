#Петр Зубарев

x = int(input("Введите число для проверки "))

class FlippaFloppa():

    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def test(x,a1,a2):
        if (x % (a1*a2) == 0):
            return "FlipFlop"
        elif (x % a1 == 0):
            return "Flip"
        elif (x % a2 == 0):
            return "Flop"
        else:
            return x
    print(test(x,5,7))
