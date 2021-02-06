#
# Множественное наследование
#

# разные названия методов
class Sitter:
    def sit(self):
        print("sit")


class Layer:
    def lay(self):
        print("lay")


class SitterLayer(Sitter, Layer):
    pass


# a = SitterLayer()
# a.sit()
# a.lay()

# Одинаковые названия методов
class SayerA:
    def say(self):
        print("a")


class SayerB:
    def say(self):
        print("b")


class SayerAB(SayerA, SayerB):
    pass


class SayerBA(SayerB, SayerA):
    pass


# в наследниках метод выбирается по первому указанному в родителях классу
# ab = SayerAB()
# ab.say()

# ba = SayerBA()
# ba.say()
