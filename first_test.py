# Григорий Зубарев

def FlipFlopFunc(a):
    if(a % 5 != 0 and a % 7 != 0):
        return a
    elif(a % 5 == 0 and a % 7 == 0):
        return "FlipFlop"
    elif(a % 5 == 0):
        return "Flip"
    else:
        return "Flop"
a = int(input('Введите число для проверки функции FlipFlop '))
print(FlipFlopFunc(a))

print("---***---***---")

class FlippaFloppa():
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    # a1 ~ 5     a2 ~ 7
    def test(self, x, a1, a2):
        if (x % a1 != 0 and x % a2 != 0):
            return x
        elif (x % a1 == 0 and x % a2 == 0):
            return "FlipFlop"
        elif (x % a1 == 0):
            return "Flip"
        else:
            return "Flop"

a1 = int(input('Введите а1 '))
a2 = int(input('Введите а2 '))
FlippaFloppaTest = FlippaFloppa(a1= a1,a2= a2)
print(FlippaFloppaTest.test(a, FlippaFloppaTest.a1, FlippaFloppaTest.a2))